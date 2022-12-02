from django.test import TestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from main.models import Drone, Medication
from django.core.files.uploadedfile import SimpleUploadedFile

class DroneTests(APITestCase):
    def test_create_drone(self):
        """
        Ensure we can create a new drone.
        """
        # url = reverse('drones')
        data = {
            'serial_number':10000,
            'drone_model':'Lightweight',
            'weight_limit':500,
            'battery_capacity':60,
            'state': 'LOADING',
            'load': []

            }
        response = self.client.post('/api/drones/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Drone.objects.count(), 1)
        self.assertEqual(Drone.objects.get().serial_number, '10000')

    def test_not_create_drone_in_loading_state_if_battery_is_under_25percent(self):
        """
        Ensure that a drone with less than 25% of battery being in loading state
        """
        data = {
            'serial_number':10000,
            'drone_model':'Lightweight',
            'weight_limit':500,
            'battery_capacity':23,
            'state': 'LOADING',
            'load': []

            }

        response = self.client.post('/api/drones/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Drone.objects.count(), 0)
        
    def test_serial_number_must_by_under_100_charcacters_long(self):
        """
        Ensure that a drone with less than 25% of battery being in loading state
        """
        serial=''
        for i in range(1,102):
            serial+='1'
        data = {
            'serial_number':serial,
            'drone_model':'Lightweight',
            'weight_limit':500,
            'battery_capacity':65,
            'state': 'LOADING',
            'load': []

            }

        response = self.client.post('/api/drones/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Drone.objects.count(), 0)
    

    def test_serial_number_must_by_only_digits(self):
        """
        Ensure that a drone serial number is only digits
        """
       
        data = {
            'serial_number':'1aswa',
            'drone_model':'Lightweight',
            'weight_limit':500,
            'battery_capacity':65,
            'state': 'LOADING',
            'load': []

            }

        response = self.client.post('/api/drones/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Drone.objects.count(), 0)

    

    def test_drone_weight_limit_is_less_than_500(self):
        """
        Ensure that a drone serial number is only digits
        """
       
        data = {
            'serial_number':'10000',
            'drone_model':'Lightweight',
            'weight_limit':501,
            'battery_capacity':65,
            'state': 'LOADING',
            'load': []

            }

        response = self.client.post('/api/drones/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Drone.objects.count(), 0)

class MedicationTests(APITestCase):
    """
    Ensure the medication is created
    """
    def test_create_medication(self):
   
        data = {
            'name':'sjkskjs',
            # '@#$8jjjjhAA-_' ,
            'weight': 100,
            'code': 'AQSWAS998',
            'image':  None
            # SimpleUploadedFile(name='test.jpg',content= b"" ,content_type='image/jpeg') ,

        }
        response = self.client.post('/api/medication/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Medication.objects.count(), 1)




    """
     Ensure that medication name allow only letters, numbers, `-`, `_`
    """
    def test_name_medication_only_allowed_characters(self):
        data = {
            'name':'@#$8jjjjhAA-_' ,
            'weight': 100,
            'code': 'AQSWAS',
            'image':None ,

        }

        response = self.client.post('/api/medication/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Drone.objects.count(), 0)

    """
     Ensure that medication CODE allow only  uppercase letters, `_`, and numbers
    """
    def test_name_medication_only_allowed_characters(self):
        data = {
            'name':'8jjjjhAA-_' ,
            'weight': 100,
            'code': 'AaSWAS',
            'image':None ,

        }

        response = self.client.post('/api/medication/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Drone.objects.count(), 0)
