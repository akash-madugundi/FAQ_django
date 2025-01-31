from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from faqApp.models import FAQ
from django.core.cache import cache

class FAQApiTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        cache.clear() 

        self.faq_api_1 = FAQ.objects.create(
            question="What is the currency of Japan?",
            answer="Yen"
        )
        self.faq_api_2 = FAQ.objects.create(
            question="What is the tallest mountain in the world?",
            answer="Mount Everest"
        )
        self.faq_api_1.save()
        self.faq_api_2.save()

    def test_get_faqs_default_lang(self):
        response = self.client.get('/api/faqs/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.data
        self.assertEqual(data[0]['question'], self.faq_api_1.question)
        self.assertEqual(data[0]['answer'], self.faq_api_1.answer)
        self.assertEqual(data[1]['question'], self.faq_api_2.question)
        self.assertEqual(data[1]['answer'], self.faq_api_2.answer)

    def test_get_faqs_hindi_lang(self):
        response = self.client.get('/api/faqs/?lang=hi')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.data
        self.assertEqual(data[0]['question'], self.faq_api_1.lang_hi)
        self.assertEqual(data[0]['answer'], self.faq_api_1.lang_hi_answer)
        self.assertEqual(data[1]['question'], self.faq_api_2.lang_hi)
        self.assertEqual(data[1]['answer'], self.faq_api_2.lang_hi_answer)

    def test_get_faqs_bengali_lang(self):
        response = self.client.get('/api/faqs/?lang=bn')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.data
        self.assertEqual(data[0]['question'], self.faq_api_1.lang_bn)
        self.assertEqual(data[0]['answer'], self.faq_api_1.lang_bn_answer)
        self.assertEqual(data[1]['question'], self.faq_api_2.lang_bn)
        self.assertEqual(data[1]['answer'], self.faq_api_2.lang_bn_answer)

    def test_get_faqs_french_lang(self):
        response = self.client.get('/api/faqs/?lang=fr')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.data
        self.assertEqual(data[0]['question'], self.faq_api_1.lang_fr)
        self.assertEqual(data[0]['answer'], self.faq_api_1.lang_fr_answer)
        self.assertEqual(data[1]['question'], self.faq_api_2.lang_fr)
        self.assertEqual(data[1]['answer'], self.faq_api_2.lang_fr_answer)