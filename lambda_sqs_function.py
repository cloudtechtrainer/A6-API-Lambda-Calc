import json
import boto3

# Initialize SQS client
sqs = boto3.client('sqs')

# Replace with your SQS queue URL
RESULT_QUEUE_URL = "https://sqs.ap-south-1.amazonaws.com/277707115666/calcsqs"

def lambda_handler(event, context):
    print("Lambda triggered by SQS")
    try:
        # Iterate over SQS messages
        for record in event['Records']:
            # Parse the SQS message body
            body = json.loads(record['body'])
            num1 = float(body['num1'])
            num2 = float(body['num2'])
            operation = body['operation']
            print("Values received: ", num1, num2, operation)
            
            # Perform the requested operation
            if operation == 'add':
                result = num1 + num2
                print("Inside add operation. Result: ", result)
            elif operation == 'subtract':
                result = num1 - num2
                print("Inside subtract operation. Result: ", result)
            elif operation == 'multiply':
                result = num1 * num2
                print("Inside multiply operation. Result: ", result)
            elif operation == 'divide':
                if num2 == 0:
                    print("Error: Cannot divide by zero")
                    continue
                result = num1 / num2
                print("Inside divide operation. Result: ", result)
            else:
                print("Invalid operation received: ", operation)
                continue
            
            # Send the result to the result SQS queue
            message = {
                "operation": operation,
                "num1": num1,
                "num2": num2,
                "result": result
            }
            response = sqs.send_message(
                QueueUrl=RESULT_QUEUE_URL,
                MessageBody=json.dumps(message)
            )
            print(f"Result sent to SQS. Message ID: {response['MessageId']}")
        
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Messages processed successfully and results sent to SQS'})
        }
    except Exception as e:
        print("Error processing messages:", str(e))
        return {
            'statusCode': 400,
            'body': json.dumps({'error': str(e)})
        }
