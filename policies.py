import json

def lambda_handler(event, context):
    greeting = 'Hola'
    encryption = greeting.lower().replace('e','3')
    return {
        'statusCode': 200,
        'body': json.dumps(encryption)
    }
