from boto3.s3.connection import S3Connection
from boto3.s3.key import Key


conn = S3Connection('AKIAIOSFODNN7EXAMPLE','wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY')
bucket = conn.create_bucket('mybucket')
