from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserLoginForm, FormSubmissionForm
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import FormSubmission
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import UserProfile, FormSubmission


from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('options')
    else:
        form = UserLoginForm()
    # Explicitly create a new form to ensure no cached data
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})



def options_view(request):
    return render(request, 'options.html')

def process_option_view(request):
    if request.method == 'POST':
        selected_option = request.POST.get('option')
        request.session['selected_option'] = selected_option
        if selected_option == 'fill_form':
            return redirect('form')
        elif selected_option == 'view_summary':
            return redirect('dashboard')
    return redirect('options')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create a UserProfile for the new user
            UserProfile.objects.create(user=user)
            messages.success(request, 'User registered successfully')
            return redirect('register')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def form_success_view(request):
    latest_submission = FormSubmission.objects.latest('id')
    return render(request, 'form_success.html', {'submission': latest_submission})

@login_required(login_url='login')
def dashboard_view(request):
    user_profile = UserProfile.objects.get(user=request.user)
    try:
        latest_submission = FormSubmission.objects.latest('id')
    except FormSubmission.DoesNotExist:
        latest_submission = None
    context = {
        'profile': user_profile,
        'submission': latest_submission,
        'has_photo': bool(latest_submission.photo) if latest_submission else False,
        'has_document': bool(latest_submission.doctors_prescription) if latest_submission else False
    }
    return render(request, 'dashboard.html', context)

@login_required(login_url='login')
def form_view(request):
    if request.method == 'POST':
        form = FormSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('form_success')
    else:
        form = FormSubmissionForm()
    return render(request, 'form.html', {'form': form})






def logout_view(request):
    logout(request)
    return redirect('login')
