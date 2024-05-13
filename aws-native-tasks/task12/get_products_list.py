import json
import boto3

dynamodb = boto3.resource('dynamodb')
products_table = dynamodb.Table('cmtr-c8cf47fa-dynamodb-l-table-products')
stocks_table = dynamodb.Table('cmtr-c8cf47fa-dynamodb-l-table-stocks')


def get_product(product_id: str) -> dict:

    product_entry = products_table.get_item(Key={"id": product_id})
    print("Product entry: ", product_entry)
    stock_entry = stocks_table.get_item(Key={"product_id": product_id})
    print("Stock entry: ", stock_entry)
    
    return {
        "id": {
            "S": product_entry["Item"]["id"],
        },
        "title": {
            "S": product_entry["Item"]["title"],
        },
        "description": {
            "S": product_entry["Item"]["description"],
        },
        "price": {
            "N": str(product_entry["Item"]["price"]),
        },
        "count": {
            "N": str(stock_entry["Item"]["count"]),
        }
    }


def lambda_handler(event, context):

    print("Event: ", event)

    uuid = '14ba3d6a-a5ed-491b-a128-0a32b71a38c4'

    if 'headers' in event and 'random-uuid' in event["headers"]:
        uuid += f'-{event["headers"]["random-uuid"]}'

    product = get_product(uuid)

    return product
