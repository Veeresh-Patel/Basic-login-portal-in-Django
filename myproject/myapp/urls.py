
from django.urls import path
from .views import login_view, register_view, form_view, dashboard_view, logout_view, form_success_view, options_view, process_option_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('form/', form_view, name='form'),
    path('form_success/', form_success_view, name='form_success'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('options/', options_view, name='options'),
    path('process_option/', process_option_view, name='process_option'),
    path('logout/', logout_view, name='logout'),
]


