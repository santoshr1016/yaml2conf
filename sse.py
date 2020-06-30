import boto3
import botocore

# https://docs.aws.amazon.com/AmazonS3/latest/user-guide/add-object-encryption.html
# https://docs.amazonaws.cn/en_us/AmazonS3/latest/API/ErrorResponses.html#ErrorCodeList

s3_client = boto3.client('s3')
response = s3_client.list_buckets()

for bucket in response['Buckets']:
  try:
    enc = s3_client.get_bucket_encryption(Bucket=bucket['Name'])
    rules = enc['ServerSideEncryptionConfiguration']['Rules']
    print('Bucket: %s, Encryption: %s' % (bucket['Name'], rules))
  except botocore.exceptions.ClientError as error:
    if error.response['Error']['Code'] == 'ServerSideEncryptionConfigurationNotFoundError':
      print('Bucket: %s, no server-side encryption' % (bucket['Name']))
    else:
      print("Bucket: %s, unexpected error: %s" % (bucket['Name'], error))

