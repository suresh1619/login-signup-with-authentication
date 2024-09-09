from django.shortcuts import render,redirect
from login.models import login_details,Signup

# Create your views here.

def login(request):
    username=''
    password=''
    ans={}

    try:
        if request.method=='POST':
            username=request.POST.get('username','')
            password=request.POST.get('password','')
            data=Signup.objects.all()
            for i in data:
                if i.username==username and i.password==password:
                    ans={'data': username }
                    return redirect('home')
                else:
                    ans={'data': 'wrong crediential'}
            

    except Exception as e:
        pass
    return render(request,'login.html',ans)


def signup(request):
    first_name=''
    last_name=''
    email=''
    username=''
    password=''
    try:
        if request.method == 'POST':
            first_name = request.POST.get('first_name','')
            last_name = request.POST.get('last_name','')
            email = request.POST.get('email','')
            username = request.POST.get('username','')
            password = request.POST.get('password','')
            data=Signup(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
            data.save()
            
    except Exception as e:
        pass
    return render(request,'signup.html',{'first_name':first_name})
def home(request):
    return render(request,'home.html')

    