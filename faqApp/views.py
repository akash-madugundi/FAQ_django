from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import FAQ
from .api.serializers import FAQSerializer
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
    
    translated_data = [faq.translate(lang) for faq in faqs]

    return Response(translated_data)