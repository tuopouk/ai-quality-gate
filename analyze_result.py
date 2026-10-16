import pandas as pd
import sys

def generate_html_report(df: pd.DataFrame, pass_rate: float, threshold: float):
    """
    Generates a simple HTML report for Azure DevOps pipeline artifacts.
    """
    html_content = f"""
    <html>
    <head><title>AI Quality Gate Report</title></head>
    <body style="font-family: Arial, sans-serif;">
        <h2>Contoso AI Quality Gate Report</h2>
        <p><strong>Pass Rate:</strong> {pass_rate:.2f}%</p>
        <p><strong>Threshold:</strong> {threshold:.2f}%</p>
        <hr>
        <h3>Details:</h3>
        {df.to_html(index=False, border=1)}
    </body>
    </html>
    """
    with open("contoso_ai_final_report.html", "w") as f:
        f.write(html_content)

def main():
    threshold = 90.0 # 90% accuracy required to pass the Quality Gate
    
    try:
        df = pd.read_csv("contoso_ai_evaluation_report.csv")
    except FileNotFoundError:
        print("Error: Evaluation CSV not found. Did run_evaluations.py fail?")
        sys.exit(1)

    total_tests = len(df)
    passed_tests = df['Pass'].sum()
    pass_rate = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

    print(f"Generating HTML report. Pass rate: {pass_rate:.2f}%")
    generate_html_report(df, pass_rate, threshold)

    if pass_rate < threshold:
        print(f"❌ QUALITY GATE FAILED! Pass rate {pass_rate:.2f}% is below threshold {threshold:.2f}%.")
        sys.exit(1) # This fails the Azure DevOps Pipeline and blocks the Pull Request
    else:
        print(f"✅ QUALITY GATE PASSED! Pass rate {pass_rate:.2f}% meets the threshold.")
        sys.exit(0)

if __name__ == "__main__":
    main()