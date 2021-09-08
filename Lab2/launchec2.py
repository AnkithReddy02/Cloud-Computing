import boto3


# aws configuration
access_id_key = ''
secret_access_key = ''
session_token_key = ''

ec2 = boto3.resource('ec2',aws_access_key_id = access_id_key,aws_secret_access_key = secret_access_key,aws_session_token = session_token_key,region_name='us-east-1')

# returns the instace id's of teh instances created.
instances = ec2.create_instances(ImageId='ami-0c2b8ca1dad447f8a', MinCount=1, MaxCount=1, InstanceType = 't2.micro',KeyName='CS351-CG31-KP',
SecurityGroupIds=['sg-01baf3d627edad858'], UserData = open("C:/Users/ankit/Desktop/cloudlab/lab2/lab2/startup_script.sh").read())


# printing instances id's list that are created
print(instances)



# taking the first instance as there is only one instance created
instance = instances[0]
# wait till the status of 'instance' changed to 'running'
instance.wait_until_running()
instance.load()

# print dns server name
print(instance.public_dns_name)







