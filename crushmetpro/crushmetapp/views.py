from django.shortcuts import render , redirect
from django.contrib.auth import authenticate,login,logout
from .forms import *
from crushmetapp.models import DemoProfile
# from django.contrib import messages



def index(request):
    return render(request,'index.html')

def registerUser(request):
      form = CreateUserForm()
      if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                # messages.success(request,"Account was successfully created for " + user)
                return redirect('login')
      context = {'form':form}
      return render(request,'signup.html',context)


def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
      #  typeu = request.POST.get('type')

        user = authenticate(request,username=username,password=password)

        if user is not None:
                login(request,user)
                return redirect('pro1')
           
        # else:
        #      messages.info(request,'Username or Password is incorrect !!')
            
    return render(request,'login.html')

def profileUpdate(request):
     profile= request.user.profile
     form = ProfileForm(instance=profile)
     if request.method == 'POST':
          form = ProfileForm(request.POST,request.FILES,instance=profile)
          if form.is_valid():
               form.save() 
     return render(request,'fill_1.html',{'form':form})


# def profile_see(request):
#      profiles = Profile.objects.all()
#      context = {
#           'profiles':profiles
#      }
#      return render(request,'profile.html',context)

def pro1(request):
     profile= request.user.profile
     form = ProfileForm(instance=profile)
     if request.method == 'POST':
          form = ProfileForm(request.POST,request.FILES,instance=profile)
          if form.is_valid():
               form.save() 
     return render(request,'fill_1.html',{'form':form})


def logoutUser(request):
    logout(request)
    return redirect('login')

def updateprof(request):
    user=request.POST['username']   
    gen=request.POST['gender']
    pref=request.POST['preference']
    pro=DemoProfile.objects.update_or_create(username=user,gender=gen,gpref=pref)
    
    return redirect('pro2')

def pro2(request):
     return render(request,'fill_2.html')

def pro3(request):
     return render(request,'fill_3.html')

def updateprof1(request):
    #print("username"+request.POST['uname'])
    uname=request.POST['uname']
    obj=DemoProfile.objects.get(username=uname)
    obj.interest=request.POST['int']   
    obj.show=request.POST['shw']
    obj.pickup=request.POST['pkup']
    obj.about=request.POST['abt']
    obj.save()
    return redirect('pro3')

def updateprof2(request):
    uname=request.POST['uname']
    obj=DemoProfile.objects.get(username=uname)
    obj.city=request.POST['city']   
    obj.dob=request.POST['dob']
    obj.img=request.POST['img']
    obj.save()
    return redirect('index')

def dashboard(request):
     return render(request,'dashboard.html')

def chat(request):
     return render(request,'chat.html')

def dating(request):
     return render(request,'dating.html')