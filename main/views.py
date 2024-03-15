from django.shortcuts import render
from . import models

# Ushbu funksiya web sahifaning asosiy qismi uchun ishlaydi
# Web sahifaning asosiy qismida barcha pagelar o'rin olgan
# Shuning uchun bu funksiya contextida barcha modellar foydalanilgan
def index(request):
    home = models.Home.objects.last() # Bitta obyekt orqali chiqarib olinadi va oxirgi ya'ni yangisidan foydalaniladi
    about_us = models.AboutUs.objects.all() # Bir qancha mavjudligi uchun all berilgan
    service = models.Service.objects.last() # Bu ham Home kabi servicelarning oxirgisini oladi 
    service.service_title = service.service_title.split('#') # Xizmatlar ichidagi kichik xizmatlar uchun alohida model yozmaslik uchun ular orasini # bilan ajratib yozdim
    blogs = models.Blog.objects.all() # Bunda ham bir qancha obyektlar olinadi
    context = {
        'home':home,
        'about_us':about_us,
        'service':service,
        'blogs':blogs
    }
    if request.method == 'POST': # Bu yer contact uchun 
        try:
            models.Contact.objects.create(
                first_name = request.POST['first_name'],
                last_name = request.POST['last_name'],
                phone_number = request.POST['phone_number'],
                email = request.POST['email'],
                message = request.POST['message'],
            )
        except:
            ...
    return render(request, 'main/index.html', context)

# Pastdagi funksiyalarda context ma'lumotlarni frontenddan olish uchun ishlatilyapti

# Bu funksiya About us qismni shakllantirish  uchun 
def about_us(request):
    about_us = models.AboutUs.objects.all()
    context = {
        'about_us':about_us
    }
    return render(request, 'main/about_us.html', context)

# Bu funksiya Service qismni shakllantirish  uchun 
def service(request):
    service = models.Service.objects.last()
    service.service_title = service.service_title.split('#')
    context = {
        'service':service,
    }
    return render(request, 'main/service.html', context)

# Bu funksiya Blog qismni shakllantirish  uchun 
def blog(request):
    blogs = models.Blog.objects.all()
    context = {
        'blogs':blogs,
    }
    return render(request, 'main/blog.html', context)

# Bu funksiya foydalanuvchilar tomonidan bog'lanish ma'lumotlarini qabul qiladi va databasega yozadi
def contact(request):
    if request.method == 'POST':
        try:
            models.Contact.objects.create(
                first_name = request.POST['first_name'],
                last_name = request.POST['last_name'],
                phone_number = request.POST['phone_number'],
                email = request.POST['email'],
                message = request.POST['message'],
            )
        except:
            ...
    return render(request, 'main/contact.html')