import boto3
from influxdb import InfluxDBClient

ec2 = boto3.client('ec2');
cloudwatch = boto3.client('cloudwatch');
client = InfluxDBClient()

def lambda_handler(event, context):
    number = get_running_count()
    json_body = [
        {
            "measurement": "number_of_running_instances",
            "tags": {
                "region": boto3.session.Session().region_name,
            },
            "time": datetime.datetime.now(),
            "fields": {
                "value": number
            }
        }
    ]

def get_running_count():
    count = 0
    response = ec2.describe_instances()

    for r in response['Reservations']:
        for i in r['Instances']:
            print(i['State'])
            if i['State']['Name'] == 'running':
                count += 1
    return count
