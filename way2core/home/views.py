from django.shortcuts import render, get_object_or_404, redirect
from home.models import IoTListModel
from home.forms import checkout, IdeaForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.core.mail import send_mail


# Create your views here.
def home(request):
    form=IdeaForm()
    if request.method=='POST':
        form=IdeaForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['name']
            Email=form.cleaned_data['Email']
            subject= 'Your Idea Submitted Successfully'
            msg='Hello {}, Your Idea Submitted successfully, Our technical team will contact you within 24 hours  \n Thank you for joining with us \n\n Mail from way2core technologies'.format(username)
            sender='way2coretech@gmail.com'
            send_mail(subject,msg,sender,[Email,],fail_silently=False)
    return render(request,'home/index.html',{'form':form})

def ListView(request):
    project_list=IoTListModel.objects.all()
    form=IdeaForm()
    if request.method=='POST':
        form=IdeaForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['name']
            Email=form.cleaned_data['Email']
            subject= 'Your Idea Submitted Successfully'
            msg='Hello {}, Your Idea Submitted successfully, Our technical team will contact you within 24 hours  \n Thank you for joining with us \n\n Mail from way2core technologies'.format(username)
            sender='way2coretech@gmail.com'
            send_mail(subject,msg,sender,[Email,],fail_silently=False)
            return redirect('/')
    paginator=Paginator(project_list,10)
    page_number=request.GET.get('page')
    try:
        project_list=paginator.page(page_number)
    except PageNotAnInteger:
        project_list=paginator.page(1)
    except EmptyPage:
        project_list=paginator.page(paginator.num_pages)
    return render(request, 'home/list.html',{'project_list':project_list,'form':form})

def checkout_view(request):
    return render(request,'home/checkout.html')

@login_required
def detail_view(request,url):
    project=get_object_or_404(IoTListModel, slug=url)
    form=checkout()
    if request.method=='POST':
        form=checkout(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['name']
            Email=form.cleaned_data['Email']
            title=form.cleaned_data['title']
            subject= 'Order Successful'
            msg='Hello {}, Your Order titled "{}" placed successfully, Our technical team will contact you within 24 hours  \n Thank you for joining with us \n\n Mail from way2core technologies'.format(username, title)
            sender='way2coretech@gmail.com'
            send_mail(subject,msg,sender,[Email,],fail_silently=False)
            return redirect('/checkout')

    return render(request, 'home/detail.html',{'project':project,'form':form})
