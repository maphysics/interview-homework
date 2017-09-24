import boto3
from influxdb import InfluxDBClient

ec2 = boto3.client('ec2');
cloudwatch = boto3.client('cloudwatch');


def lambda_handler(event, context):
    point = make_payload()
    # Connect to client
    # Currently my ec2 running my docker image of influxdb lacks an elastic ip
    # Therefore the call may fail on instance recovery
    # If autoscaling group was enabled
    # Otherwise it will fail as no machine will come up?
    client = InfluxDBClient('ec2-34-228-233-250.compute-1.amazonaws.com', 8086, 'root', 'root', 'example')
    # Check database is there
    # If yes write_points
    # Else make database, then write points
    # Close connection


def make_payload():
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
    return json_body


def get_running_count():
    count = 0
    response = ec2.describe_instances()

    for r in response['Reservations']:
        for i in r['Instances']:
            print(i['State'])
            if i['State']['Name'] == 'running':
                count += 1
    return count
