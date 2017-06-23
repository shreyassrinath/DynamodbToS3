# Export Dynamo DB data to S3

## Introduction

Amazon DynamoDB is a fast and flexible NoSQL database service for all applications that need consistent, single-digit millisecond latency at any scale. For data durability, Tables are automatically distributed across 3 facilities in an AWS Region of your choice, and ensure continous operation even in the case of AZ level interruption of service.

There are many use cases for Dynamodb data export:

*  Maintain a baseline set of data, for testing purposes. 
    * One could put the baseline data into a DynamoDB table and export it to Amazon S3. Then, after you run an application that modifies the test data, you could "reset" the data set by importing the baseline from Amazon S3 back into the DynamoDB table.
* Accidental deletion of data, or even an accidental DeleteTable operation.
* Export data to S3 and then import data to identical table in another region so that load is reduced. 

Amazon DynamoDB provides export capability via [AWS Data pipeline](http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-importexport-ddb-part2.html) which requires spinning up of addional resources. 
The goal of this project is to provide an alternative to that approach where compute is done on the local vgrant VM. The idea is to spin up docker containers(one per dynamodb table) to export data from dynamodb to s3. 

## Installation requirements

* Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads) and [Vagrant](https://www.vagrantup.com/downloads.html)
* Clone this repo
* Drop in AWS Credentials @ config/.aws/credentials folder. The aws credentials need to have permissions to manage Dynamodb and S3. 

## Architecture

![Alt](/resources/dynamodb_to_s3.jpg "Architecture Diagram")

## Commands

`$ vagrant up`

`$ vagrant ssh`

### cd to directory

`$ cd exportDDB`

### Build and run the images using docker compose

Update the docker-compose.yml file with the dynamodb table and S3 bucket details. Adding services section per the tables being exported.

Ex:

```yml
export_myDynamoDbTable1_image:
        build:
            context: . 
            args:
                ddbTable: myDynamoDbTable1
                s3Bucket: myS3Bucket
```
Build using docker compose

`$ docker-compose build`

Run! This should export data to the specified S3 bucket/s. 

`$ docker-compose up`

