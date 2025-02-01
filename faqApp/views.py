import stat
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import FAQ
from .api.serializers import FAQSerializer
from django.core.cache import cache
import time
from rest_framework import status

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


@api_view(['POST'])
def create_faq(request):
    question = request.data.get('question')
    answer = request.data.get('answer')

    if not question or not answer:
        return Response({"error": "Both 'question' and 'answer' are required."}, status=status.HTTP_400_BAD_REQUEST)

    existing_faq = FAQ.objects.filter(question=question, answer=answer).first()
    if existing_faq:
        return Response({"status": "FAQ already exists with the same question and answer."}, status=status.HTTP_409_CONFLICT)
    
    faq = FAQ(question=question, answer=answer)
    try:
        faq.save()
        return Response({"status": "FAQ created successfully!", "id": faq.id}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)