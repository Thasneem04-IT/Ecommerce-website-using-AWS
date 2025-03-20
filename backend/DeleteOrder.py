import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Orders')

def lambda_handler(event, context):
    try:
        # Extract OrderID from pathParameters
        order_id = event.get("pathParameters", {}).get("OrderID")

        if not order_id:
            return {
                'statusCode': 400,
                'headers': {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
                'body': json.dumps({"error": "OrderID is required in the path"})
            }

        # Delete order from DynamoDB
        table.delete_item(Key={'OrderID': order_id})

        return {
            'statusCode': 200,
            'headers': {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
            'body': json.dumps({"message": "Order removed successfully"})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
            'body': json.dumps({"error": str(e)})
        }
