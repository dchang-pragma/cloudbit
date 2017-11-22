# -*- coding: utf-8 -*-
import boto3
import json
s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)
 
ec2client = boto3.client('ec2')

response = ec2client.describe_instances(
    Filters=[
        {
            'Name': 'instance-state-name',
            'Values': [
                'stopped',
            ]
        },
    ],
)
i = 0

for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
    	i = i + 1
    	#print (instance['InstanceId'])
    	print(instance["InstanceId"],instance["State"])

        # This sample print will output entire Dictionary object
        #print(instance)
        # This will print will output the value of the Dictionary key 'InstanceId'
        #print(instance["InstanceId"])

    print (i)



