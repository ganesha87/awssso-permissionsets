import boto3

bucketName = 'tf-states-demo'
s3 = boto3.resource('s3')
s3.meta.client.upload_file('./terraform/terraform.tfstate',bucketName, 'permissionsets/terraform.tfstate')
