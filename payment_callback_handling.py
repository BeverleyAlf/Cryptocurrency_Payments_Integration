from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/payment-callback', methods=['POST'])
def payment_callback():
    # Handle payment callback from the cryptocurrency payment gateway
    transaction_id = request.json.get('transaction_id')
    status = request.json.get('status')

    # Update the transaction status in your platform's database
    # Example: update_transaction_status_in_database(transaction_id, status)

    return jsonify({'message': 'Payment callback received successfully'})

if __name__ == '__main__':
    app.run(debug=True)
