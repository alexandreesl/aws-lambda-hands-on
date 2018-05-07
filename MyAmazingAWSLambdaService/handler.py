# -*- coding: UTF-8 -*-

import json

from helpers.DynamoDbHelper import DynamoDbHelper
from helpers.ProductConverter import ProductConverter


def get_path_parameters(event, name):
    return event['pathParameters'][name]


dynamodb_helper = DynamoDbHelper(table='product')
product_converter = ProductConverter()


def save(event, context):
    product = product_converter.convert(event)

    if 'id' not in event['body']:
        return {
            "statusCode": 422,
            "body": json.dumps({'message': 'Product ID is required!'})
        }

    try:
        dynamodb_helper.save(product)
        response = {
            "statusCode": 200,
            "body": json.dumps({'message': 'saved successfully'})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({'message': str(e)})
        }

    return response


def get(event, context):
    product = dynamodb_helper.get(get_path_parameters(event, 'product_id'))

    if product is not None:
        response = {
            "statusCode": 200,
            "body": json.dumps(product)
        }
    else:
        response = {
            "statusCode": 404,
            "body": json.dumps({'message': 'not found'})
        }
    return response


def delete(event, context):
    try:
        dynamodb_helper.delete(get_path_parameters(event, 'product_id'))
        response = {
            "statusCode": 200,
            "body": json.dumps({'message': 'deleted successfully'})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({'message': str(e)})
        }

    return response
