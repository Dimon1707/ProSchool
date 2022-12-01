from django.contrib.auth.views import LoginView
from django.urls import path
from core.views import index, register, logout, form, mainpage, ServiceListView, ServiceDetailView
from core.views import customer_form

urlpatterns = [
    # 1-путь,2-функция,3-кр.название
    path('', index, name='index'),
    path('form/', form, name='form'),
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    path('mainpage/', mainpage, name='mp'),
    path('customer/create/', customer_form, name='customer'),
    path('service_list/', ServiceListView, name='s_list'),
    path('service_detail/<int:pk>/', ServiceDetailView.as_view(), name='s_detail'),

]