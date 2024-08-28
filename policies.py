import json

def lambda_handler(event, context):
    data_policy = """
    We are committed to protecting your privacy. We collect and use your personal data only to provide and improve our services.
    Your data is stored securely and only accessible to authorized personnel.
    We do not share your information with third parties without your consent, except as required by law.
    You have the right to access, correct, and delete your data at any time. For more details, please review our Privacy Policy.
    """
    
    response = event['response']

    if response.lower() == "yes":
        statuscode = 200
        body = 'User accepted the data policy. The user can continue with te application.'
    else:
        statuscode = 400
        body = 'User rejected the data policy. The user cannnot continue with te application.'
        
    return {
        'statusCode': statuscode,
        'body': json.dumps(body)
        }