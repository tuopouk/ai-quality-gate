import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

# Ladataan lokaalit muuttujat .env -tiedostosta (jos sellainen on olemassa)
load_dotenv()

class Config:
    """
    Handles dynamic credential fetching.
    - Local Dev: Reads from .env
    - Production (DevOps): Fetches dynamically from Azure Key Vault
    """
    def __init__(self):
        self.kv_url = os.getenv("KEY_VAULT_URL")
        
        # If a Key Vault URL is provided, set up the Azure connection
        if self.kv_url:
            self.credential = DefaultAzureCredential()
            self.client = SecretClient(vault_url=self.kv_url, credential=self.credential)
            print("Config: Running in Production mode (Azure Key Vault)")
        else:
            self.client = None
            print("Config: Running in Local mode (.env fallback)")

    def get_secret(self, secret_name: str) -> str:
        """
        Tries to fetch from Key Vault first. 
        Falls back to local environment variables (.env).
        """
        if self.client:
            try:
                return self.client.get_secret(secret_name).value
            except Exception as e:
                print(f"Warning: Could not fetch {secret_name} from Key Vault: {e}")
                
        # Fallback to local .env variable (convert kebab-case to UPPER_SNAKE_CASE)
        env_var_name = secret_name.replace("-", "_").upper()
        return os.getenv(env_var_name, "")

# Initialize global config
config = Config()