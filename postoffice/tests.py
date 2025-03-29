import decimal
import random
from django.test import TestCase

from postoffice.models import Letters, Parcels


class LetterTestCase(TestCase):
    def setUp(self):
        LETTER_TYPES = [ 10, 20, 30, 40]

        for i in range(1, 51):
            i = Letters.objects.create(
                sender=f'Sender_{i}',
                recipient=f'recipient_{i}',
                dispatch_point=f'dispatch_point_{i}',
                receive_point=f'receive_point_{i}',
                dispatch_postal_code=(str(i)*3),
                receive_postal_code=(str(i+1)*3),
                letter_type=random.choice(LETTER_TYPES),
                letter_weight=round(random.uniform(0, 2), 2)
            )
            self.i = i
        
        self.letters_qs = Letters.objects.all()

    def test_letters_count(self):
        letter_count = self.letters_qs.count()
        self.assertEqual(letter_count, 50)
    
    def test_letter_detail(self):
        test_letter = Letters.objects.get(recipient='recipient_17')
        self.assertEqual(test_letter.dispatch_postal_code, 171717)
        self.assertEqual(test_letter.receive_postal_code, 181818)

    def test_valid_letter_weight(self):
        test_letter = Letters.objects.get(id=random.randint(1, 51))
        self.assertEqual(test_letter.letter_weight.__class__, decimal.Decimal)

    def test_not_zero_receive_postal_code(self):
        for letter in self.letters_qs:
            self.assertLessEqual(0, letter.receive_postal_code)

    
class ParcelTestCase(TestCase):
    def setUp(self):
        PARCEL_TYPES = [ 10, 20, 30, 40]

        for i in range(1, 21):
            i = Parcels.objects.create(
                sender=f'Sender_{i}',
                recipient=f'recipient_{i}',
                dispatch_point=f'dispatch_point_{i}',
                receive_point=f'receive_point_{i}',
                dispatch_postal_code=(str(i)*3),
                receive_postal_code=(str(i+1)*3),
                phone_number=str(random.randint(10000000, 99999999)),
                parcel_type=random.choice(PARCEL_TYPES),
                payment_amount=round(random.uniform(0, 1000), 2)
            )
            self.i = i
        
        self.parcel_qs = Parcels.objects.all()

    def test_parcel_count(self):
        parcel_count = self.parcel_qs.count()
        self.assertEqual(parcel_count, 20)
    
    def test_parcel_detail(self):
        test_parcel = Parcels.objects.get(recipient='recipient_20')
        self.assertEqual(test_parcel.dispatch_postal_code, 202020)
        self.assertEqual(test_parcel.receive_postal_code, 212121)

    def test_valid_payment_amount(self):
        test_parcel = Parcels.objects.get(id=random.randint(1, 21))
        self.assertEqual(test_parcel.payment_amount.__class__, decimal.Decimal)
    
    def test_valid_phone_number(self):
        phone_number = Parcels.objects.get(id=1).phone_number
        self.assertTrue(phone_number)
        self.assertEqual(phone_number.__class__, str)