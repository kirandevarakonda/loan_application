# loan_application_service/models.py
from mongoengine import Document, StringField, IntField, FloatField, BooleanField

class LoanApplication(Document):
    applicant_name = StringField(required=True)
    credit_score = IntField(required=True)
    loan_amount = FloatField(required=True)
    loan_purpose = StringField(required=True)
    income = FloatField(required=True)
    employment_status = StringField(required=True)
    risk_score = IntField()
    approval_status = BooleanField()
