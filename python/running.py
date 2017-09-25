import boto3
import datetime as dt
from influxdb import InfluxDBClient

ec2 = boto3.client('ec2');
cloudwatch = boto3.client('cloudwatch');
tagName = "aws:cloudformation:stack-name"
tagValue = "EC2ContainerService-influxdb-cluster"


def lambda_handler(event, context):
    point = make_payload()

    client = InfluxDBClient('ec2-34-228-233-250.compute-1.amazonaws.com', 8086, 'root', 'root', 'example')
    # Check database is there
    # If yes write_points
    # Else make database, then write points
    # Close connection
    return point


def make_payload():
    number = get_running_count()
    json_body = [
        {
            "measurement": "number_of_running_instances",
            "tags": {
                "region": boto3.session.Session().region_name
            },
            "time": str(dt.datetime.now()),
            "fields": {
                "value": number
            }
        }
    ]
    return json_body


def get_running_count():
    count = 0
    response = ec2.describe_instances()
    print(response)

    for r in response['Reservations']:
        for i in r['Instances']:
            print(i['State'])
            if 'Tags' in i and i['State']['Name'] == 'running':
                for t in i['Tags']:
                    if t['Key'] == tagName and t['Value'] == tagValue:
                        count += 1
    return count
