from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

from services.ticket.Ticket_Machine import Ticket_Machine
from services.route.Route_Service import Route_Service

ticket_machine = Ticket_Machine()
route_service = Route_Service()

# Servicio para obtener información de boleta
@app.route('/get-ticket-info', methods=['GET'])
def get_ticket_info():
    try:
        ticketID = request.args.get('ID')
        
        # Validar que el ID se haya proporcionado
        if not ticketID:
            return jsonify({'error': 'Se requiere el parámetro ID'}), 400
        
        # Buscar el ticket por ID en la lista de tickets
        ticket_info = ticket_machine.request_from_ID(ticketID)
        
        # Verificar si se encontró el ticket
        if ticket_info is None:
            return jsonify({'error': 'Ticket no encontrado'}), 404
        
        return ticket_info
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Servicio para obtener información de rutas
@app.route('/get-route-info', methods=['GET'])
def get_route_info():
    from_location = request.args.get('from')
    ticketID = request.args.get('ID')

    # Validar que el ID se haya proporcionado
    if not from_location or not ticketID:
        return jsonify({'error': 'Se requiere el parametro de ubicacion y ID'}), 400
    
    try:
        ticket_info = ticket_machine.request_from_ID(ticketID)
        if ticket_info is None:
            return jsonify({'error': 'Ticket no encontrado'}), 404
        to_location = ticket_info.json['zone']

        # Buscar la ruta entre los puntos
        route_key = f'{from_location}-{to_location}'
        route_info = route_service.request_from_ID(route_key)
        return route_info
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Servicio para obtener el estado de una zona
@app.route('/get-zone-status', methods=['GET'])
def get_zone_status():
    zone = request.args.get('zone')
    try:
        response = requests.get(f'http://localhost:5003/zone?zone={zone}')
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000)
