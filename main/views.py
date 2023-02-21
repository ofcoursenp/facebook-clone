from django.shortcuts import get_object_or_404
from django.shortcuts import render,redirect,HttpResponse
from .forms import NewUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import DefineUser,Post,follow,Like,Comment

# Create your views here.

def landing(req):
    return render(req,'landing.html')

@login_required(login_url='login')
def Like_post(req, post_id):
    
    userforlike = req.user
    post = get_object_or_404(Post, id=post_id)
    profile = DefineUser.objects.filter(user=post.user).first()
    profile_pic_url = profile.profilePic.url if profile and profile.profilePic else None
    current_likes = post.likes
    liked = Like.objects.filter(user=userforlike,post=post).count()
    comment_text = req.POST.get('comment_text')
    user_id = userforlike.id
    is_liked = ''
    if not liked:
        is_liked = ""
        comments = Comment.objects.filter(post=post).order_by('-id')
        send = {'items': post,'profile':profile_pic_url,'liked':is_liked,'comments':comments,'user_id':user_id}

    else:
        is_liked = "liked"
        comments = Comment.objects.filter(post=post).order_by('-id')
        send = {'items': post,'profile':profile_pic_url,'liked':is_liked,'comments':comments,'user_id':user_id}

    if req.POST.get('like'):
        if userforlike == post.user:
            messages.info(req,'You cant like ur own post')
            return redirect('home')
        if not liked:
            is_liked=''
            liked = Like.objects.create(user=userforlike,post=post)
            current_likes +=1
            comments = Comment.objects.filter(post=post).order_by('-id')
            send = {'items': post,'profile':profile_pic_url,'liked':is_liked,'comments':comments,'user_id':user_id}

        else:
            print(False)
            is_liked='liked'
            liked = Like.objects.filter(user=userforlike,post=post).delete()
            current_likes -=1
            comments = Comment.objects.filter(post=post).order_by('-id')
            send = {'items': post,'profile':profile_pic_url,'liked':is_liked,'comments':comments,'user_id':user_id}

    if req.POST.get('comment'):
        comment_text = req.POST.get('comment')
        if comment_text:
            new_comment = Comment.objects.create(user=userforlike, post=post, comment=comment_text)
            messages.success(req, 'Comment added successfully')
        else:
            messages.error(req, 'Comment text cannot be empty')

        comments = Comment.objects.filter(post=post).order_by('-id')
        send = {'items': post,'profile':profile_pic_url,'liked':is_liked,'comments':comments,'user_id':user_id}

    print(comments)
    comments = Comment.objects.filter(post=post).order_by('-id')
    print(comments)     
    post.likes = current_likes
    post.save()
    print(post.title)
    print(is_liked)
    send = {'items': post,'profile':profile_pic_url,'liked':is_liked,'comments':comments,'user_id':user_id}
    return render(req, 'specificpost.html', send)
    
    

@login_required(login_url='login')
def index(req):
    # followed = follow.objects.filter(user=req.user)
    # print(followed)
    users = follow.objects.filter(user_id=req.user.id)

    add_post = []
    for user in users:
        get_post = Post.objects.filter(user__username=user)
        add_post.append(get_post)
        # print(get_post.id)

    if users:
        send = {'following':add_post}
        return render(req,'index.html',send)
    return render(req,'index.html')
    

@login_required(login_url='login')
def profile(req):
    profile = DefineUser.objects.filter(user=req.user).first()
    account_created_at = profile.created_on if profile else None
    account_bio = profile.bio if account_created_at else None
    profile_pic_url = profile.profilePic.url if profile and profile.profilePic else None
    post = Post.objects.filter(user=req.user)
    print(post)
    send = {'profile': profile, 'profile_pic_url': profile_pic_url, 'account_created_at': account_created_at,'posts':post,'account_bio':account_bio,}
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
                print(new_user)
                user = form.cleaned_data.get('username')
                messages.success(req,f'Account was created with username {user}')
                usercreate = DefineUser.objects.create(bio='', user=new_user)  # Assign new_user to the user attribute
                usercreate.save()
                return redirect('login')
            else:
                messages.info(req, 'invalid registration details')
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


@login_required(login_url='login')
def chatPage(req):

    return render(req,'chat.html')


