from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator, LANGUAGES

class FAQ(models.Model):
    faq_id = models.AutoField
    question = models.TextField()
    answer = RichTextField()
    lang_hi = models.TextField(null=True, blank=True)
    lang_hi_answer = models.TextField(null=True, blank=True)
    lang_bn = models.TextField(null=True, blank=True)
    lang_bn_answer = models.TextField(null=True, blank=True)
    lang_fr = models.TextField(null=True, blank=True)
    lang_fr_answer = models.TextField(null=True, blank=True)

    def translate(self, lang='en'):
        if lang not in LANGUAGES:
            lang='en'
        translator = Translator()
        translated_question = translator.translate(self.question, dest=lang).text
        translated_answer = translator.translate(self.answer, dest=lang).text

        return {    
            'id': self.id,
            'question': translated_question,
            'answer': translated_answer
        }
    
    
    def save(self, *args, **kwargs):
        if not self.lang_hi:
            self.lang_hi = Translator().translate(self.question, dest='hi').text
            self.lang_hi_answer = Translator().translate(self.answer, dest='hi').text

        if not self.lang_bn:
            self.lang_bn = Translator().translate(self.question, dest='bn').text
            self.lang_bn_answer = Translator().translate(self.answer, dest='bn').text

        if not self.lang_fr:
            self.lang_fr = Translator().translate(self.question, dest='fr').text
            self.lang_fr_answer = Translator().translate(self.answer, dest='fr').text
        
        super().save(*args, **kwargs)