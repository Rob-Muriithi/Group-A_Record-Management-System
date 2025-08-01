import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import datetime
from typing import List, Union
import json
from conf.data_class import *



class RecordManager():

    def __init__(self, file='src/record/record.jsonl'):
        self.file = file
        self.data = {
            "clients": [],
            "airlines": [],
            "flights": []
        }
        self.load_data()        
        
    def load_data(self):
        try:
            with open(self.file) as f:
                self.data = json.load(f)
        except FileNotFoundError:
            print(f"File {self.file} not found. Starting with empty data.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from {self.file}. Starting with empty data.")
        except Exception as e:
            print(f"Unexpected error loading data: {e}")

    def save_to_json_file(self):
        try:
            with open(self.file, 'w') as f:
                json.dump(self.data, f, indent=2)
        except Exception as e:
            print(f"Error saving data to {self.file}: {e}")

    def add_client(self, client_data):
        try:
            client = Client(**client_data)
            self.data["clients"].append(client.to_dict())
            self.save_to_json_file()
            return "Client Added!"
        except Exception as e:
            print(f"Error adding client: {e}")
            return "Failed to add client."

    def add_airline(self, airline_data):
        try:
            airline = Airline(**airline_data)
            self.data["airlines"].append(airline.to_dict())
            self.save_to_json_file()
            return "Airline Added!"
        except Exception as e:
            print(f"Error adding airline: {e}")
            return "Failed to add airline."

    def add_flight(self, flight_data):
        try:
            flight = Flight(**flight_data)
            self.data["flights"].append(flight.to_dict())
            self.save_to_json_file()
            return "Flight Added!"
        except Exception as e:
            print(f"Error adding flight: {e}")
            return "Failed to add flight."

    def update_client(self, id:int, **updates) ->bool:
        try:
            id_present = any(client.get("id") == id for client in self.data["clients"])
            if not id_present:
                print(f"Client with ID {id} not found.")
                return False
            for client in self.data["clients"]:
                if client.get("ID", client.get("id")) == id:
                    for k, v in updates.items():
                        if k in client:
                            client[k] = v
                    self.save_to_json_file()
                    return True
            return False
        except Exception as e:
            print(f"Error updating client: {e}")
            return False

    def update_airline(self, id:int, **updates) ->bool:
        try:
            id_present = any(airline.get("id") == id for airline in self.data["airlines"])
            if not id_present:
                print(f"Airline with ID {id} not found.")
                return False
            for airline in self.data["airlines"]:
                if airline.get("ID", airline.get("id")) == id:
                    for k, v in updates.items():
                        if k in airline:
                            airline[k] = v
                    self.save_to_json_file()
                    return True
            return False
        except Exception as e:
            print(f"Error updating airline: {e}")
            return False

    def update_flight(self, id:int, **updates) ->bool:
        try:
            id_present = any(flight.get("id") == id for flight in self.data["flights"])
            if not id_present:
                print(f"Flight with ID {id} not found.")
                return False
            for flight in self.data["flights"]:
                if flight.get("ID", flight.get("id")) == id:
                    for k, v in updates.items():
                        if k in flight:
                            flight[k] = v
                    self.save_to_json_file()
                    return True
            return False
        except Exception as e:
            print(f"Error updating flight: {e}")
            return False

    def delete_client(self, client_id):
        try:
            id_present = any(client.get("id") == client_id for client in self.data["clients"])
            if not id_present:
                print(f"Client with ID {client_id} not found.")
                return False
            self.data["clients"] = [client for client in self.data["clients"] if client.get("id") != client_id]
            self.save_to_json_file()
            return True
        except Exception as e:
            print(f"Error deleting client: {e}")
            return False

    def delete_airline(self, airline_id):
        try:
            id_present = any(airline.get("id") == airline_id for airline in self.data["airlines"])
            if not id_present:
                print(f"Airline with ID {airline_id} not found.")
                return False
            self.data["airlines"] = [airline for airline in self.data["airlines"] if airline.get("id") != airline_id]
            self.save_to_json_file()
            return True
        except Exception as e:
            print(f"Error deleting airline: {e}")
            return False

    def delete_flight(self, flight_id):
        try:
            id_present = any(flight.get("id") == flight_id for flight in self.data["flights"])
            if not id_present:
                print(f"Flight with ID {flight_id} not found.")
                return False
            self.data["flights"] = [flight for flight in self.data["flights"] if flight.get("id") != flight_id]
            self.save_to_json_file()
            return True
        except Exception as e:
            print(f"Error deleting flight: {e}")
            return False
        
    def search_client(self, client_id):
        try:
            id_present = any(client.get("id") == client_id for client in self.data["clients"])
            if not id_present:
                print(f"Client record with ID {client_id} not found.")
                return False
            for client in self.data["clients"]:
                if client.get("id") == client_id:
                    return client
            return None
        except Exception as e:
            print(f"Error searching for client: {e}")
            return None
        
    def search_airline(self, airline_id):
        try:
            id_present = any(airline.get("id") == airline_id for airline in self.data["airlines"])
            if not id_present:
                print(f"Airline record with ID {airline_id} not found.")
                return False
            for airline in self.data["airlines"]:
                if airline.get("id") == airline_id:
                    return airline
            return None
        except Exception as e:
            print(f"Error searching for airline: {e}")
            return None
        
    def search_flight(self, flight_id):
        try:
            id_present = any(flight.get("id") == flight_id for flight in self.data["flights"])
            if not id_present:
                print(f"Flight record with ID {flight_id} not found.")
                return False
            for flight in self.data["flights"]:
                if flight.get("id") == flight_id:
                    return flight
            return None
        except Exception as e:
            print(f"Error searching for flight: {e}")
            return None
        
    def search_record(self, record_type: str, record_id: int) -> Union[Client, Airline, Flight, None]:
        try:
            if record_type == "clients":
                return self.search_client(record_id)
            elif record_type == "airlines":
                return self.search_airline(record_id)
            elif record_type == "flights":
                return self.search_flight(record_id)
            else:
                print(f"Unknown record type: {record_type}")
                return None
        except Exception as e:
            print(f"Error searching for record: {e}")
            return None
    