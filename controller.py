from flask import Flask, request, jsonify
from services import ReceiptService

app = Flask(__name__)

# Handler for processing the receipt
@app.route('/receipts/process', methods=['POST'])
def handle_process_receipt():
    data = request.json
    try:
        # Call service to create the receipt
        receipt = ReceiptService.create_receipt(
            retailer=data['retailer'],
            purchase_date=data['purchaseDate'],
            purchase_time=data['purchaseTime'],
            items=data['items'],
            total=data['total']
        )
        return jsonify({"id": receipt.id}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    

# Handler for retrieving receipt points by ID
@app.route('/receipts/<receipt_id>/points', methods=['GET'])
def handle_get_points(receipt_id):
    points = ReceiptService.get_receipt_points(receipt_id)
    if points is None:
        return jsonify({"error": "Receipt not found"}), 404
    return jsonify({"points": points}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True, port=8080)
