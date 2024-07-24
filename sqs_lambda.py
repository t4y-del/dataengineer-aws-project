import json
import boto3
import logging
from datetime import datetime

# Configuración del logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3_client = boto3.client('s3')

def convert_dynamo_to_dict(dynamo_item):
    """
    Convertir datos del formato DynamoDB a un diccionario estándar.
    """
    result = {}
    for key, value in dynamo_item.items():
        if 'S' in value:
            result[key] = value['S']
        elif 'N' in value:
            result[key] = int(value['N'])
    return result

def lambda_handler(event, context):
    """
    Manejar el evento de SQS, transformar los datos de DynamoDB y almacenarlos en S3.
    """
    for record in event.get('Records', []):
        try:
            # Procesar el cuerpo del mensaje SQS
            message_body = json.loads(record.get('body', '{}'))
            
            # Extraer los datos de DynamoDB
            dynamodb_event = message_body.get('dynamodb', {})
            new_image = dynamodb_event.get('NewImage', {})
            
            # Convertir los datos de DynamoDB a un formato estándar
            converted_data = convert_dynamo_to_dict(new_image)
            
            # Crear el nombre del archivo para S3
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            file_name = f"demandas_{converted_data.get('id', 'unknown')}_{timestamp}.json"
            
            # Subir el archivo a S3
            s3_client.put_object(
                Bucket='project-demandas-raw-argentina',
                Key=file_name,
                Body=json.dumps(converted_data),
                ContentType='application/json'
            )
            
            logger.info(f"Archivo guardado en S3: {file_name}")
        except Exception as e:
            logger.error(f"Error al procesar el mensaje: {e}")
        
    return {
        'statusCode': 200,
        'body': json.dumps('Datos transformados y almacenados en S3')
    }
