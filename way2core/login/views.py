from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from login.forms import Signupform, Forgot_pwd
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
# Create your views here.
@login_required
def home(request):
    return render(request,'login/index.html')

def signup(request):
    form=Signupform()
    if request.method=='POST':
        form=Signupform(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            username=form.cleaned_data['username']
            subject= 'signup successful'
            msg='Hello {}, your account created successfully \n Thank you for joining with us \n\n Mail from way2core technologies'.format(username)
            sender='way2coretech@gmail.com'
            send_mail(subject,msg,sender,[email,],fail_silently=False)
            user=form.save()
            user.set_password(user.password)
            user.save()
            return redirect('/accounts/login')
    return render(request,'login/signup.html',{'form':form})

def validate_view(request):
    username=request.GET.get('username',None)
    data={
    'is_taken':User.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this username already exists.'
    return JsonResponse(data)

# def forgotpwd(request):
#     form=Forgot_pwd()
#     if request.method=='POST':
#         form=Forgot_pwd(request.POST)
#         if form.is_valid():
#             email=form.cleaned_data['Email']
#             username=form.cleaned_data['Username']
#         return redirect('/accounts/login')
#     return render(request,'login/forgotmail.html', {'form':form})
#
# def forgotajax(request):
#     username=request.GET.get('username',None)
#     email=request.GET.get('email',None)
#     data={
#     'is_taken':User.objects.filter(username__iexact=username,email__iexact=email).exists()
#     }
#     if data['is_taken']:
#         data['success_message'] = "We've emailed you instructions for setting your password, if an account exists with the email you entered. You should receive them shortly."
#     else:
#         data['error_message'] = 'A user with this username & email id not exists.'
#     return JsonResponse(data)

def logout(request):
    return render(request,'login/logout.html')
