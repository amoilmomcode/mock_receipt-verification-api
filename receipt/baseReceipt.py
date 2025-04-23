import json

class Receipt:
    def __init__(self, receipt):
        self.status = "invalid"
        self.user_id = receipt.get("user_id")
        self.platform = receipt.get("platform")
        self.receipt_id = receipt.get("receipt_id")

    def verify(self):
        pass

