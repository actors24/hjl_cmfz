import hashlib
import json
import random
import time

from django.core.paginator import Paginator
from django.http import HttpResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from user.models import User


def check_user(request):
    user = User.objects.all()
    rows = request.GET.get('rows')
    page = request.GET.get('page', 1)
    pagtor = Paginator(user, per_page=rows)
    try:
        pager = pagtor.page(page).object_list
    except:
        pager = pagtor.page(int(page) - 1).object_list
    page_data = {
        "page": page,
        "total": pagtor.num_pages,
        "records": pagtor.count,
        "rows": list(pager)
    }

    def mydefault(u):
        if isinstance(u, User):
            return {'id': u.pk, 'username': u.user_name, 'fa_name': u.fa_name, 'gender': u.gender,
                    'address': u.address, 'email': u.e_mail, 'brief': u.personal_brief, 'pic': str(u.image),
                    'status': u.status, 'phone': u.phone,
                    'register_time': u.register_time.strftime('%Y-%m-%d %H:%M:%S')}
    data = json.dumps(page_data, default=mydefault)
    return HttpResponse(data)


@csrf_exempt
def add_user(request):
    user_name = request.POST.get('user_name')
    fa_name = request.POST.get('fa_name')
    password = request.POST.get('password')
    gender = request.POST.get('gender')
    address = request.POST.get('address')
    e_mail = request.POST.get('e_mail')
    brief = request.POST.get('brief')
    pic = request.FILES.get('pic')
    status = request.POST.get('status')
    phone = request.POST.get('phone')
    salt = str(random.randint(100000, 999999))
    sha = hashlib.sha1()
    sha.update((password + salt).encode())
    password = sha.hexdigest()
    now_time = time.strftime("%Y-%m-%d %H:%M:%S")
    print(user_name, fa_name, password, gender, address, e_mail, brief, pic, status, phone)
    User.objects.create(user_name=user_name, fa_name=fa_name, passeord=password, salt=salt, gender=gender,
                        address=address, e_mail=e_mail, personal_brief=brief, image=pic, status=status, phone=phone,
                        register_time=now_time)
    return HttpResponse(1)
