
from src.researcher_logic import ResearcherLogic

def start_discovery():
    # Mock 'Product Data' payload
    mock_policy = {
        "Version": "2012-10-17",
        "Statement": [{"Effect": "Allow", "Action": "*", "Resource": "*"}]
    }

    researcher = ResearcherLogic()
    analysis = researcher.analyze_policy(mock_policy)

    print(f"--- Identity Guardian: Analysis Report ---")
    print(f"Risk Score: {analysis['risk_score']}")
    print(f"Findings: {analysis['findings']}")

if __name__ == "__main__":
    start_discovery()