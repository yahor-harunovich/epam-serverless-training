import json
from tests.test_hello_world import HelloWorldLambdaTestCase


class TestSuccess(HelloWorldLambdaTestCase):

    def test_success(self):
        event = {
            "requestContext": {
                "http": {
                    "method": "GET",
                    "path": "/hello"
                }

            }
        }
        context = dict()
        response = {
            "statusCode": 200,
            "body": json.dumps({
                'statusCode': 200,
                'message': 'Hello from Lambda'
            })
        }
        self.assertEqual(self.HANDLER.handle_request(event, context), response)

