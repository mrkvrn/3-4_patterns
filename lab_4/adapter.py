print("Adapter Pattern")

class LegacyPaymentService:
    def process_legacy_payment(self):
        return "SUCCESS#12345#100.00USD"

class PaymentProcessor:
    def process_payment(self):
        return "Payment processed: $100.00, ID: 12345, Status: SUCCESS"

class PaymentAdapter(PaymentProcessor):
    def __init__(self, legacy_service):
        self._legacy_service = legacy_service
    
    def process_payment(self):
        legacy_result = self._legacy_service.process_legacy_payment()
        parts = legacy_result.split('#')
        status = parts[0]
        payment_id = parts[1]
        amount = parts[2].replace('USD', '')
        return f"Payment processed: ${amount}, ID: {payment_id}, Status: {status}"
