import boto3
from botocore.exceptions import ClientError

class DynamoDBService:
    def __init__(self):
        dynamodb = boto3.resource('dynamodb')
        self.products_table = dynamodb.Table('Products')

    def get_products(self):
        response = self.products_table.scan()
        return response.get('Items', [])

    def get_product(self, product_id: str):
        response = self.products_table.get_item(Key={'ProductId': product_id})
        return response.get('Item')

    def create_product(self, product: dict):
        try:
            response = self.products_table.put_item(Item=product)
            return response
        except ClientError as e:
            print("Error inserting item:", e)
            return {"Error": str(e)}

    def update_product(self, product_id: str, updates: dict):
        update_expression = 'SET ' + ', '.join(f'{k}=:{k}' for k in updates.keys())
        expression_attribute_values = {f':{k}': v for k, v in updates.items()}
        self.products_table.update_item(
            Key={'ProductId': product_id},
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_attribute_values
        )

    def delete_product(self, product_id: str):
        self.products_table.delete_item(Key={'ProductId': product_id})

    def get_inventory(self):
        response = self.products_table.scan(AttributesToGet=['ProductId', 'ProductName', 'StockLevel'])
        return response.get('Items', [])

    def get_inventory_item(self, product_id: str):
        response = self.products_table.get_item(
            Key={'ProductId': product_id},
            AttributesToGet=['ProductId', 'ProductName', 'StockLevel']
        )
        return response.get('Item')

    def create_order(self, product_id: str, quantity: int):
        product = self.get_product(product_id)
        if not product or product['StockLevel'] < quantity:
            return None

        new_stock_level = product['StockLevel'] - quantity
        self.update_product(product_id, {'StockLevel': new_stock_level})
        return {'ProductId': product_id, 'Quantity': quantity}
