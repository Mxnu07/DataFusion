import pandas as pd
import yaml
import xml.etree.ElementTree as ET

def load_json(file_path):
    return pd.read_json(file_path)

def load_yaml(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return pd.DataFrame(data)

def load_csv(file_path):
    return pd.read_csv(file_path)

def load_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    transactions = []

    # Extract transaction data
    for trans in root.findall('transaction'):
        transaction_id = trans.get('id')
        phone = trans.find('phone').text
        store = trans.find('store').text
        items = []
        for item in trans.findall('items/item'):
            item_name = item.find('item').text
            price = float(item.find('price').text)
            quantity = int(item.find('quantity').text)
            items.append({
                'transaction_id': transaction_id,
                'item_name': item_name,
                'price': price,
                'quantity': quantity,
                'phone': phone,
                'store': store
            })
        transactions.extend(items)
    return pd.DataFrame(transactions)
