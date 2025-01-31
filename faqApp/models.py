from django.db import models
from ckeditor.fields import RichTextField

class FAQ(models.Model):   # FAQ is table name
    faq_id = models.AutoField
    question = models.TextField()
    answer = RichTextField()

    # def __str__(self):
    #     return self.question