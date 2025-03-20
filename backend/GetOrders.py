import boto3
import json
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Orders')

# Function to convert Decimal to float
def decimal_to_float(obj):
    if isinstance(obj, Decimal):
        return float(obj)  # Convert Decimal to float
    raise TypeError("Object of type %s is not JSON serializable" % type(obj).__name__)

def lambda_handler(event, context):
    try:
        response = table.scan()  # Fetch all orders
        
        return {
            'statusCode': 200,
            'headers': {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
            'body': json.dumps(response['Items'], default=decimal_to_float)  # Convert Decimals
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
            'body': json.dumps({"error": str(e)})
        }
