from django.shortcuts import render
from django.contrib.auth.views import auth_logout
from core.forms import UserRegistrationForm
from core.models import Customer, Service
from django.views.generic import CreateView,  DetailView


def index(reguest):
    '''

     Это функция отрисовки гл.страницы

    '''
    return render(reguest, 'sofiindex.html')


def mainpage(reguest):
    '''

     Это функция отрисовки 2 страницы

    '''
    return render(reguest, 'mp.html')


def mainpage1(reguest):
    '''

     Это функция отрисовки 2 страницы

    '''
    return render(reguest, 'mp.html')


def form(request):
    '''

    Это функция отрисовки формы регистрации

    '''
    if request.method == 'GET':
        return render(request, 'form.html')
    elif request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        new_contact = Contact(name=name, email=email)
        new_contact.save()

        return render(request, 'form.html')


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save()
            new_user.set_password(user_form.cleaned_data['password_1'])
            new_user.save()
            return render(request, 'form.html', {'new_user': new_user})
    user_form = UserRegistrationForm()
    return render(request, 'register.html', {'user_form': user_form})


def logout(request):
    auth_logout(request)
    return render(request, 'form.html')


def customer_form(request):
    if request.method == 'GET':
        return render(request, 'form.html')

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        customer = Customer(name=name, phone=phone, email=email)
        customer.save()
        return render(request, 'form.html')


def ServiceListView(request):
    if request.method == 'GET':
        ServiceList = Service.objects.all()
        context = {'ServiceList': ServiceList, }
        return render(request, 'service_list.html', context)


class ServiceDetailView(DetailView):
    model = Service
    context_object_name = 'ServiceDetail'
    template_name = 'service_detail.html'