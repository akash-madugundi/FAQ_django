from django.contrib import admin
from .models import FAQ

class FAQAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'answer', 'lang_hi', 'lang_hi_answer', 'lang_bn', 'lang_bn_answer', 'lang_fr', 'lang_fr_answer')
    search_fields = ('id', 'question', 'answer')

admin.site.register(FAQ, FAQAdmin)
