
import datetime

class Client:
    def __init__(self, id, name, address1, address2, address3, city, state, zip_code, country, phone):
        self.id = id
        self.name = name
        self.address1 = address1
        self.address2 = address2
        self.address3 = address3
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.country = country
        self.phone = phone

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "address1": self.address1,
            "address2": self.address2,
            "address3": self.address3,
            "city": self.city,
            "state": self.state,
            "zip_code": self.zip_code,
            "country": self.country,
            "phone": self.phone
        }
    
    @classmethod
    def from_dict(cls, data):
        try:
            return cls(
                id=data["id"],
                name=data["name"],
                address1=data["address1"],
                address2=data["address2"],
                address3=data["address3"],
                city=data["city"],
                state=data["state"],
                zip_code=data["zip_code"],
                country=data["country"],
                phone=data["phone"]
            )
        except KeyError as e:
            print(f"Missing key in Client data: {e}")
            return None


class Airline:
    def __init__(self, id, company_name):
        self.id = id
        self.company_name = company_name

    def to_dict(self):
        return {
            "id": self.id,
            "company_name": self.company_name
        }
    
    @classmethod
    def from_dict(cls, data):
        try:
            return cls(
                id=data["id"],
                company_name=data["company_name"]
            )
        except KeyError as e:
            print(f"Missing key in Airline data: {e}")
            return None


class Flight:
    def __init__(self, id, client_id, airline_id, date, start_city, end_city):
        self.id = id
        self.client_id = client_id
        self.airline_id = airline_id
        self.date = date
        self.start_city = start_city
        self.end_city = end_city

    def to_dict(self):
        return {
            "id": self.id,
            "client_id": self.client_id,
            "airline_id": self.airline_id,
            "date": self.date,
            "start_city": self.start_city,
            "end_city": self.end_city
        }
    
    @classmethod
    def from_dict(cls, data):
        try:
            return cls(
                id=data["id"],
                client_id=data["client_id"],
                airline_id=data["airline_id"],
                date=data["date"],
                start_city=data["start_city"],
                end_city=data["end_city"]
            )
        except KeyError as e:
            print(f"Missing key in Flight data: {e}")
            return None