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
Access_key='AKIA4ZSUVQ5PNEUI25VH'
Secret_key='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'
s='start'
print("start")
for i in range(num):
    print(get_time())
    s += ','+str(get_time())
    time.sleep(60)
print('end')
s += ','+'end'
client = boto3.client(
    's3',
    aws_access_key_id=Access_key,
    aws_secret_access_key=Secret_key)
s3 = client
bucket_name = 'bucketmaharshi'
object_key = str(num)+' min'
response = s3.put_object(Bucket=bucket_name, Key=object_key, Body=s)
print(s)
