from flask import Flask, jsonify, make_response, request
from db import logReceipt
import json
from receipt.appleReceipt import AppleReceipt
from receipt.googleReceipt import GoogleReceipt

app = Flask(__name__)

def buildResponse(message):
    data = {'msg':message}
    return jsonify(data)

def getReceipt(receipt):
    match receipt.get("platform",None):
        case "google":
            return GoogleReceipt(receipt)
        case "apple":
            return AppleReceipt(receipt)
        case _:
            return None

@app.route("/receipt", methods=['POST'])
def receiptVerify():
    data = request.json

    if not data:
        return buildResponse("no data"), 503

    receipt = getReceipt(data)
    if not receipt:
        return buildResponse("invalid platform"), 503

    if not receipt.user_id or not receipt.receipt_id:
        return buildResponse("invalid id"), 503

    if receipt.verify():
        logReceipt(receipt)
    else: return buildResponse("invalid receipt"), 503

    return buildResponse("receipt verified"), 200


if __name__ == "__main__":
    app.run(debug=True)

