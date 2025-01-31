from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator

class FAQ(models.Model):
    faq_id = models.AutoField
    question = models.TextField()
    answer = RichTextField()

    # def __str__(self):
    #     return self.question
    def translate(self, lang='en'):
        translator = Translator()
        translated_question = translator.translate(self.question, dest=lang).text
        translated_answer = translator.translate(self.answer, dest=lang).text

        return {
            'id': self.id,
            'question': translated_question,
            'answer': translated_answer
        }