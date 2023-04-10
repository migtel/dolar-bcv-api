from django.http import JsonResponse
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.views.decorators.csrf import csrf_exempt
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings


# Create your views here.
@csrf_exempt
def dolar(request):
    disable_warnings(InsecureRequestWarning)
    url = 'https://www.bcv.org.ve/'
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.text, 'html.parser')
    dolar = float(soup.find('div', {'id': 'dolar'}).text.strip().replace(',', '.').replace("USD \n ", ""))
    print('USD: ', dolar)
    return JsonResponse({'dolar': dolar})
