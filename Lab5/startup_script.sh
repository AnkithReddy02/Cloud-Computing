#!/usr/bin/python



import os


os.system('yum install -y python python-dev python-pip')
os.system('pip install boto3')


os.system('sudo yum update -y')
os.system('sudo amazon-linux-extras install -y lamp-mariadb10.2-php7.2 php7.2')
os.system('sudo yum install -y httpd')
os.system('sudo systemctl start httpd')
os.system('sudo usermod -a -G apache ec2-user')
os.system('sudo chown -R ec2-user:apache /var/www')
os.system('sudo chmod 2775 /var/www')
os.system('find /var/www -type d -exec sudo chmod 2775 {} \;')
os.system('find /var/www -type f -exec sudo chmod 0664 {} \;')

os.system('mkdir var/www/inc')
os.system("""echo " <?php define('DB_SERVER', 'ankithreddy.cbrgivjp7kpl.us-east-1.rds.amazonaws.com');define('DB_USERNAME', 'ankithreddy');define('DB_PASSWORD', 'ankithreddy');
define('DB_DATABASE', 'ankithreddy');?>" >> var/www/inc/dbinfo.inc""")

import boto3


access_id_key = "ASIA2QSCNKB266E2JSI4"
secret_access_key = "vjiHZz7oLQQdKtK5lERUU3rJrMNRW3lsg7W1qhjF"
session_token_key = "FwoGZXIvYXdzEM3//////////wEaDFGuhcB0RGMXG3wIfCLKAYBL7kaw1Ms2ULgQ/erP/juti5XSyFpXYJeOczdHJzQMHtimUpPkvVp3taH0VJcJvIq8diLG1PdTh9MKSQKoDkqZ+IODS0qzHIahDOLjhBmygPp5Z7mDQBXBQwavpSaBmNx+jhCA2km9xSW4ARjg0vtCzYwXZWncFWV0NrCbzn69Aq4H4PJmbDuMiHuRKvrISd0/PQY4bvhSZ7xpLeBcfPc6AJXK6NeMGpeht1OkC9BHC7hnA5Ut6uwIdCqP2moqTfXRJ29IhlLy5pEo8+GvigYyLUfO1/jEmLO2e+lEd+VwvaVThFsDTgL9CEn2tfaE65bhwhzrvQyQkDYkHvV7uQ=="


s3 = boto3.resource('s3',aws_access_key_id = access_id_key,aws_secret_access_key = secret_access_key,aws_session_token = session_token_key)

my_bucket = s3.Bucket('cs351-lab2')

s3client = boto3.client('s3',aws_access_key_id = access_id_key,aws_secret_access_key = secret_access_key,aws_session_token = session_token_key)


for file_object in my_bucket.objects.all():
    s3client.download_file('cs351-lab2',file_object.key,'var/www/html/'+file_object.key)
