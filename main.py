import requests
import base64


# function for getting transaction data from a block
def block_data(block_number):
    url = f'https://akash-api.w3coins.io/blocks/{block_number}'
    response = requests.get(url)

    data_list = response.json()
    transactions_data_list = data_list.get('block', {}).get('data', {}).get('txs', [])
    return transactions_data_list

# function for decoding transaction data from base64 format
def decode_transactions(data_of_transactions):
    decoded_data = []
    for data in data_of_transactions:
        decoded = base64.b64decode(data)
        decoded_data.append(decoded)
    return decoded_data

# The main function of the program
def main():
    block_number = 11260638
    data_of_transactions = block_data(block_number)

    if not data_of_transactions:
        print("No transactions in this block.")
        return 

    transactions = decode_transactions(data_of_transactions)

    for id_tran, value_tran in enumerate(transactions, start=1):
        print(f"Transaction {id_tran}: {value_tran}")


if __name__ == "__main__":
    main()
