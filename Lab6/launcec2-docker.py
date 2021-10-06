import boto3


# aws configuration
access_id_key = "ASIA2QSCNKB27TWA4OF7"
secret_access_key = "ZqhRCTw6xH2Mq1Sf6sZnYqZoP7ixp7Ynyuo3WlK0"
session_token_key = "FwoGZXIvYXdzEA8aDBuN1oo9ILAZemP77iLKARtH53BSgJMDo+zmDhpzerth94CveQybIBF7vgdYp5HHno6cAkVWEifPFF/QX4MA3VkYidxJgT1Pn/x+C6MiCTnu2ljCR5SV6ksXtUWLNsM7gaYpzA5ZkAEYKLFwYj506Hn81NojkxPRHGpweuF9Z6Lmii4F2DMwlXqKt59Oym+q8D/d+5/jkPXVi/VpAfRBwo2mYjDIzJtgs4afgXgztvQMpl4uiG7vS8zPtyUQq6b8ayiyMVIdBQ6uQj3aSJH1ACUPyUh7WH5vKlsokcz2igYyLVMRmvlFyB32ozIs4Bnwyt6MhyLlrtlkMfjMpmrNwg5JHcKM4JaMKRHi4GX33A=="


ec2 = boto3.resource(
    "ec2",
    aws_access_key_id=access_id_key,
    aws_secret_access_key=secret_access_key,
    aws_session_token=session_token_key,
    region_name="us-east-1",
)

# returns the instace id's of teh instances created.
instances = ec2.create_instances(
    ImageId="ami-0c2b8ca1dad447f8a",
    MinCount=1,
    MaxCount=1,
    InstanceType="t2.micro",
    KeyName="CS351-CG31-KP",
    SecurityGroupIds=["sg-01baf3d627edad858"],
    UserData=open("C:/Users/ankit/Desktop/cloudlab/lab6/startupscript.sh").read(),
)


# printing instances id's list that are created
print(instances)


# taking the first instance as there is only one instance created
instance = instances[0]
# wait till the status of 'instance' changed to 'running'
instance.wait_until_running()
instance.load()

# print dns server name
print(instance.public_dns_name)
