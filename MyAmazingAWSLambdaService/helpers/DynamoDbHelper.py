# -*- coding: UTF-8 -*-

import boto3

dynamodb = boto3.resource('dynamodb')


class DynamoDbHelper:

    def __init__(self, **kwargs):
        self._table = dynamodb.Table(kwargs.get('table', """missing"""))

    def save(self, entity):
        """
        	save entity from DYNAMODB_self.table
        """
        saved = self._table.put_item(Item=entity)
        print('Saving result: ({})'.format(saved))

    def get(self, entity_id):
        """
			get entity from DYNAMODB_self.table
		"""
        entity = self._table.get_item(Key={'id': entity_id})

        if 'Item' in entity:
            return entity['Item']
        else:
            return None

    def delete(self, entity_id):
        """
        	delete entity from DYNAMODB_self.table
        """
        deleted = self._table.delete_item(Key={'id': entity_id})
        print('Deleting result: ({})'.format(deleted))
