import json


class ResearcherLogic:
    def __init__(self):
        # Critical actions that should never have a Resource: "*"
        self.high_risk_actions = ["*", "iam:CreateAccessKey", "administratoraccess"]

    def analyze_policy(self, policy_json):
        findings = []
        risk_score = 0.0
        for statement in policy_json.get('Statement', []):
            if statement.get('Action') == "*" and statement.get('Resource') == "*":
                findings.append("🚨 Full Admin access detected.")
                risk_score = 1.0
        return {"risk_score": risk_score, "findings": findings}