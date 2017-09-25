# Interview Homework
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

Notes:
20170919 
* added influxdb image to ECR, need to verify ports and incorporate docker-compose file.  Normally this is done with ecs-cli; however, it is unavailable for windows.  Need to decided about spinning up a linux vm for this task.  Most likely possible through AWS ECS UI as well.
	* using container-transform to convert the docker-compose to an ecs task https://github.com/micahhausler/container-transform
	* memory set through UI (128 to start) also removed tildas from volumn names
* ECS cluster with one container instance of influxdb running
* Stopping for the night.  Planning to pick up again 20190921 in the evening to step the ec2s for monitoring with the lambda.

20170923
* created the python deployment archive for the lambda
* started researching on influxdb works
* todo: edit Dockerfile to make the database, users, etc
* todo: regenerate task on ecs instance
* todo: update lambda function to put data in database - verify permissions/roles

20170924
* adding environment variable overrides to the ecs task
	* INFLUX_DB=instances 
	* INFLUXDB_ADMIN_USER=root 
	* INFLUXDB_AMDIN_PASSWORD=root 
	* INFLUXDB_USER=qback
	* INFLUXDB_USER_PASSWORD=hailmary

20170925
* the lamda function now checks the tag names before incrementing the sum
* task definition still produces a task that stops due to esstential process errors
* the docker image I generated for influxdb maybe incorrect or my set up of influxdb is incorrect stemming from my lack of knowledge of the database
* at this point normally, I would seek out assistance from more experienced team members. Given the assignment and time frame, I will defer asking these questions until we go over the assignment
