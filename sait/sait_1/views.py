from django.shortcuts import render
from django.http import HttpResponse
import datetime
from math import pi
from .forms import StudentForm

def home(request):
    now = datetime.datetime.now()
    context = {
        "img" :"sait_1/images/фото.jpg",
        "name" :"Мураткин Илья Сергеевич",
        "phone" :"890006620444",
        "email" :"ismuratkin@edu.hse.ru",
        "group" :"Экономика",
        'now': now,
        "img_1" :"sait_1/images/фото_1.jpg",
        "name_1" :"Байгужин Искандер Рустамович",
        "phone_1" :"цифры)",
        "email_1" :"irbaigushin@edu.hse.ru",
        "prepod" : "Марширов В.В."

    }
    return render(request, 'home.html', context)

def index(request):
    return HttpResponse("Тут нет сайта. Иди сюда -> http://127.0.0.1:8000/home/")

def razdel_1(request):
    return render(request, 'razdel_1.html')

def zadacha(request, A, H, R, M):
    # http://127.0.0.1:8000/responseApp/f_str_int_slug/x=1&y=2/123/1st-django-site

    kub_volume = A**3
    cilindr_volume = R**2 * H * pi

    kub = M <= kub_volume
    cilindr = M <= cilindr_volume

    fits = "ни в одну фигуру"
    if kub and cilindr:
        fits = "в обе фигуры"
    elif kub:
        fits = "в куб"
    elif cilindr:
        fits = "в цилиндр"

    context = {
        'A': A,
        'H': H,
        'R': R,
        'M': M,
        'kub_volume': kub_volume,
        'cilindr_volume': cilindr_volume,
        'kub': kub,
        'cilindr': cilindr,
        'fits': fits,
    }
    return render(request, 'zadacha.html', context)

def student_grades(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            names = form.cleaned_data['names'].split()
            grades = form.cleaned_data['grades'].split()

            student_scores = {}
            for i, name in enumerate(names):
                grade_list = grades[i].split('-')
                total_score = sum(int(grade) for grade in grade_list)
                student_scores[name] = total_score

            if student_scores: 
                best_student = max(student_scores, key=student_scores.get)
                context = {'form': form, 'best_student': best_student}
                return render(request, 'student_grades.html', context)
    else:
        form = StudentForm()
    return render(request, 'student_grades.html', {'form': form})

def massiv(request):
    objects_array = [
        {
            "id": "1",
            "title": "Сникерс",
            "description": "Шоколадка",
            "price": 100,
            "img": "sait_1/images/snikers.jpg"
        },
        {
            "id": "2",
            "title": "Баунти",
            "description": "Шоколадка",
            "price": 200,
            "img": "sait_1/images/bounty.jpeg"
        },
        {
            "id": "3",
            "title": "Киткат",
            "description": "Шоколадка",
            "price": 300,
            "img": "https://avatars.mds.yandex.net/get-mpic/5177644/img_id5690238125692061619.jpeg/orig"
        },
        {
            "id": "4",
            "title": "Твикс",
            "description": "Шоколадка",
            "price": 400,
            "img": "https://main-cdn.sbermegamarket.ru/big1/hlr-system/582/366/004/103/014/19/100023331887b0.jpg"
        }
    ]
    dict_of_array = {'objects_array': objects_array}
    context = {'dict_of_array': dict_of_array}
    return render(request, "massiv.html", context)