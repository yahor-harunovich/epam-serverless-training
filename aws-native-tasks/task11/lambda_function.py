import datetime

import boto3


cloud_trail_client = boto3.client('cloudtrail')


def get_unique_users(start_time, end_time, next_token=None):
    unique_users = set()

    while True:
        if next_token:
            response = cloud_trail_client.lookup_events(
                StartTime=datetime.datetime.fromtimestamp(int(start_time)),
                EndTime=datetime.datetime.fromtimestamp(int(end_time)),
                NextToken=next_token,
            )
        else:
            response = cloud_trail_client.lookup_events(
                StartTime=datetime.datetime.fromtimestamp(int(start_time)),
                EndTime=datetime.datetime.fromtimestamp(int(end_time)),
            )

        events = response.get("Events", [])
        for event in events:
            username = event.get("Username")
            if username:
                unique_users.add(username)

        next_token = response.get("NextToken")
        if not next_token:
            break

    return sorted(list(unique_users))


def lambda_handler(event, context):
    start_time = event["start_time"]
    end_time = event["end_time"]

    unique_users = get_unique_users(start_time, end_time)
    return unique_users 
