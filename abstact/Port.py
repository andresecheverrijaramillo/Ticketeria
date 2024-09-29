# domain/ports/ticket_repository.py
from abc import ABC, abstractmethod
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(BASE_DIR, '../database.json')

class Port:
    @abstractmethod
    def request_from_ID(self, user_id, event_id):
        pass
    
    def read_db(self, parameter, id):
        # Cargar el archivo JSON
        with open(json_path) as f:
            data = json.load(f)
        
        return data[parameter].get(id, None)
