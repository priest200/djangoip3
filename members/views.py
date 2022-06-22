from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *


@login_required(login_url='login-user/')
def index(request):
    project = Project.objects.get(id=4)
    rating = Prorating.objects.get(pro_name=project)

    if request.method == "POST":
        search_value = request.POST.get("search")
        projects = Project.objects.filter(name__contains=search_value)
        if len(projects) == 0:
            messages.success(request, "No results found!")
    else:
        projects = Project.objects.all()
    return render(request, 'html/index.html', {'projects': projects, "project": project, 'rating': rating})


@login_required(login_url='login-user/')
def submit_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            prorating = Prorating()
            prorating.pro_name = project
            prorating.save()
            messages.success(request, "Project was submitted successful")
            return redirect('index-page')
    else:
        form = ProjectForm()
        return render(request, 'html/project-form.html', {'form': form})

    return render(request, 'html/project-form.html', {'form': form})


@login_required(login_url='login-user/')
def rate_project(request, id):
    project = Project.objects.get(id=id)
    if request.method == "POST":
        form = RateForm(request.POST)

        if form.is_valid():
            pro = Prorating.objects.get(pro_name=project)

            if int(form['design'].value()) > 10 or int(form['design'].value()) < 0:
                messages.success(request, "Design cannot be less than 0 or greater than 10 ")
            elif int(form['usability'].value()) > 10 or int(form['usability'].value()) < 0:
                messages.success(request, "Usability cannot be less than 0 or greater than 10 ")
            elif int(form['content'].value()) > 10 or int(form['content'].value()) < 0:
                messages.success(request, "Content cannot be less than 0 or greater than 10 ")
            else:
                pro.count = pro.count + 1
                pro.design = (int(pro.design) + int(form['design'].value())) / 2
                pro.usability = (int(pro.usability) + int(form['usability'].value())) / 2
                pro.content = (int(pro.content) + int(form['content'].value())) / 2
                project.rating = (project.rating + (
                    int(int(form['design'].value()) + int(form['usability'].value()) + int(
                        form['content'].value()))) / 3) / 2
                pro.save()
                project.save()
                messages.success(request, "Project was rated/reviewed successful")

    else:
        form = RateForm()
    return render(request, 'html/project-page.html', {"project": project, 'form': form})


@login_required(login_url='login-user/')
def post_comment(request, id):
    project = Project.objects.get(id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.pro_name = project
            comment.commenter = request.user
            comment.save()
    else:
        form = RateForm()
    return render(request, 'html/project-page.html', {"project": project, 'form': form})


@login_required(login_url='login-user/')
def view_project(request, id):
    project = Project.objects.get(id=id)
    comments = Comment.objects.filter(pro_name=project)
    rating = Prorating.objects.get(pro_name=project)
    form = RateForm()
    c_form = CommentForm()
    rate_project(request, id)
    post_comment(request, id)
    return render(request, 'html/project-page.html',
                  {"project": project, "form": form, "c_form": c_form, "comments": comments, "rating": rating})


@login_required(login_url='login-user/')
def my_profile(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    projects = Project.objects.filter(user=user)
    if request.method == "POST":
        username = request.POST.get('username')
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        profile.profile_pic = request.FILES['profile_pic']
        profile.caption = request.POST.get("bio")

        user = User.objects.filter(username=user.username).update(username=username, first_name=fullname, email=email)
        profile.save()
    return render(request, 'html/profile.html', {"profile": profile, "projects": projects})


def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile()
            profile.user = user
            profile.save()
            login(request, user)
            messages.success(request, "Account created successfully")
            return redirect('index-page')
        else:
            for error in form.error_messages:
                messages.error(request, form.error_messages[error])
                print(error)
                return render(request, 'html/register.html', {"form": form})
    else:
        form = RegisterForm()
    return render(request, 'html/register.html', {"form": form})


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index-page')
        else:
            messages.error(request, "Invalid username or password")
            return render(request, 'html/login.html', {})

    return render(request, 'html/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "successfully logged out")
    return redirect('login-user')


@api_view(["GET"])
def project_list(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def user_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)
