from django.shortcuts import render,redirect
from .forms import NewUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import DefineUser
# Create your views here.


@login_required(login_url='login')
def index(req):
    return render(req,'index.html')
    
@login_required(login_url='login')
def profile(req):
    profile = DefineUser.objects.filter(user=req.user).first()
    profile_pic_url = profile.profilePic.url if profile and profile.profilePic else None
    send = {'profile': profile, 'profile_pic_url': profile_pic_url}
    return render(req, 'profile.html', send)

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
        return redirect('edit')
    
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

@login_required(login_url='login')
def logoutPage(req):
    logout(req)
    return redirect('login')

@login_required(login_url='login')
def edit(req):
    try:
        document = DefineUser.objects.get(user=req.user)
    except DefineUser.DoesNotExist:
        document = DefineUser(user=req.user)
    if req.method == 'POST':
        file2 = req.FILES.get('file')
        bio = req.POST.get('bio')
        if file2:
            document.profilePic = file2
        if bio:
            document.bio = bio
        document.save()

        return redirect('profile')

    return render(req,'editprofile.html')



