import boto3


access_id_key = "ASIA2QSCNKB266E2JSI4"
secret_access_key = "vjiHZz7oLQQdKtK5lERUU3rJrMNRW3lsg7W1qhjF"
session_token_key = "FwoGZXIvYXdzEM3//////////wEaDFGuhcB0RGMXG3wIfCLKAYBL7kaw1Ms2ULgQ/erP/juti5XSyFpXYJeOczdHJzQMHtimUpPkvVp3taH0VJcJvIq8diLG1PdTh9MKSQKoDkqZ+IODS0qzHIahDOLjhBmygPp5Z7mDQBXBQwavpSaBmNx+jhCA2km9xSW4ARjg0vtCzYwXZWncFWV0NrCbzn69Aq4H4PJmbDuMiHuRKvrISd0/PQY4bvhSZ7xpLeBcfPc6AJXK6NeMGpeht1OkC9BHC7hnA5Ut6uwIdCqP2moqTfXRJ29IhlLy5pEo8+GvigYyLUfO1/jEmLO2e+lEd+VwvaVThFsDTgL9CEn2tfaE65bhwhzrvQyQkDYkHvV7uQ=="


rdsClient = boto3.client(
    "rds",
    aws_access_key_id=access_id_key,
    aws_secret_access_key=secret_access_key,
    aws_session_token=session_token_key,
    region_name="us-east-1",
)

response = rdsClient.create_db_instance(
    DBName="ankithreddy",
    DBInstanceIdentifier="ankithreddy",
    AllocatedStorage=5,
    DBInstanceClass="db.t2.micro",
    Engine="MySQL",
    MasterUsername="ankithreddy",
    MasterUserPassword="ankithreddy",
    PubliclyAccessible=True,
)


import time

while True:
    response = rdsClient.describe_db_instances(
        DBInstanceIdentifier="ankithreddy",
        MaxRecords=20,
    )

    status = response["DBInstances"][0]["DBInstanceStatus"]

    if status == "available" or status == "AVAILABLE":
        break
    else:
        time.sleep(10)


print(response["DBInstances"][0]["Endpoint"]["Address"])
