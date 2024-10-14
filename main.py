# main.py
import os
import requests
from dotenv import load_dotenv
import pandas as pd
import logging
from time import sleep

# Configurar logging
log_folder = 'logs'
os.makedirs(log_folder, exist_ok=True)
logging.basicConfig(
    filename=os.path.join(log_folder, 'send_messages.log'),
    level=logging.INFO,
    format='%(asctime)s %(levelname)s:%(message)s'
)

# Cargar variables de entorno
load_dotenv()

# Variables de configuración
API_URL = os.getenv('WHATSAPP_API_URL')
PHONE_NUMBER_ID = os.getenv('WHATSAPP_PHONE_NUMBER_ID')
ACCESS_TOKEN = os.getenv('WHATSAPP_ACCESS_TOKEN')
TEMPLATE_NAME = os.getenv('TEMPLATE_NAME')
LANGUAGE_CODE = os.getenv('LANGUAGE_CODE')
PHONE_COLUMN = os.getenv('PHONE_COLUMN')

# Encabezados para las solicitudes HTTP
HEADERS = {
    'Authorization': f'Bearer {ACCESS_TOKEN}',
    'Content-Type': 'application/json'
}

def load_contacts(csv_file):
    try:
        df = pd.read_csv(csv_file)
        logging.info(f"Loaded {len(df)} contacts from {csv_file}.")
        return df
    except Exception as e:
        logging.error(f"Error loading contacts: {e}")
        return None

def send_message(to, variables):
    url = f"{API_URL}/{PHONE_NUMBER_ID}/messages"
    
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "template",
        "template": {
            "name": TEMPLATE_NAME,
            "language": {
                "code": LANGUAGE_CODE
            }
        }
    }
    
    if variables:
        components = []
        for key, value in variables.items():
            components.append({
                "type": "body",
                "parameters": [
                    {"type": "text", "text": value}
                ]
            })
        payload["template"]["components"] = components
    
    try:
        response = requests.post(url, headers=HEADERS, json=payload)
        response.raise_for_status()
        logging.info(f"Message sent to {to}. Response: {response.json()}")
    except requests.exceptions.HTTPError as http_err:
        logging.error(f"HTTP error occurred for {to}: {http_err} - {response.text}")
    except Exception as err:
        logging.error(f"Other error occurred for {to}: {err}")

def main():
    contacts = load_contacts('data/contacts.csv')
    if contacts is None:
        logging.error("No contacts to process.")
        return
    
    # Identificar las columnas que contienen variables (excluir la columna del teléfono)
    variable_columns = [col for col in contacts.columns if col != PHONE_COLUMN]
    
    for index, row in contacts.iterrows():
        to = str(row[PHONE_COLUMN])
        
        if variable_columns:
            # Extraer variables dinámicas en orden
            variables = [str(row[col]) for col in variable_columns]  # Convertir a string por seguridad
        else:
            variables = []  # No hay variables
        
        send_message(to, variables)
        sleep(1)  # Pausa para evitar exceder los límites de la API

if __name__ == "__main__":
    main()
