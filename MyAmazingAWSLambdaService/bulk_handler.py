# -*- coding: UTF-8 -*-

import boto3
import pandas as pd

from helpers.DynamoDbHelper import DynamoDbHelper

client = boto3.client('s3')
dynamodb_helper = DynamoDbHelper(table='product')


def bulk_insert(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        obj = client.get_object(Bucket=bucket, Key=key)
        products = pd.read_csv(obj['Body'])
        products_records = products.fillna('').to_dict('records')
        for product in products_records:
            record = {
                'id': product['id'],
                'name': product.get('name', ''),
                'description': product.get('description', ''),
                'price': product.get('price', '')
            }
            dynamodb_helper.save(record)
