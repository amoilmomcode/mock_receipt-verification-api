import receipt.baseReceipt as base

class AppleReceipt(base.Receipt):
    def verify(self):
        # verify logic here in real life.
        import random

        result = random.choice((True, False))

        if result:
            self.status = "valid"

        return result

