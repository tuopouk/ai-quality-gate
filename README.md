# AI Quality Gate Example

This repository contains the evaluation logic for testing LLM Agents, designed to run in Azure DevOps.

## Local Testing

You don't need Azure DevOps to test the Python logic. To run this locally:

1. Clone the repository.
2. Create a virtual environment: `python3 -m venv venv && source venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Rename `.env.example` to `.env` and fill in your test credentials.
5. Run the evaluation: `python3 -m agent.run_evaluations`
6. Generate the report: `python3 analyze_result.py`

## Production Deployment (Azure DevOps)

To deploy this in production, use the provided `azure-pipelines.yaml` file in your Azure DevOps project. The pipeline will automatically fetch credentials securely from Azure Key Vault.