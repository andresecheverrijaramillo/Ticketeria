from flask import jsonify
from abstact.Port import Port


class Route_Service(Port):
    def request_from_ID(self, route_id):
        route_info = self.read_db('routes', route_id)

        # Verificar si se encontró el ticket
        if route_info is None:
            return jsonify(({'error': 'Ticket no encontrado'}), 404)
        
        return jsonify({'route': route_id, 'route': route_info})
        




