
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from todolist.models import Task
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import TaskList
# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    
    data_todolist = Task.objects.filter(user=request.user)
    context = {
        'data_todolist': data_todolist,
        'nama': 'Nanda Tristan Ardiansyah',
        'npm' : '2106752086',
        'last_login' : request.COOKIES['last_login'],
    }
    
    return render(request, "todolist.html",context)


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
def create_task(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TaskList(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required

            inputtitle = form.cleaned_data['titleField']
            inputdescription = form.cleaned_data['descriptionField']
            
            task = Task(user=request.user,title= inputtitle ,description=inputdescription, )
            task.save()
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/todolist/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TaskList()

    return render(request, 'create-task.html', {'form': form})

def delete_task(request, pk):
    item = Task.objects.filter(pk=pk)
    item.delete()
    return HttpResponseRedirect('/todolist/')

def change_status(request, pk):
    thisitem = Task.objects.get(id=pk)
    if thisitem.isFinished == False:
        thisitem.isFinished = True
    else:
        thisitem.isFinished = False
    thisitem.save()
    return HttpResponseRedirect('/todolist/')