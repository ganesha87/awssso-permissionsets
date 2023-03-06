import boto3

s3 = boto3.resource('s3')
s3.meta.client.upload_file('../tf-assignments/terraform.tfstate','tf-states-demo', 'assignments/terraform.tfstate')
s3.meta.client.upload_file('../tf-assignments/terraform.tfstate','tf-states-demo', 'permissionsets/terraform.tfstate')