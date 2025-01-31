from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import FAQ
from .api.serializers import FAQSerializer

def home(request):
    return HttpResponse("Hello World")

# def getfaqs(request):
#     # lang = request.GET.get('lang', '').strip()
#     lang = request.GET.get('lang', '').strip()
#     if not lang:
#         lang = 'en'
#     return HttpResponse(lang)

@api_view(['GET'])
def get_faqs(request):
    lang = request.GET.get('lang', 'en').strip() 
    faqs = FAQ.objects.all()
    predefined_languages = ['hi', 'bn', 'fr']
    
    if lang not in predefined_languages:
        translated_data = [faq.translate(lang) for faq in faqs]
    else:
        translated_data = []
        for faq in faqs:
            faq_data = {
                'id': faq.id,
                'question': getattr(faq, f'lang_{lang}', faq.question),
                'answer': getattr(faq, f'lang_{lang}_answer', faq.answer)
            }
            translated_data.append(faq_data)

    return Response(translated_data)