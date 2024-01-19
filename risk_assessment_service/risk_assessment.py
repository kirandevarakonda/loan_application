# risk_assessment.py

class RiskAssessment:
    @staticmethod
    def calculate_risk_score(loan_application):
        # Define weights for each factor
        credit_score_weight = 0.4
        debt_to_income_weight = 0.3
        employment_status_weight = 0.2
        loan_amount_weight = 0.1

        # Normalize credit score to be between 0 and 1
        normalized_credit_score = loan_application['credit_score'] / 800.0  # Assuming a maximum credit score of 800

        # Normalize debt-to-income ratio to be between 0 and 1
        normalized_debt_to_income = min(loan_application['income'] / loan_application['loan_amount'], 1.0)

        # Determine employment status score (1.0 for Employed, 0.5 for other statuses)
        employment_status_score = 1.0 if loan_application['employment_status'] == "Employed" else 0.5

        # Determine loan amount score (1.0 for amounts <= $50,000, 0.5 otherwise)
        loan_amount_score = 1.0 if loan_application['loan_amount'] <= 50000 else 0.5

        # Combine scores using weights to get the overall risk score
        risk_score = (
            normalized_credit_score * credit_score_weight +
            normalized_debt_to_income * debt_to_income_weight +
            employment_status_score * employment_status_weight +
            loan_amount_score * loan_amount_weight
        )

        return risk_score
