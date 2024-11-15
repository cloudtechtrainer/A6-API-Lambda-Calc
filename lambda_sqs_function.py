import json

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
            
            # Log the successful processing
            print(f"Processed result: {result}")
        
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Messages processed successfully'})
        }
    except Exception as e:
        print("Error processing messages:", str(e))
        return {
            'statusCode': 400,
            'body': json.dumps({'error': str(e)})
        }
