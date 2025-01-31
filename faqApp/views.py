from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import FAQ
from .api.serializers import FAQSerializer
from googletrans import Translator

# Create your views here.

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
    serializer = FAQSerializer(faqs, many=True)

    if not lang:
        lang = 'en'
        
    translator = Translator()
    translated_data = []

    for faq in serializer.data:
        translated_question = translator.translate(faq['question'], dest=lang).text
        translated_answer = translator.translate(faq['answer'], dest=lang).text
        translated_data.append({
            'id': faq['id'],
            'question': translated_question,
            'answer': translated_answer
        })

    return Response(translated_data)