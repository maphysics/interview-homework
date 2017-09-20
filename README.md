# Interview Homework

Notes:
20170919 
* added influxdb image to ECR, need to verify ports and incorporate docker-compose file.  Normally this is done with ecs-cli; however, it is unavailable for windows.  Need to decided about spinning up a linux vm for this task.  Most likely possible through AWS ECS UI as well.
	* using container-transform to convert the docker-compose to an ecs task https://github.com/micahhausler/container-transform


## Problem 1

### Scenario
Due to data requirements, developers need to spin up application and database instances in a special AWS account to be able to test their code.  In order to contain costs, the SRE team needs to keep track of how many instances are running at any given time to make sure that we do not cross certain cost thresholds.

### Requirement
Create a Lambda function that can be run on a regular schedule (Cloudwatch Events) that get the number of EC2 Instances running in an account that have a specific tag and put the results in an InfluxDB.

### Instructions
Fork this repo to your personal GitHub account.  After you have completed your function, email a link to your repository for review (an address will be provided to you).  For convenience. , an InfluxDB Docker compose file is included to spin up the InfluxDB

## What You Will Need
1.  A GitHub account
2.  AWS Account
3.  Docker

