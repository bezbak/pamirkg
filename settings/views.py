from django.shortcuts import render, redirect
from .models import Setting, Tours, Video, Photo
from django.core.mail import send_mail
# Create your views here.
def index(request):
    setting = Setting.objects.latest('id')
    if request.method == 'POST':
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        comment = request.POST.get("comment")
        text = f"""
            ФИО: {full_name},
            Почта: {email},
            Номер телефона: {phone},
            Сообщение: {comment}
        """
        send_mail(
                    #subject 
                    f"Запрос от {full_name}", 
                    #message 
                    f"{text}", 
                    #from email 
                    'noreply@somehost.local', 
                    #to email 
                    ['info.pamirtour@gmail.com'] 
        ) 
        return redirect('index')
    context = {
        'setting':setting,
        'name':'main'
    }
    return render(request, 'main.html', context)

def tours(request):
    setting = Setting.objects.latest('id')
    tours = Tours.objects.all()
    if request.method == 'POST':
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        comment = request.POST.get("comment")
        text = f"""
            ФИО: {full_name},
            Почта: {email},
            Номер телефона: {phone},
            Сообщение: {comment}
        """
        send_mail(
                    #subject 
                    f"Запрос от {full_name}", 
                    #message 
                    f"{text}", 
                    #from email 
                    'noreply@somehost.local', 
                    #to email 
                    ['info.pamirtour@gmail.com'] 
        ) 
        return redirect('tours')
    context = {
        'setting':setting,
        'name':'kyr',
        'tours':tours
    }
    return render(request, "kyrgyzstan.html",context)

def contact(request):
    setting = Setting.objects.latest('id')
    if request.method == 'POST':
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        comment = request.POST.get("comment")
        text = f"""
            ФИО: {full_name},
            Почта: {email},
            Номер телефона: {phone},
            Сообщение: {comment}
        """
        send_mail(
                    #subject 
                    f"Запрос от {full_name}", 
                    #message 
                    f"{text}", 
                    #from email 
                    'noreply@somehost.local', 
                    #to email 
                    ['info.pamirtour@gmail.com'] 
        ) 
        return redirect('contact')
    context = {
        'setting':setting,
        'name':'contact'
    }
    return render(request, 'contact.html',context)

def gallery(request):
    setting = Setting.objects.latest('id')
    if request.method == 'POST':
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        comment = request.POST.get("comment")
        text = f"""
            ФИО: {full_name},
            Почта: {email},
            Номер телефона: {phone},
            Сообщение: {comment}
        """
        send_mail(
                    #subject 
                    f"Запрос от {full_name}", 
                    #message 
                    f"{text}", 
                    #from email 
                    'noreply@somehost.local', 
                    #to email 
                    ['info.pamirtour@gmail.com'] 
        ) 
        return redirect('gallery')
    context = {
        'setting':setting,
        'name':'gallery'
    }
    return render(request, 'gallery.html',context)

def photos(request):
    setting = Setting.objects.latest('id')
    photos = Photo.objects.all()
    if request.method == 'POST':
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        comment = request.POST.get("comment")
        text = f"""
            ФИО: {full_name},
            Почта: {email},
            Номер телефона: {phone},
            Сообщение: {comment}
        """
        send_mail(
                    #subject 
                    f"Запрос от {full_name}", 
                    #message 
                    f"{text}", 
                    #from email 
                    'noreply@somehost.local', 
                    #to email 
                    ['info.pamirtour@gmail.com'] 
        ) 
        return redirect('photos')
    context = {
        'setting':setting,
        'photos':photos,
        'name':'gallery',
    }
    return render(request, 'photos.html',context)

def video(request):
    setting = Setting.objects.latest('id')
    videos = Video.objects.all()
    if request.method == 'POST':
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        comment = request.POST.get("comment")
        text = f"""
            ФИО: {full_name},
            Почта: {email},
            Номер телефона: {phone},
            Сообщение: {comment}
        """
        send_mail(
                    #subject 
                    f"Запрос от {full_name}", 
                    #message 
                    f"{text}", 
                    #from email 
                    'noreply@somehost.local', 
                    #to email 
                    ['info.pamirtour@gmail.com'] 
        ) 
        return redirect('video')
    context = {
        'setting':setting,
        'name':'gallery',
        'css1':"video",
        'videos':videos
    }
    return render(request, 'video.html',context)

def tour(request, id):
    setting = Setting.objects.latest('id')
    tour = Tours.objects.get(id= id)
    if request.method == 'POST':
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        comment = request.POST.get("comment")
        text = f"""
            ФИО: {full_name},
            Почта: {email},
            Номер телефона: {phone},
            Сообщение: {comment}
        """
        send_mail(
                    #subject 
                    f"Запрос от {full_name}", 
                    #message 
                    f"{text}", 
                    #from email 
                    'noreply@somehost.local', 
                    #to email 
                    ['info.pamirtour@gmail.com'] 
        ) 
        return redirect('tour', tour.id)
    context = {
        'setting':setting,
        'name':'tours',
        'tour':tour
    }
    return render(request, 'tour.html',context)
