from flask import jsonify
from abstact.Port import Port


class Ticket_Machine(Port):
    def request_from_ID(self, ticketID):
        # Buscar el ticket por ID en la lista de tickets
        ticket_info = self.read_db('tickets', ticketID)
        
        # Verificar si se encontró el ticket
        if ticket_info is None:
            return jsonify(({'error': 'Ticket no encontrado'}), 404)
        
        return jsonify(ticket_info)

