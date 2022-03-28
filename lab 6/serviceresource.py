import boto3
import os
import pandas as pd

s3 = boto3.resource(
    service_name='s3',
    region_name='us-east-1',
    aws_access_key_id="AKIAY54725OR3UTCCXUR",
    aws_secret_access_key='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'
)
os.environ["AWS_DEFAULT_REGION"] = 'us-east-1'
os.environ["AWS_ACCESS_KEY_ID"] = "AKIAY54725OR3UTCCXUR"
os.environ["AWS_SECRET_ACCESS_KEY"] = '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'

# Make dataframes
foo = pd.DataFrame({'x': [1, 2, 3], 'y': ['a', 'b', 'c']})
bar = pd.DataFrame({'x': [10, 20, 30], 'y': ['aa', 'bb', 'cc']})

# Save to csv
foo.to_csv('foo.csv')
bar.to_csv('bar.csv')

# Upload files to S3 bucket
s3.Bucket('a-very-cool-bucket').upload_file(Filename='foo.csv', Key='foo.csv')
s3.Bucket('a-very-cool-bucket').upload_file(Filename='bar.csv', Key='bar.csv')

for obj in s3.Bucket('a-very-cool-bucket').objects.all():
    print(obj)

# s3.ObjectSummary(bucket_name='a-very-cool-bucket', key='bar.csv')
# s3.ObjectSummary(bucket_name='a-very-cool-bucket', key='foo.csv')

# Load csv file directly into python
obj = s3.Bucket('a-very-cool-bucket').Object('foo.csv').get()
foo = pd.read_csv(obj['Body'], index_col=0)

# Download file and read from disc
s3.Bucket('a-very-cool-bucket').download_file(Key='foo.csv', Filename='foo2.csv')
pd.read_csv('foo2.csv', index_col=0)
