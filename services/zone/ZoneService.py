import json
import os  
from flask import Flask, jsonify, request

app = Flask(__name__)

# Obtener la ruta absoluta del archivo JSON
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(BASE_DIR, 'database.json')


# Servicio que devuelve qué tan llena está una zona
@app.route('/zone', methods=['GET'])
def get_zone_status():
    # Cargar el archivo JSON
    with open(json_path) as f:
        data = json.load(f)
    zone = request.args.get('zone')

    zone_data = data['zones'].get(zone)

    if (zone_data):
        empty = zone_data['capacity'] - zone_data['occupied']
        status = {'Asientos Vacios': empty}
    else:
        status = data['zones'].get(zone, {'status': 'Zona no encontrada'})

    return jsonify({'zone': zone, 'status': status})

if __name__ == '__main__':
    app.run(port=5003)