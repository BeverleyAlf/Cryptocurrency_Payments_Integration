import requests

class CryptocurrencyPaymentGateway:
    def __init__(self, api_key, secret_key):
        self.api_key = api_key
        self.secret_key = secret_key
        self.base_url = "https://api.payment-gateway.com"

    def initiate_transaction(self, amount, currency, customer_email):
        # Make API call to initiate the cryptocurrency payment
        url = f"{self.base_url}/initiate-transaction"
        headers = {
            'Authorization': f"Bearer {self.api_key}"
        }
        data = {
            'amount': amount,
            'currency': currency,
            'customer_email': customer_email
        }
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            return response.json()['transaction_id']
        else:
            print("Error initiating transaction:", response.text)
            return None

    def check_transaction_status(self, transaction_id):
        # Make API call to check the status of a transaction
        url = f"{self.base_url}/transaction/{transaction_id}"
        headers = {
            'Authorization': f"Bearer {self.api_key}"
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()['status']
        else:
            print("Error checking transaction status:", response.text)
            return None

# Example usage:

# Set up API keys and credentials from the cryptocurrency payment gateway provider
api_key = "your_api_key"
secret_key = "your_secret_key"

# Create an instance of CryptocurrencyPaymentGateway
payment_gateway = CryptocurrencyPaymentGateway(api_key, secret_key)

# Initiate a transaction
amount = 100.0
currency = "USD"
customer_email = "customer@example.com"
transaction_id = payment_gateway.initiate_transaction(amount, currency, customer_email)
if transaction_id:
    print("Transaction initiated. Transaction ID:", transaction_id)
else:
    print("Error initiating transaction.")

# Check transaction status
if transaction_id:
    status = payment_gateway.check_transaction_status(transaction_id)
    if status:
        print("Transaction Status:", status)
    else:
        print("Error checking transaction status.")
