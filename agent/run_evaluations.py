import pandas as pd
from agent.agent_core import AgentCore
import sys

def fetch_golden_dataset():
    """
    Simulates fetching the Golden Dataset dynamically from a Fabric Lakehouse.
    """
    print("Fetching Golden Dataset from Microsoft Fabric Lakehouse...")
    # In production, connect to Fabric OneLake / SQL endpoint here
    return [
        {"id": 1, "query": "What is the capital of France?", "expected": "Paris"},
        {"id": 2, "query": "Is Azure DevOps a Microsoft product?", "expected": "Yes"}
    ]

def llm_judge(predicted: str, expected: str) -> bool:
    """
    In Part 2, we will implement the complex LLM-as-a-Judge logic here.
    For now, this returns a simple mock evaluation.
    """
    return expected.lower() in predicted.lower()

def main():
    agent = AgentCore()
    dataset = fetch_golden_dataset()
    results = []

    print("Starting LLM-as-a-Judge Evaluation...")
    for item in dataset:
        # 1. Ask the agent
        # Mocking the output for the sake of the skeleton
        predicted_answer = agent.process_query(item["query"], mock_response=item["expected"]) 
        
        # 2. Judge the output
        is_pass = llm_judge(predicted_answer, item["expected"])
        
        results.append({
            "Query": item["query"],
            "Expected": item["expected"],
            "Predicted": predicted_answer,
            "Pass": is_pass
        })

    # 3. Export raw data for the analyze_result step
    df = pd.DataFrame(results)
    csv_path = "contoso_ai_evaluation_report.csv"
    df.to_csv(csv_path, index=False)
    print(f"Evaluation completed. Raw data saved to {csv_path}")

if __name__ == "__main__":
    main()