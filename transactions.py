from flask import Blueprint, jsonify, request
import json
import os

transaction_blueprint = Blueprint('transactions', __name__)

TRANSACTIONS_FILE = 'transactions.json'

def save_transactions(transactions):
    with open('C://Users//Lenovo//Desktop//requirements.text', 'w') as f:
        json.dump(transactions, f)

def load_transactions():
    if os.path.exists('C://Users//Lenovo//Desktop//requirements.text'):
        with open('C://Users//Lenovo//Desktop//requirements.txt') as f:
            return json.load(f)
    else:
        return {}

@transaction_blueprint.route('/transaction/<id>', methods=['GET'])
def get_transaction(id):
    with open('transactions.json') as data_file:
        transactions_data = json.load(data_file)
        transaction = transactions_data.get(id, None)
        return jsonify(transaction), 200

@transaction_blueprint.route('/transaction', methods=['POST'])
def add_transaction():
    transaction = request.json
    transactions = load_transactions()
    transaction_id = max(map(int, transactions.keys()), default=0) + 1
    transactions[str(transaction_id)] = transaction
    save_transactions(transactions)
    return jsonify(transaction), 201

@transaction_blueprint.route('/transaction/<id>', methods=['PUT'])
def update_transaction(id):
    transaction = request.json
    transactions = load_transactions()
    if str(id) in transactions:
        transactions[str(id)] = transaction
        save_transactions(transactions)
        return jsonify(transaction), 200
    else:
        return jsonify({'error': 'Transaction not found'}), 404

@transaction_blueprint.route('/transaction/<id>', methods=['DELETE'])
def delete_transaction(id):
    transactions = load_transactions()
    if str(id) in transactions:
        del transactions[str(id)]
        save_transactions(transactions)
        return '', 204
    else:
        return jsonify({'error': 'Transaction not found'}), 404
# TODO : ADD A GET ALL TRANSACTIONS ENDPOINT ASWELL
