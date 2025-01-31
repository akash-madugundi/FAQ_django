from django.test import TestCase
from django.urls import reverse

class FaqsViewTest(TestCase):
    
    def test_faqs_with_lang(self):
        response = self.client.get('/api/faqs/?lang=hi')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), 'hi')

    def test_faqs_without_lang(self):
        # Test with no 'lang' parameter (should default to 'en')
        response = self.client.get('/api/faqs/')
        self.assertEqual(response.status_code, 200)  # Check for a successful response
        self.assertEqual(response.content.decode(), 'en')  # Check that the output is 'en'
        
    def test_faqs_with_empty_lang(self):
        # Test with 'lang' parameter set to an empty value
        response = self.client.get('/api/faqs/?lang=bn')
        self.assertEqual(response.status_code, 200)  # Check for a successful response
        self.assertEqual(response.content.decode(), 'bn')  # Check that the output is 'en'
