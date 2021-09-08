import boto3


# aws configuration
access_id_key = 'ASIA2QSCNKB22OK423HH'
secret_access_key = 'PZNBAge3IlspHInQjhiDGKMN9quZeL4Tr/lLnrb/'
session_token_key = 'FwoGZXIvYXdzEGYaDBRcQ71J7o9e3rfDSSLKAfg7CZukR6zQy/f8B3PUHau6rRk3TFcfS/4MX2XjNgcV49B1VXlledFH+E1NTZ9dJNWR45vYlTqbjV82P0Cimx7fh6dPXTx3XdOXFuyGSPXCXsfay5px8Y9atkO3hF+36EhhW+AyK9JJ3bnHLmVhIE40rOHhJPoI5nh4TnerLzTV0d2LhvKDR/vkZfZj4Vf7kBINjmEnS/J5PukAXakCcKrU+s+vzOmafEC+VSmNg8gKWONtBU7TYhOsjpWA7XeUEMwomSIctXLGYmsoju/giQYyLUcRIVSXLUK/MZ1kDcMW8uscHf4S2X69gvXYy852FJ+7iOeutbra6ziUE42/hA=='



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







