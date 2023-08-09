import json

def lambda_handler(event, context):
    print("triggered")
    try:
        num1 = float(event['queryStringParameters']['num1'])
        num2 = float(event['queryStringParameters']['num2'])
        operation = event['queryStringParameters']['operation']
        print("values recieved: ", num1, num2,operation)
        if operation == 'add':
            print("inside add operation")
            result = num1 + num2
            print ("Result is: ", result)
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                return {
                    'statusCode': 400,
                    'body': json.dumps({'error': 'Cannot divide by zero'})
                }
            result = num1 / num2
        else:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Invalid operation'})
            }

        return {
            'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
            'statusCode': 200,
            'body': json.dumps({'result': result})
        }
    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': str(e)})
        }
