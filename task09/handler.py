import json


def lambda_handler(event, context):
    contacts = [
        {
            "id": 1,
            "name": "Elma Herring",
            "email": "elmaherring@unq.com",
            "phone": "+1 (913) 497-2020"
        },
        {
            "id": 2,
            "name": "Bell Burgess",
            "email": "bellburgess@unq.com",
            "phone": "+1 (887) 478-2693"
        },
        {
            "id": 3,
            "name": "Hobbs Ferrell",
            "email": "hobbsferrell@unq.com",
            "phone": "+1 (862) 581-3022"
        }
    ]
    if event["httpMethod"] == "GET" and event["resource"] == "/contacts":
        response = {
            'statusCode': 200,
            'body': json.dumps(contacts),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
        return response
