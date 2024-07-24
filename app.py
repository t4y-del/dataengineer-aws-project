import logging
from flask import Flask, render_template, redirect, url_for
from forms import DemandasForm
import boto3
from botocore.exceptions import NoCredentialsError
import uuid
import os
from flask_wtf.csrf import CSRFProtect

# Configuración de la aplicación Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
csrf = CSRFProtect(app)

# Inicialización del cliente DynamoDB
session = boto3.Session()
dynamodb = session.resource('dynamodb', region_name='us-east-2')

# Nombre de la tabla DynamoDB
TABLE_NAME = 'demandas'

# Configuración del logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def index():
    form = DemandasForm()
    return render_template('index.html', form=form)

@app.route('/submit', methods=['GET', 'POST'])
def submit_demand():
    logging.info('Acceso al endpoint de registro de demanda')
    form = DemandasForm()
    if form.validate_on_submit():
        # Genera un ID único para la demanda
        unique_id = str(uuid.uuid4())
        persona = form.persona.data
        nombre = form.nombre.data
        dni = form.dni.data
        ano_nacimiento = form.anio_nacimiento.data
        legajo = form.legajo.data

        # Intentar registrar la demanda en DynamoDB
        try:
            table = dynamodb.Table(TABLE_NAME)
            table.put_item(
                Item={
                    'id': unique_id,
                    'titulo': persona,
                    'nombre': nombre,
                    'dni': dni,
                    'ano_nacimiento': ano_nacimiento,
                    'legajo': legajo
                }
            )
            logging.info('Demanda registrada exitosamente')
            return render_template('success.html')
        except Exception as error:
            logging.error(f'Error al registrar la demanda: {error}')
            return render_template('error.html')
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
