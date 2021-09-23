#!pip install boto3

import boto3


access_id_key = "ASIA2QSCNKB2ZENDC4NK"
secret_access_key = "kfR4mX4ZFvzkxFUaiovC3gQThWV8U1rmsRbkAlQK"
session_token_key = "FwoGZXIvYXdzECUaDBUwX/jilptszH8H0CLKAUVkCXSsskj6VEWrY07JBJ5Hmdo/TBFCDGd/ITIZ8ktoLwcvrp+/24wq7rgFmCziHlS1nYBlRPVaH69RvnealE2J9YrkHlxkvqNrb6rnumCH4Q+5WYqvYnNTDaO+QSeVX0fyabe29UkAMdMBVukbNJDvbh6QooR80enl12JR3DaR1nGUCniOyGYppjQtqJSIYY96Qw/pR0489QT4rBkG9P4eHXwz3Zrq1d+OdB/kjT0JkUf1OK+wj9teRvrCzwN0IIbE9ETs20k+IZsoxPSKigYyLRlaDSknWXHMUjRVR0QhyX6emo1yerJOKIlDt3TDXSbBN84CZI+of9llXo4pVw=="


"""

cf = boto3.client(
    "cloudfront",
    region_name="us-east-1",
    aws_access_key_id=access_id_key,
    aws_secret_access_key=secret_access_key,
    aws_session_token=session_token_key
    )

response = cf.create_distribution(
        DistributionConfig={
            "CallerReference": "my-distribution-cdn",
            "DefaultRootObject": "index.html",
            "Origins": {
                "Quantity": 1,
                "Items": [
                    {
                        "Id": "cs351-lab2",
                        "DomainName": "cs351-lab2.s3.us-east-1.amazonaws.com",
                        "S3OriginConfig": {"OriginAccessIdentity": ""},
                    },
                ],
            },
            "DefaultCacheBehavior": {
                "TargetOriginId": "cs351-lab2",
                "ViewerProtocolPolicy": "allow-all",
                "AllowedMethods": {
                    "Quantity": 1,
                    "Items": [
                        "GET",
                        "HEAD",
                        "POST",
                        "PUT",
                        "PATCH",
                        "OPTIONS",
                        "DELETE",
                    ],
                    "CachedMethods": {
                        "Quantity": 1,
                        "Items": [
                            "GET",
                            "HEAD",
                            "POST",
                            "PUT",
                            "PATCH",
                            "OPTIONS",
                            "DELETE",
                        ],
                    },
                },
            },
            "Comment": "Hosting Dynamic website",
            "Enabled": True,
        }
    )
print(response)

"""

s3 = boto3.client(
    "s3",
    aws_access_key_id=access_id_key,
    aws_secret_access_key=secret_access_key,
    aws_session_token=session_token_key,
)
s3.upload_file(
    "C:/Users/ankit/Desktop/cloudlab/lab4/RealEstate.war",
    "cs351-lab2",
    "RealEstate.war",
)

import boto3


boto3client = boto3.client(
    "elasticbeanstalk",
    region_name="us-east-1",
    aws_access_key_id=access_id_key,
    aws_secret_access_key=secret_access_key,
    aws_session_token=session_token_key,
)


boto3client.create_application_version(
    ApplicationName="my-app",
    AutoCreateApplication=True,
    Description="my-app-v1",
    Process=True,
    SourceBundle={
        "S3Bucket": "cs351-lab2",
        "S3Key": "RealEstate.war",
    },
    VersionLabel="v1",
)

import time

while True:

    response = boto3client.describe_application_versions(
        ApplicationName="my-app",
        VersionLabels=[
            "v1",
        ],
        MaxRecords=123,
    )

    if response["ApplicationVersions"][0]["Status"] != "PROCESSED":
        time.sleep(5)
    else:
        break


response = boto3client.create_environment(
    ApplicationName="my-app",
    EnvironmentName="my-env",
    SolutionStackName="64bit Amazon Linux 2 v4.2.5 running Tomcat 8.5 Corretto 11",
    VersionLabel="v1",
    OptionSettings=[
        {
            "Namespace": "aws:autoscaling:launchconfiguration",
            "OptionName": "IamInstanceProfile",
            "Value": "aws-elasticbeanstalk-ec2-role",
        },
        {
            "Namespace": "aws:autoscaling:launchconfiguration",
            "OptionName": "InstanceType",
            "Value": "t2.micro",
        },
        {
            "Namespace": "aws:autoscaling:launchconfiguration",
            "OptionName": "EC2KeyName",
            "Value": "CS351-CG31-KP",
        },
        {
            "Namespace": "aws:autoscaling:launchconfiguration",
            "OptionName": "ImageId",
            "Value": "ami-087c17d1fe0178315",
        },
        {
            "Namespace": "aws:autoscaling:launchconfiguration",
            "OptionName": "SecurityGroups",
            "Value": "CS351-CG31",
        },
        {
            "Namespace": "aws:autoscaling:trigger",
            "OptionName": "BreachDuration",
            "Value": "1",
        },
        {
            "Namespace": "aws:autoscaling:trigger",
            "OptionName": "Statistic",
            "Value": "Average",
        },
        {
            "Namespace": "aws:autoscaling:trigger",
            "OptionName": "Unit",
            "Value": "Percent",
        },
        {
            "Namespace": "aws:autoscaling:trigger",
            "OptionName": "EvaluationPeriods",
            "Value": "1",
        },
        {
            "Namespace": "aws:autoscaling:trigger",
            "OptionName": "Period",
            "Value": "1",
        },
        {
            "Namespace": "aws:autoscaling:trigger",
            "OptionName": "UpperThreshold",
            "Value": "70",
        },
        {
            "Namespace": "aws:autoscaling:trigger",
            "OptionName": "UpperBreachScaleIncrement",
            "Value": "1",
        },
        {
            "Namespace": "aws:autoscaling:trigger",
            "OptionName": "MeasureName",
            "Value": "CPUUtilization",
        },
        {
            "Namespace": "aws:autoscaling:trigger",
            "OptionName": "LowerThreshold",
            "Value": "30",
        },
        {
            "Namespace": "aws:autoscaling:trigger",
            "OptionName": "LowerBreachScaleIncrement",
            "Value": "-1",
        },
        {
            "Namespace": "aws:autoscaling:asg",
            "OptionName": "Availability Zones",
            "Value": "Any 2",
        },
        {
            "Namespace": "aws:autoscaling:asg",
            "OptionName": "MaxSize",
            "Value": "3",
        },
        {
            "Namespace": "aws:autoscaling:asg",
            "OptionName": "MinSize",
            "Value": "1",
        },
    ],
)
