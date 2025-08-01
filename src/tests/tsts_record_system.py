import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from conf.recordmanager import RecordManager
import pytest

class TestRecordSystem:
    def setup_method(self):
        """Setup method to initialize the RecordManager before each test."""
        self.manager = RecordManager()

    TEST_CLIENT_DATA = {
        "id": 1001,
        "name": "John O'Connor",
        "address1": "15 St. Patrick's Rd",
        "address2": "",
        "address3": "",
        "city": "Dublin",
        "state": "DN",
        "zip_code": "D02 X285",
        "country": "Ireland",
        "phone": "+353-1-555-2468"
    }

    TEST_UPDATED_CLIENT_DATA = {
        "id": 1001,
        "name": "John O'Connor",
        "address1": "15 St. Patrick's Rd",
        "address2": "",
        "address3": "",
        "city": "Dublin",
        "state": "DN",
        "zip_code": "D02 X285",
        "country": "Ireland",
        "phone": "+44-70-6245-4673"
    }

    TEST_AIRLINE_DATA = {
        "id": 2001,
        "company_name": "Air Ireland"
    }

    TEST_UPDATED_AIRLINE_DATA = {
        "id": 2001,
        "company_name": "Singapore Airlines"
    }

    TEST_FLIGHT_DATA = {
        "id": 5110,
        "client_id": 1111,
        "airline_id": 8,
        "date": "2025-08-19",
        "start_city": "Dublin",
        "end_city": "Amsterdam",
    }

    TEST_SEARCH_FLIGHT_DATA = {
        "id": 5110,
        "client_id": 1111,
        "airline_id": 8,
        "date": "2025-08-19",
        "start_city": "Rio de Janeiro",
        "end_city": "Bangkok",
    }

    def test_add_client(self):
        """Test adding a client record."""
        previous_count = len(self.manager.data["clients"])
        result = self.manager.add_client(self.TEST_CLIENT_DATA)
        assert result == "Client Added!"
        assert len(self.manager.data["clients"]) > previous_count
        result = self.manager.search_client(self.TEST_CLIENT_DATA["id"])
        assert result["name"] == self.TEST_CLIENT_DATA["name"] and result["phone"] == self.TEST_CLIENT_DATA["phone"]

    def test_add_airline(self):
        """Test adding an airline record."""
        previous_count = len(self.manager.data["airlines"])
        result = self.manager.add_airline(self.TEST_AIRLINE_DATA)
        assert result == "Airline Added!"
        assert len(self.manager.data["airlines"]) > previous_count
        result = self.manager.search_airline(self.TEST_AIRLINE_DATA["id"])
        assert result["company_name"] == self.TEST_AIRLINE_DATA["company_name"]

    def test_add_flight(self):
        """Test adding a flight record."""
        previous_count = len(self.manager.data["flights"])
        result = self.manager.add_flight(self.TEST_FLIGHT_DATA)
        assert result == "Flight Added!"
        assert len(self.manager.data["flights"]) > previous_count
        result = self.manager.search_flight(self.TEST_FLIGHT_DATA["id"])
        assert result["client_id"] == self.TEST_FLIGHT_DATA["client_id"] and result["end_city"] == self.TEST_FLIGHT_DATA["end_city"]

    def test_search_client(self):
        """Test searching for a client record."""
        self.manager.add_client(self.TEST_CLIENT_DATA)
        result = self.manager.search_client(self.TEST_CLIENT_DATA["id"])
        assert result is not None
        assert result["name"] == self.TEST_CLIENT_DATA["name"]

    def test_search_airline(self):
        """Test searching for an airline record."""
        self.manager.add_airline(self.TEST_AIRLINE_DATA)
        result = self.manager.search_airline(self.TEST_AIRLINE_DATA["id"])
        assert result is not None
        assert result["company_name"] == self.TEST_AIRLINE_DATA["company_name"]

    def test_search_flight(self):
        """Test searching for a flight record."""
        self.manager.add_flight(self.TEST_SEARCH_FLIGHT_DATA)
        result = self.manager.search_flight(self.TEST_SEARCH_FLIGHT_DATA["id"])
        assert result is not None
        assert result["client_id"] == self.TEST_SEARCH_FLIGHT_DATA["client_id"] and result["end_city"] == self.TEST_SEARCH_FLIGHT_DATA["end_city"]

    def test_update_client(self):
        """Test updating a client record."""
        # Ensure the client exists before updating
        self.manager.add_client(self.TEST_CLIENT_DATA)
        self.manager.update_client(self.TEST_UPDATED_CLIENT_DATA["id"], **{k: v for k, v in self.TEST_UPDATED_CLIENT_DATA.items() if k != "id"})
        result = self.manager.search_client(self.TEST_UPDATED_CLIENT_DATA["id"])
        assert result["name"] == self.TEST_UPDATED_CLIENT_DATA["name"] and result["phone"] == self.TEST_UPDATED_CLIENT_DATA["phone"]
        assert result["address1"] == self.TEST_UPDATED_CLIENT_DATA["address1"]

    def test_update_flight(self):
        """Test updating a flight record."""
        # Ensure the flight exists before updating
        self.manager.add_flight(self.TEST_FLIGHT_DATA)
        self.manager.update_flight(self.TEST_SEARCH_FLIGHT_DATA["id"], **{k: v for k, v in self.TEST_SEARCH_FLIGHT_DATA.items() if k != "id"})
        result = self.manager.search_flight(self.TEST_SEARCH_FLIGHT_DATA["id"])
        assert result["client_id"] == self.TEST_SEARCH_FLIGHT_DATA["client_id"] and result["end_city"] == self.TEST_SEARCH_FLIGHT_DATA["end_city"]

    def test_update_airline(self):
        """Test updating an airline record.""" 
        # Ensure the airline exists before updating
        self.manager.add_airline(self.TEST_AIRLINE_DATA)
        self.manager.update_airline(self.TEST_UPDATED_AIRLINE_DATA["id"], **{k: v for k, v in self.TEST_UPDATED_AIRLINE_DATA.items() if k != "id"})
        result = self.manager.search_airline(self.TEST_UPDATED_AIRLINE_DATA["id"])
        assert result["company_name"] == self.TEST_UPDATED_AIRLINE_DATA["company_name"]


    def test_delete_flight(self):
        """Test deleting a flight record."""
        self.manager.add_flight(self.TEST_SEARCH_FLIGHT_DATA)
        self.manager.delete_flight(self.TEST_SEARCH_FLIGHT_DATA["id"])
        result = self.manager.search_flight(self.TEST_SEARCH_FLIGHT_DATA["id"])
        assert result is False
    
    def test_delete_airline(self):
        """Test deleting an airline record."""
        self.manager.add_airline(self.TEST_AIRLINE_DATA)
        self.manager.delete_airline(self.TEST_AIRLINE_DATA["id"])
        result = self.manager.search_airline(self.TEST_AIRLINE_DATA["id"])
        assert result is False

    def test_delete_client(self):
        """Test deleting a client record."""
        self.manager.add_client(self.TEST_CLIENT_DATA)
        self.manager.delete_client(self.TEST_CLIENT_DATA["id"])
        result = self.manager.search_client(self.TEST_CLIENT_DATA["id"])
        assert result is False

    def teardown_method(self):
        """Teardown method to clean up after each test."""
        self.manager.data = {
            "clients": [],
            "airlines": [],
            "flights": []
        }
        self.manager.save_to_json_file()

if __name__ == "__main__":
    # Run the tests
    pytest.main(["-s", "-v", __file__])

    # If you want to run the tests directly without pytest, uncomment:
    '''test_system = TestRecordSystem()
    test_system.setup_method()
    test_system.test_add_client()
    test_system.test_add_airline()
    test_system.test_add_flight()
    test_system.test_update_client()
    test_system.test_delete_client()
    test_system.test_search_client()
    test_system.test_search_airline()
    test_system.test_search_flight()
    test_system.teardown_method()'''
        