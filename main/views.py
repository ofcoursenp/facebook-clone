from django.shortcuts import get_object_or_404
from django.shortcuts import render,redirect
from .forms import NewUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import DefineUser,Post,follow

# Create your views here.


@login_required(login_url='login')
def index(req):
    return render(req,'index.html')
    
@login_required(login_url='login')
def profile(req):
    profile = DefineUser.objects.filter(user=req.user).first()
    account_created_at = profile.created_on if profile else None
    profile_pic_url = profile.profilePic.url if profile and profile.profilePic else None
    post = Post.objects.filter(user=req.user)
    print(post)
    send = {'profile': profile, 'profile_pic_url': profile_pic_url, 'account_created_at': account_created_at,'posts':post}
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
                new_user = form.save()  # Save the newly created user
                user = form.cleaned_data.get('username')
                messages.success(req,f'Account was created with username {user}')
                usercreate = DefineUser.objects.create(bio='', user=new_user)  # Assign new_user to the user attribute
                usercreate.save()
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

@login_required(login_url='login')
def create(req):
    if req.method == "POST":
        title = req.POST.get('title')
        text = req.POST.get('content')
        image = req.FILES.get('image')
        user = req.user
        post = Post.objects.create(title=title,text=text,image=image,user=user,likes=0)
        return redirect('home')
    return render(req,'create.html')

@login_required(login_url='login')
def viewUser(req,name):
    if str(req.user.id) == name:
        return redirect('profile')
    profile = DefineUser.objects.filter(user=name).first()
    account_created_at = profile.created_on if profile else None
    profile_pic_url = profile.profilePic.url if profile and profile.profilePic else None
    post = Post.objects.filter(user=name)
    id = req.user.id
    
    print(post)
    try:
        following = follow.objects.get(user=req.user,following=profile)
        is_following = "following"
    except Exception as e:
        is_following = False
        
        # print(is_following)

    
    send = {'profile': profile, 'profile_pic_url': profile_pic_url, 'account_created_at': account_created_at,'posts':post,'following':is_following,'id':id}

    # print(str(req.user.username) == profile)

    # if str(req.user.username) == profile:
    #     return redirect('profile')

    if req.method == 'POST':
        if 'follow' in req.POST:
            f = follow(user=req.user,following=profile)
            f.save()
        elif 'unfollow' in req.POST:
            follow.objects.filter(user=req.user,following=profile).delete()
    
    return render(req, 'user.html', send)

