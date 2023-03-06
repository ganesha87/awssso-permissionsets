import boto3

s3 = boto3.resource('s3')
#s3://tf-states-demo/assignments/terraform.tfstate
s3.meta.client.download_file('tf-states-demo', 'assignments/terraform.tfstate', './config/assgn.tfstate')
s3.meta.client.download_file('tf-states-demo', 'permissionsets/terraform.tfstate', './config/psets.tfstate')