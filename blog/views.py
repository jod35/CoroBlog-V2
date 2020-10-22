from django.shortcuts import render,redirect
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostCreationForm
from django.views.generic import UpdateView,DeleteView
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.

#home
def index(request):
    posts=Post.published.all()
    context={
        'posts':posts
    }
    return render(request,'blog/index.html',context)

#registration
def register(request):
    form=UserRegistrationForm()
    
    if request.method =="POST":
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            
            messages.success(request,"Account Creation Successful, Please Login")

            return redirect('blog:login')

    context={
        'form':form
    }
    return render(request,'blog/signup.html',context)

@login_required 
def post_details(request,slug):
    post=Post.objects.filter(slug=slug).first()
    context={
        'post':post
    }
    return render(request,'blog/postdetails.html',context)

@login_required
def home_page(request):
    posts=Post.published.all()
    context={
        'posts':posts
    }
    return render(request,'blog/home.html',context)

def create_post(request):
    form=PostCreationForm()

    if request.method =="POST":
        form=PostCreationForm(request.POST)

        if form.is_valid():
            obj=form.save(commit=False)

            obj.author=request.user

            obj.save()

            messages.success(request,"Post Created Successfully")

            return redirect('blog:user_posts')

    context={
        'form':form
    }

    return render(request,'blog/createpost.html',context)

def posts(request):
    posts=Post.published.all()
    
    context={
        'posts':posts
    }

    return render(request,'blog/posts.html',context)

def my_posts(request):
    posts=Post.objects.filter(author=request.user).all()

    context={
        'posts':posts
    }

    return render(request,'blog/myposts.html',context)


class PostEditView(UpdateView,SuccessMessageMixin):
    model=Post
    fields=['title','body']
    template_name='blog/editpost.html'
    success_url="/posts/"
    success_message="Post has been Updated successfully"


class PostDeleteView(DeleteView):
    model=Post
    template_name='blog/deletepost.html'
    success_url="/my_posts/"
    context_object_name='post'
