import boto3


access_id_key = "ASIA2QSCNKB266E2JSI4"
secret_access_key = "vjiHZz7oLQQdKtK5lERUU3rJrMNRW3lsg7W1qhjF"
session_token_key = "FwoGZXIvYXdzEM3//////////wEaDFGuhcB0RGMXG3wIfCLKAYBL7kaw1Ms2ULgQ/erP/juti5XSyFpXYJeOczdHJzQMHtimUpPkvVp3taH0VJcJvIq8diLG1PdTh9MKSQKoDkqZ+IODS0qzHIahDOLjhBmygPp5Z7mDQBXBQwavpSaBmNx+jhCA2km9xSW4ARjg0vtCzYwXZWncFWV0NrCbzn69Aq4H4PJmbDuMiHuRKvrISd0/PQY4bvhSZ7xpLeBcfPc6AJXK6NeMGpeht1OkC9BHC7hnA5Ut6uwIdCqP2moqTfXRJ29IhlLy5pEo8+GvigYyLUfO1/jEmLO2e+lEd+VwvaVThFsDTgL9CEn2tfaE65bhwhzrvQyQkDYkHvV7uQ=="

ec2 = boto3.resource(
    "ec2",
    aws_access_key_id=access_id_key,
    aws_secret_access_key=secret_access_key,
    aws_session_token=session_token_key,
    region_name="us-east-1",
)

instances = ec2.create_instances(
    ImageId="ami-0c2b8ca1dad447f8a",
    MinCount=1,
    MaxCount=1,
    InstanceType="t2.micro",
    KeyName="CS351-CG31-KP",
    SecurityGroupIds=["sg-01baf3d627edad858"],
    UserData=open("C:/Users/ankit/Desktop/lab5/lab5/startup_script.sh").read(),
)


print(instances)


instance = instances[0]
instance.wait_until_running()
instance.load()

print(instance.public_dns_name)
