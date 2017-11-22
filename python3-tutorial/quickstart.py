# -*- coding: utf-8 -*-
import boto3
import json
s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)

#ec2 = boto3.client('ec2')
#response = ec2.describe_instances()
#print(response)


#import boto3    
ec2client = boto3.client('ec2')
#response = ec2client.describe_instances(
#	 Filters=[
#        {B
#            'Name': 'instance-state-name',
#            'Values': [
#                'stopped',
#            ]
#        }
#    ],

#	)
response = ec2client.describe_instances(
    Filters=[
        {
            'Name': 'instance-state-name',
            'Values': [
                'stopped',
            ]
        },
    ],
    #InstanceIds=[
    #    'string',
    #],
    #DryRun=False,
    #MaxResults=123,
    #NextToken='string'
)
i = 0
#file = open ('output.json', 'w')
#fo = open("foo.txt", "w")
#fo.write( "Python is a great language.\nYeah its great!!\n")
#fo.close()

#with open('data.txt', 'w') as outfile:
#    json.dump(response, outfile)

for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
    	i = i + 1
        # This sample print will output entire Dictionary object
        #print(instance)
        # This will print will output the value of the Dictionary key 'InstanceId'
        #print(instance["InstanceId"],instance["State"])
        print(instance['InstanceId'])
    print(i)
    #for instance in reservation["Groups"]:
        # This sample print will output entire Dictionary object
        #print(instance)
        # This will print will output the value of the Dictionary key 'InstanceId'
        #print(instance["GroupName"])



