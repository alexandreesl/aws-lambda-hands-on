# -*- coding: UTF-8 -*-
import json


class ProductConverter:

    def convert(self, event):
        """
           convert entity from input to dictionary to be saved on dynamodb
        """
        data = json.loads(event['body'])
        return {
            'id': data['id'],
            'name': data.get('name', default=''),
            'description': data.get('description', default=''),
            'price': data.get('price', default='')
        }
