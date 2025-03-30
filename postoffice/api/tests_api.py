from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from postoffice.api.serializers import LetterSerializer
from postoffice.models import Letters


class PostofficeTests(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.url = 'http://127.0.0.1:8000/api/letters/'

        for i in range(5):
            Letters.objects.create(
                sender=f'sender_{i}',
                recipient=f'recipient_{i}',
                dispatch_point=f'dispatch_point_{i}',
                receive_point=f'receive_point_{i}',
                dispatch_postal_code=i*6,
                receive_postal_code=(i+1)*6,
                letter_type=i*10,
                letter_weight=i*1.10)

    def test_create_letter(self):
        """ Ensure we can create a new Letter object """

        response = self.client.get(self.url)
        serializer = LetterSerializer(Letters.objects.all(), many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'], serializer.data)

    def test_get_invalid_letter(self):
        response = self.client.get(self.url+'/1001')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
