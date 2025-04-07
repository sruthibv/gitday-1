import boto3

client = boto3.client('ec2')
response = client.run_instances(
    ImageId='ami-002f6e91abff6eb96',
    InstanceType='t2.micro',
    KeyName='demo',
    MaxCount=1,
    MinCount=1
)
