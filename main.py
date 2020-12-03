def lambda_handler(event, context):
    message = 'Olá {}!'.format(event['name'])  
    return { 
        'message' : message
    } 