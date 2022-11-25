import os
import urllib.parse
import boto3

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')

    settings = make_settings(bucket, key)
    user_metadata = {
        'JobCreatedBy': 'videoConvertSample',
    }

    client = boto3.client('mediaconvert', endpoint_url = '<your-endpoint-url>')
    result = client.create_job(
        Role = '<role-arn>',
        JobTemplate = '<Template-name>',
        Settings=settings,
        UserMetadata=user_metadata,
    )

def make_settings(bucket, key):
    basename = os.path.basename(key).split('.')[0]

    return \
    {
        "Inputs": [
            {
               "FileInput": f"s3://{bucket}/{key}",
            }
        ],
        
    }
