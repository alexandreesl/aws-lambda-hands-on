# -*- coding: UTF-8 -*-


class ProductConverter:

    def convert(self, event):
        """
           convert entity from input to dictionary to be saved on dynamodb
        """
        return {
            'id': event['body']['id'],
            'name': event['body'].get('name', default=''),
            'description': event['body'].get('description', default=''),
            'price': event['body'].get('price', default='')
        }
