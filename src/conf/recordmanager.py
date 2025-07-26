import sys
sys.path('../conf')
import datetime
from typing import List, Union
import json
from conf.data_class import *



class RecordManager():

    def __init__(self):
        self.data = {
            "clients": [],
            "airlines": [],
            "flights": []
        }
        self.load_data()        
        
    def load_data(self, file:str):
        try:
            with open(file) as f:
                self.data = json.load(f)
        except FileNotFoundError:
            print(f"File {file} not found. Starting with empty data.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from {file}. Starting with empty data.")
        except Exception as e:
            print(f"Unexpected error loading data: {e}")

    def save_to_json_file(self, file:str):
        try:
            with open(file, 'w') as f:
                json.dump(self.data, f, indent=2)
        except Exception as e:
            print(f"Error saving data to {file}: {e}")

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
            return "airline Added!"
        except Exception as e:
            print(f"Error adding airline: {e}")
            return "Failed to add airline."

    def add_flight(self, flight_data):
        try:
            flight = Flight(**flight_data)
            self.data["flights"].append(flight.to_dict())
            self.save_to_json_file()
            return "flight Added!"
        except Exception as e:
            print(f"Error adding flight: {e}")
            return "Failed to add flight."

    def update_client(self, id:int, **updates) ->bool:
        try:
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
            self.data["clients"] = [client for client in self.data["clients"] if client.get("id") != client_id]
            self.save_to_json_file()
            return True
        except Exception as e:
            print(f"Error deleting client: {e}")
            return False

    def delete_airline(self, airline_id):
        try:
            self.data["airlines"] = [airline for airline in self.data["airlines"] if airline.get("id") != airline_id]
            self.save_to_json_file()
            return True
        except Exception as e:
            print(f"Error deleting airline: {e}")
            return False

    def delete_flight(self, flight_id):
        try:
            self.data["flights"] = [flight for flight in self.data["flights"] if flight.get("id") != flight_id]
            self.save_to_json_file()
            return True
        except Exception as e:
            print(f"Error deleting flight: {e}")
            return False