from rest_framework import status
from rest_framework.test import APITestCase


class MainTestCase(APITestCase):

    def test_urls_available(self):
        available_urls = [
            "api/country",
            "api/shipment"
        ]
        response = self.client.get("/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = response.json().keys()
        for url in available_urls:
            self.assertTrue(url in response)


class CreateCountryTestCase(APITestCase):

    def test_country_create(self):
        country_name = "test_country_name"
        response = self.client.post("/api/country/", {"name": country_name})
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual({"id": 1, "name": country_name}, response.json())


class UpdateCountryTestCase(APITestCase):
    country_id = None
    country_name = None

    def setUp(self, country_name="test_country_name"):
        response = self.client.post("/api/country/", {"name": country_name})
        response = response.json()
        self.country_id, self.country_name = response['id'], response['name']

    def test_country_get_one(self):
        response = self.client.get("/api/country/1/")
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual({"id": self.country_id, "name": self.country_name}, response.json())

    def test_country_get_list(self):
        self.setUp()
        response = self.client.get("/api/country/")
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(2, len(response.json()))

    def test_country_put(self):
        data = {'name': 'new_name'}
        response = self.client.put(f"/api/country/{self.country_id}/", data=data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        data['id'] = 1
        self.assertEqual(data, response.json())

    def test_country_patch(self):
        data = {'name': 'new_name'}
        response = self.client.patch(f"/api/country/{self.country_id}/", data=data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        data['id'] = 1
        self.assertEqual(data, response.json())

    def test_country_delete(self):
        response = self.client.delete(f"/api/country/{self.country_id}/")
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)


class CreateShipmentTestCase(APITestCase):
    country_to_id = None
    country_from_id = None

    def create_country(self, name):
        response = self.client.post("/api/country/", {"name": name})
        return response.json().get('id', -1)

    def setUp(self):
        self.country_to_id = self.create_country(name="test_company_from")
        self.country_from_id = self.create_country(name="test_company_to")

    def test_shipment_create(self):
        data = {
            "date_of_departure": "2022-03-22",
            "date_of_arrival": "2022-03-25",
            "country_to": self.country_to_id,
            "country_from": self.country_from_id
        }
        response = self.client.post(f"/api/shipment/", data=data)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        data['id'] = 1
        self.assertEqual(data, response.json())


class UpdateShipmentTestCase(APITestCase):
    country_to_id = None
    country_from_id = None

    def create_country(self, name):
        response = self.client.post("/api/country/", {"name": name})
        return response.json().get('id', -1)

    def setUp(self):
        self.country_from_id = self.create_country(name="test_company_from")
        self.country_to_id = self.create_country(name="test_company_to")
        data = {
            "date_of_departure": "2022-03-22",
            "date_of_arrival": "2022-03-25",
            "country_to": self.country_to_id,
            "country_from": self.country_from_id
        }
        response = self.client.post(f"/api/shipment/", data=data)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

    def test_shipment_get_one(self):
        response = self.client.get(f"/api/shipment/1/")
        data = {
            "id": 1,
            "date_of_departure": "2022-03-22",
            "date_of_arrival": "2022-03-25",
            "country_to": self.country_to_id,
            "country_from": self.country_from_id
        }
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(data, response.json())

    def test_shipment_get_list(self):
        self.setUp()
        response = self.client.get(f"/api/shipment/")
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(2, len(response.json()))

    def test_shipment_put(self):
        data = {
            "date_of_departure": "2050-03-22",
            "date_of_arrival": "2050-03-25",
            "country_to": self.country_from_id,
            "country_from": self.country_to_id
        }
        response = self.client.put(f"/api/shipment/1/", data=data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        data['id'] = 1
        self.assertEqual(data, response.json())

    def test_shipment_patch(self):
        data = {
            "date_of_departure": "2010-03-22"
        }
        response = self.client.patch(f"/api/shipment/1/", data=data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_shipment_delete(self):
        response = self.client.delete(f"/api/shipment/1/")
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
