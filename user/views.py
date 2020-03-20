from django.shortcuts import render
from user.forms import UserForm, PostForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Post
from product.models import Product



def index(request):
    context = {}
    qs = Post.objects.filter().values()
    context['text'] = qs
    if request.user.is_authenticated:
        context['postform'] = PostForm()
    
    if request.method == 'POST':
        post_form = PostForm(data=request.POST)
        if post_form.is_valid():
            post = post_form.save()
            post.user = request.user
            post.save()

    return render(request,'user/index.html', context)

@login_required
def special(request):
    return HttpResponse("You are logged in !")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user:index'))


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request,'user/registration.html',
                          {'user_form':user_form,
                           'registered':registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('user:index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'user/login.html', {})



def post(request, mid):
    context = {}

    if Post.objects.filter(id=mid).values('text'):
        qs = Post.objects.filter(id=mid).values()[0]
        context['text'] = qs['text']
        return render(request, 'user/post.html', context);
    else:
        return render(request, 'user/404.html')


def product(request):
    context = {}
    qs = Product.objects.filter().values()
    context['products'] = qs
    return render(request,'user/shop.html', context)
