from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

from django.test import TestCase

# Create your tests here.
from .models import BucketList

class ModelTestCase(TestCase):
    ''' test suite for BucketList class'''

    def setUp(self):
        self.bucketlist_name="Writign World Class Code"

        self.bucketlist = BucketList(name=self.bucketlist_name)

    def test_model_can_create_a_bucketlist(self):
        
        old_count = BucketList.objects.count()
        self.bucketlist.save()
        new_count = BucketList.objects.count()

        self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):
    ''' Test Suite for BucketList views '''

    def setUp(self):
        self.client = APIClient()
        self.bucketlist_data = {'name' : 'Goto Usa'}

        self.response = self.client.post(reverse('create'), self.bucketlist_data, format="json")    

    def test_api_can_create_a_bucket_list(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)