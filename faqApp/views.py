from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import FAQ
from .api.serializers import FAQSerializer
from django.core.cache import cache
import time

def home(request):
    return HttpResponse("Hello World")

@api_view(['GET'])
def get_faqs(request):
    lang = request.GET.get('lang', 'en').strip() 

    faqs_cache_key = f"faqs_{lang}"
    cached_faqs = cache.get(faqs_cache_key)
    if cached_faqs:
        return Response(cached_faqs)
    
    # time.sleep(5)       # testing cache by putting db into sleep for 5sec when retrieving data from db
    faqs = FAQ.objects.all()
    predefined_languages = ['hi', 'bn', 'fr']
    
    translated_data = []
    if lang not in predefined_languages:
        translated_data = [faq.translate(lang) for faq in faqs]
    else:
        for faq in faqs:
            faq_data = {
                'id': faq.id,
                'question': getattr(faq, f'lang_{lang}', faq.question),
                'answer': getattr(faq, f'lang_{lang}_answer', faq.answer)
            }
            translated_data.append(faq_data)

    cache.set(faqs_cache_key, translated_data, timeout=3600)

    return Response(translated_data)