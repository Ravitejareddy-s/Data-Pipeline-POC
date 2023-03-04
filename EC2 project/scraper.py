import random
import pandas as pd
import time
import boto3

def get_time():
    utc_now = time.time()
    ist_offset = 5.5 * 60 * 60
    ist_time = utc_now + ist_offset
    time_str = time.strftime("%H:%M:%S", time.gmtime(ist_time))
    return(time_str)

num = random.randint(5, 40)
s='start'
print("start")
for i in range(num):
    print(get_time())
    s += ','+str(get_time())
    time.sleep(2)
print('end')
s += ','+'end'
s3 = boto3.client('s3')
bucket_name = 'bucketmaharshi'
object_key = str(num)+' min'
response = s3.put_object(Bucket=bucket_name, Key=object_key, Body=s)
print(s)
region = 'ap-south-1'
instances = ['i-0eb790bc1a0c0a808']
#ec2 = boto3.client('ec2', region_name=region)
ec2 = boto3.client('ec2',region_name=region)
ec2.stop_instances(InstanceIds=instances)
print('you should not be able to see this')