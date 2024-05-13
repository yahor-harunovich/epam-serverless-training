import json
import boto3


dynamodb = boto3.resource('dynamodb')
products_table = dynamodb.Table('cmtr-c8cf47fa-dynamodb-l-table-products')
stocks_table = dynamodb.Table('cmtr-c8cf47fa-dynamodb-l-table-stocks')

def add_product(product: dict) -> None:

    products_table.put_item(Item={
        "id": product["id"],
        "title": product["title"],
        "description": product["description"],
        "price": product["price"],
    })
    stock_entry = {
        "product_id": product["id"],
        "count": product["count"],
    }
    stocks_table.put_item(Item=stock_entry)


def lambda_handler(event, context):

    print("Event: ", event)

    uuid = '14ba3d6a-a5ed-491b-a128-0a32b71a38c4'

    if 'headers' in event and 'random-uuid' in event["headers"]:
        uuid += f'-{event["headers"]["random-uuid"]}'

    product = {
        "id": uuid,
        "title": "Product Title",
        "description": "This product ...",
        "price": 200,
        "count": 2
    }
    add_product(product)

    return {
        "count": {
            "N": str(product["count"]),
        },
        "description": {
            "S": product["description"],
        },
        "id": {
            "S": product["id"],
        },
        "price": {
            "N": str(product["price"]),
        },
        "title": {
            "S": product["title"],
        }
    } 
