import boto3
import json
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Products')

# Function to convert Decimal to float
def decimal_converter(obj):
    if isinstance(obj, Decimal):
        return float(obj)  # or str(obj) if you prefer
    raise TypeError

def lambda_handler(event, context):
    response = table.scan()  # Fetch all products
    
    return {
        'statusCode': 200,
        'headers': {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"  # Enables CORS
        },
        'body': json.dumps(response['Items'], default=decimal_converter)
    }
