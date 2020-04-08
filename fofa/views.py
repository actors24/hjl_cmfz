from django.http import HttpResponse
from django.shortcuts import render
from redis import Redis
from hjl_cmfz.settings import API_KEY
from utils.send_message import YunPian
from utils.random_code import get_code
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
red = Redis(host='192.168.133.128', port=6379)


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


@csrf_exempt
def get_phone_code(request):
    number = request.POST.get('number')
    try:
        result = red.get(number+'_1')
        if result:
            print(0)
            return HttpResponse(0)
        else:
            code = get_code()
            pian = YunPian(API_KEY)
            if pian.send_message(number, code) == 200:
                red.set(number+'_1', code, 120)
                red.set(number+'_2', code, 600)
                return HttpResponse(1)
            else:
                return HttpResponse(0)
    except:
        return HttpResponse(0)


def check_code(request):
    number = request.GET.get('mobile')
    code = request.GET.get('code')
    try:
        result = red.get(number+'_2')
        if result.decode('utf-8') == code:
            return HttpResponse(1)
        else:
            return HttpResponse(0)
    except:
        return HttpResponse(0)
