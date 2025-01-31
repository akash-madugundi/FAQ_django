from django.test import TestCase
from faqApp.models import FAQ
from googletrans import Translator

class FAQModelTest(TestCase):

    def setUp(self):
        self.faq_model_1 = FAQ.objects.create(
            question="What is the capital of India?",
            answer="New Delhi"
        )
        self.faq_model_2 = FAQ.objects.create(
            question="What is the largest ocean in the world?",
            answer="Pacific Ocean"
        )


    def test_translation_fields(self):
        self.faq_model_1.save()
        translator = Translator()
        
        expected_hi1 = translator.translate(self.faq_model_1.question, dest='hi').text
        expected_bn1 = translator.translate(self.faq_model_1.question, dest='bn').text
        expected_fr1 = translator.translate(self.faq_model_1.question, dest='fr').text
        
        self.assertEqual(self.faq_model_1.lang_hi, expected_hi1)
        self.assertEqual(self.faq_model_1.lang_bn, expected_bn1)
        self.assertEqual(self.faq_model_1.lang_fr, expected_fr1)


        self.faq_model_2.save()
        expected_hi2 = translator.translate(self.faq_model_2.question, dest='hi').text
        expected_bn2 = translator.translate(self.faq_model_2.question, dest='bn').text
        expected_fr2 = translator.translate(self.faq_model_2.question, dest='fr').text
        
        self.assertEqual(self.faq_model_2.lang_hi, expected_hi2)
        self.assertEqual(self.faq_model_2.lang_bn, expected_bn2)
        self.assertEqual(self.faq_model_2.lang_fr, expected_fr2)


    def test_answer_translation_fields(self):
        self.faq_model_1.save()
        translator = Translator()
        
        expected_hi_answer1 = translator.translate(self.faq_model_1.answer, dest='hi').text
        expected_bn_answer1 = translator.translate(self.faq_model_1.answer, dest='bn').text
        expected_fr_answer1 = translator.translate(self.faq_model_1.answer, dest='fr').text

        self.assertEqual(self.faq_model_1.lang_hi_answer, expected_hi_answer1)
        self.assertEqual(self.faq_model_1.lang_bn_answer, expected_bn_answer1)
        self.assertEqual(self.faq_model_1.lang_fr_answer, expected_fr_answer1)


        self.faq_model_2.save()
        expected_hi_answer2 = translator.translate(self.faq_model_2.answer, dest='hi').text
        expected_bn_answer2 = translator.translate(self.faq_model_2.answer, dest='bn').text
        expected_fr_answer2 = translator.translate(self.faq_model_2.answer, dest='fr').text

        self.assertEqual(self.faq_model_2.lang_hi_answer, expected_hi_answer2)
        self.assertEqual(self.faq_model_2.lang_bn_answer, expected_bn_answer2)
        self.assertEqual(self.faq_model_2.lang_fr_answer, expected_fr_answer2)