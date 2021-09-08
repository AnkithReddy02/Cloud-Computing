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
access_id_key = 'ASIA2QSCNKB2WDBS2OSX'
secret_access_key = 'J0yeMQzTVGbS3Bhgkmg76hZYZjxvnr3xixAjEw+b'
session_token_key = 'FwoGZXIvYXdzEHMaDJOIDfosn25M1PpM7yLKAV8E6TLm/fxTj5WAzmV0QCHj2CAicycZBdIL3gIw3RytbwN+Ljumq6wdc6F/j2L8pQwaDxxCvG3beRfSk7sH24WSbTG2ItXac+u4hq6Md6g/Zz1U4dSPJiExk4B5xcobf/3eEKEJWewEog3lpNG6fgD7k2h4ahx29gf4hm7JgwNh8heudOIbFVEhOTM8tZ0c7d1EToNed0MRKS1lnXZe2y2Ew+YzzhWaVnGItT5xTUtyz7y7mc3ghy/UM93HdyaQfzKLJ/kAFXjlmNAox+jjiQYyLXhKk76wtBX05SmvB8SW9pu6KGzEsXPlhrwoEaTcadB8rqepP3tAq1jLiWCeCA=='


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