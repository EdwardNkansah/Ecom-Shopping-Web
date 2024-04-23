from django.test import TestCase
from .models import Product
from django.contrib.auth.models import User


class ProductModelTestCase(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name='Test Product',
            rating=4.5,
            prices=9.99,
            memory='8GB',
            camera='12MP',
            display='5.5"',
            battery='3000mAh',
            processor='Quad-core',
            warranty='1 year',
            digital=True
        )

    def test_product_str(self):
        self.assertEqual(str(self.product), 'Test Product')

