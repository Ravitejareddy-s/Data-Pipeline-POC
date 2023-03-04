import boto3
s3 = boto3.client(
    's3',region_name='ap-south-1')
s="fghgf"
response = s3.put_object(Bucket='bucketmaharshi', Key='object_key.csv', Body=s)