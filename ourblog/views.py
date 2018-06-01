from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required, permission_required
from ourblog.models import Blog, Blogger, Comment
from ourblog.forms import BlogForm, RegistrationForm, CommentForm, BloggerForm
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.utils import timezone
from django.template.context_processors import csrf
from django.core.paginator import Paginator, EmptyPage, Page
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user
# Create your views here.

def home(request):
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 2)
    page = request.GET.get("page")
    blogs = paginator.get_page(page)
    context = {"blogs":blogs}
    template = "home.html"
    return render(request, template, context)

def blog(request, id):
    blog = Blog.objects.get(id=id)
    context = {"blog":blog}
    template = "individual_blog.html"
    return render_to_response(template, context)

def create_blogger(request):
    if request.POST:
        form = BloggerForm(request.POST)
        if form.is_valid():
			#form.id = user.id
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = BloggerForm()
    args = {}
    args.update(csrf(request))
    args["form"] = form
    return render_to_response("create_blogger.html", args)

def create_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")

    else:
        #data = {"publish_date":timezone.now()}
        form = BlogForm()
        args = {}
        args.update(csrf(request))
        args["form"] = form
        return render_to_response("create_blog.html", args)
    #user = auth.get_user(request)
    #print(auth.get_user(request), "1")
    #if user.is_authenticated:
    #if request.POST:
        #data = {"publish_date":timezone.now()}
    #    form = BlogForm(request.POST)
    #    if form.is_valid():
            #form.publish_date = timezone.now()
    #        form.save()
    #        return HttpResponseRedirect("/")
    #else:
    #    form = BlogForm()
    #args = {"publish_date":timezone.now()}
    #args.update(csrf(request))
    #args["form"] = form
    #return render_to_response("create_blog.html", args)

def like_blog(request, id):
    if id:
        blog = Blog.objects.get(id=id)
        count = blog.likes
        count += 1
        blog.likes = count
        blog.save()

    return HttpResponseRedirect("blog/%s" % id)

def add_comment(request, id):
    blog = Blog.objects.get(id=id)
    if request.method == "POST":
        f = CommentForm(request.POST)
        if f.is_valid():
            comment = f.save(commit=False)
            comment.publish_date = timezone.now()
            comment = blog
            comment.save()
            #return render_to_response(template_name="individual_blog.html", context={"blog": Blog.objects.get(id=id)})
            return HttpResponseRedirect("/blog/%s" % id)

    else:
        f = CommentForm()

        args = {}
        args.update(csrf(request))

        args["blog"] = blog
        args["form"] = f

        return render_to_response("add_comment.html", args)

def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response("account/login.html", c)

def auth_view(request):
    username = request.POST.get("username", "")
    password = request.POST.get("password", "")
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect("/account/loggedin")
    else:
        return HttpResponseRedirect("/account/invalid")

def loggedin(request):
    return render_to_response("account/loggedin.html", {"full_name":request.user.username})

def invalid_login(request):
    return render_to_response("account/invalid_login.html")

def logout(request):
    auth.logout(request)
    return render_to_response("home.html")

def register_user(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/account/register_success")

    else:
        form = RegistrationForm()
        args = {}
        args.update(csrf(request))

        args["form"] = form
        return render_to_response("account/register.html", args)

def register_success(request):
    return render_to_response("account/register_success.html")
