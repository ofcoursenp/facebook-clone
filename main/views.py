from django.shortcuts import render,redirect
from .forms import NewUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='login')
def index(req):
    return render(req,'index.html')
    
@login_required(login_url='login')
def profile(req):
    return render(req,'profile.html')

def register(req): 
    if req.user.is_authenticated:
        return redirect('home')
    else: 
        form = NewUserCreationForm()
        send = {'form':form}
        if req.method == "POST":
            form = NewUserCreationForm(req.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(req,f'Account was created with username {user}')
                return redirect('login')
        return render(req,'register.html',send)

def loginPage(req):
    if req.user.is_authenticated:
        return redirect('home')
    
    else:
        if req.method == "POST":
            username = req.POST.get('username')
            password = req.POST.get('password')

            user = authenticate(req, username=username, password=password)
            if user is not None:
                login(req,user)
                return redirect('home')

            else:
                messages.warning(req,'Username or password is incorrect')
                return render(req,'login.html')

        return render(req,'login.html')


def logoutPage(req):
    logout(req)
    return redirect('login')


