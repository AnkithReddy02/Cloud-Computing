#!/usr/bin/python



import os


# python script file


# no need of sudo as cript is being executed by the root user.

# installing pip
os.system('yum install -y python python-dev python-pip')


# installing boto3
os.system('pip install boto3')


os.system('yum -y update')
os.system('yum install -y httpd')
os.system('service httpd start')

# directing to user folder
# os.system('cd ~')


# os.system('cd /var/www/html')




import boto3



# aws configuration
access_id_key = 'ASIA2QSCNKB22OK423HH'
secret_access_key = 'PZNBAge3IlspHInQjhiDGKMN9quZeL4Tr/lLnrb/'
session_token_key = 'FwoGZXIvYXdzEGYaDBRcQ71J7o9e3rfDSSLKAfg7CZukR6zQy/f8B3PUHau6rRk3TFcfS/4MX2XjNgcV49B1VXlledFH+E1NTZ9dJNWR45vYlTqbjV82P0Cimx7fh6dPXTx3XdOXFuyGSPXCXsfay5px8Y9atkO3hF+36EhhW+AyK9JJ3bnHLmVhIE40rOHhJPoI5nh4TnerLzTV0d2LhvKDR/vkZfZj4Vf7kBINjmEnS/J5PukAXakCcKrU+s+vzOmafEC+VSmNg8gKWONtBU7TYhOsjpWA7XeUEMwomSIctXLGYmsoju/giQYyLUcRIVSXLUK/MZ1kDcMW8uscHf4S2X69gvXYy852FJ+7iOeutbra6ziUE42/hA=='


# using s3 resource to use s3bucket along with configuration
s3 = boto3.resource('s3',aws_access_key_id = access_id_key,aws_secret_access_key = secret_access_key,aws_session_token = session_token_key)

# getting my bucket
my_bucket = s3.Bucket('cs351-lab2')

# using client to download files along with configuration
s3client = boto3.client('s3',aws_access_key_id = access_id_key,aws_secret_access_key = secret_access_key,aws_session_token = session_token_key)


# for doqnloading all files
# these files will be downloaded to the /var/www/html/ folder
for file_object in my_bucket.objects.all():
    # parameters : (bucketname, filename to be downloaded, path along with what name to be downloaded)
    s3client.download_file('cs351-lab2',file_object.key,'var/www/html/'+file_object.key)


# single file specifaclly also can  be downloaded 