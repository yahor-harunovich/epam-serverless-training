import json

import requests

from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda


class OpenMeteoAPI:

    def __init__(self) -> None:
        self.url = "https://api.open-meteo.com/v1/forecast"

    def get_weather_forecast(self, latitude: float, longitude: float) -> dict: 
        
        response = requests.get(
            url=self.url,
            params={
                "latitude": latitude,
                "longitude": longitude,
            }
        )
        response.raise_for_status()
        forecast = response.json()
        return forecast


_LOG = get_logger('ApiHandler-handler')
open_meteo_api = OpenMeteoAPI()


class ApiHandler(AbstractLambda):

    def validate_request(self, event) -> dict:
        pass
        
    def handle_request(self, event, context):
        """
        Explain incoming event here
        """

        method = event["requestContext"]["http"]["method"]
        path = event["requestContext"]["http"]["path"]

        if method == "GET" and path == "/weather":

            latitude = 48.8566
            longitude = 2.3522
            forecast = open_meteo_api.get_weather_forecast(latitude=latitude, longitude=longitude)

            return {
                "statusCode": 200,
                "body": json.dumps(forecast)
            }

    

HANDLER = ApiHandler()


def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)
