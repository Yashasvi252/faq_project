from django.test import TestCase
from .models import FAQ

class FAQTestCase(TestCase):
    def setUp(self):
        FAQ.objects.create(question="What is Django?", answer="A Python framework.")

    def test_translation(self):
        faq = FAQ.objects.get(question="What is Django?")
        self.assertIsNotNone(faq.question_hi)
        self.assertIsNotNone(faq.question_bn)
