import boto3
import time


"""
1. Create Launch Configuration.
2. Create Auto Scaling Group
3. Scale UP and Scale DOWN policy
4. Up and Down Alarm

"""
access_id_key = ""
secret_access_key = ""
session_token_key = ""

auto_scale = boto3.client(
    "autoscaling",
    aws_access_key_id=access_id_key,
    aws_secret_access_key=secret_access_key,
    aws_session_token=session_token_key,
    region_name="us-east-1",
)

lc = auto_scale.create_launch_configuration(
    LaunchConfigurationName="my-launch-configuration",
    InstanceType="t2.micro",
    KeyName="CS351-CG31-KP",
    ImageId="ami-087c17d1fe0178315",
    SecurityGroups=["sg-01baf3d627edad858"],
    UserData=open("C:/Users/ankit/Desktop/cloudlab/lab3/startup_script.sh").read(),
)

auto_scale.create_auto_scaling_group(
    AutoScalingGroupName="my-auto-scaling-group",
    LaunchConfigurationName="my-launch-configuration",
    AvailabilityZones=["us-east-1b", "us-east-1c", "us-east-1d", "us-east-1a"],
    MinSize=1,
    MaxSize=3,
)
scale_up_policy = auto_scale.put_scaling_policy(
    # For AdjustmentType = 'ChangeInCapacity' we must specify the scaling adjustment such that whenever teh threshold goes below the minimum
    # then it will increase instances by 1.
    AdjustmentType="ChangeInCapacity",
    AutoScalingGroupName="my-auto-scaling-group",
    PolicyName="scale_up_policy",
    PolicyType="SimpleScaling",  # by default its SimpleScaling
    ScalingAdjustment=1,
)
scale_down_policy = auto_scale.put_scaling_policy(
    # For AdjustmentType = 'ChangeInCapacity' we must specify the scaling adjustment such that whenever teh threshold goes above the maximum
    # then it will decrease instances by 1.
    AdjustmentType="ChangeInCapacity",
    AutoScalingGroupName="my-auto-scaling-group",
    PolicyName="scale_down_policy",
    PolicyType="SimpleScaling",
    ScalingAdjustment=-1,
)
cloud_watch = boto3.client(
    "cloudwatch",
    aws_access_key_id=access_id_key,
    aws_secret_access_key=secret_access_key,
    aws_session_token=session_token_key,
    region_name="us-east-1",
)
cloud_watch.put_metric_alarm(
    AlarmName="up_alarm",
    Namespace="AWS/EC2",
    # we are using the threshold metric(CPUUtilization) to launch or terminate the instances
    MetricName="CPUUtilization",
    # threshold is based on average cpu utilization
    Statistic="Average",
    # comparision operator describes when to put the alarm, here in this case, it puts the alarm when the avg. CPUUtilization is GreaterThanThreshold
    ComparisonOperator="GreaterThanThreshold",
    # period describes after what time interval in secs, the data points should be considered (here data point represent how much cpu is utilized)
    Period=60,
    # EvaluationPeriods describes after how many periods of time interval, teh evaluation of metric(CPUUtilization) must be done.
    EvaluationPeriods=2,
    # DatapointsToAlarm describe, how many points are required that are above threshold( only in this case ) in the evaluation period to
    # change the state to ALARM from OK
    DatapointsToAlarm=2,
    # Upper or Maximum Threshold of CPUUtilization
    Threshold=70,
    AlarmDescription="Above 70 percent of CPUUtilization",
    AlarmActions=[scale_up_policy["PolicyARN"]],
)

cloud_watch.put_metric_alarm(
    AlarmName="down_alarm",
    Namespace="AWS/EC2",
    MetricName="CPUUtilization",
    Statistic="Average",
    ComparisonOperator="LessThanThreshold",
    Period=60,
    EvaluationPeriods=2,
    DatapointsToAlarm=2,
    Threshold=40,
    AlarmDescription="Below 40 percent of CPUUtilization",
    AlarmActions=[scale_down_policy["PolicyARN"]],
)


time.sleep(30)

response = auto_scale.describe_auto_scaling_groups(
    AutoScalingGroupNames=["my-auto-scaling-group"]
)
auto_scaling_group_list = response["AutoScalingGroups"]
req_instance_id = (((auto_scaling_group_list[0])["Instances"])[0])["InstanceId"]
print(req_instance_id)
ec2 = boto3.resource(
    "ec2",
    aws_access_key_id=access_id_key,
    aws_secret_access_key=secret_access_key,
    aws_session_token=session_token_key,
    region_name="us-east-1",
)
instance = ec2.Instance(id=req_instance_id)
instance.wait_until_running()
instance.load()
print(instance.public_dns_name)


"""

"""
