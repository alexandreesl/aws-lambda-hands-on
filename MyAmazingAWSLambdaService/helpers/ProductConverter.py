# -*- coding: UTF-8 -*-
import json


class ProductConverter:

    def convert(self, event):
        """
           convert entity from input to dictionary to be saved on dynamodb
        """
        if isinstance(event['body'], dict):
            data = event['body']
        else:
            data = json.loads(event['body'])
        return {
            'id': data['id'],
            'name': data.get('name', ''),
            'description': data.get('description', ''),
            'price': data.get('price', '')
        }
