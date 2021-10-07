#!/bin/sh


yum install -y python python-dev python-pip
pip install boto3
yum -y update
yum install -y httpd
service httpd start
amazon-linux-extras install -y docker
service docker start
wget https://cs351-lab2.s3.amazonaws.com/docker-ignore-tomcat.zip
unzip docker-ignore-tomcat.zip
(cd docker-ignore-tomcat && docker build -t sample-tomcat . && docker run -d -p 8081:8080 sample-tomcat)







