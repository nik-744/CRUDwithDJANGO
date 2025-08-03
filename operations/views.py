from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import student
from .forms import StudentForm 
# from django.http import HttpResponse

## Superuser: admin
## Password: admin

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f"Username: {username}, Password: {password}")  # Debugging line
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('loginuser')
    return render(request, 'operations/login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return render(request, "operations/signup.html", {'error': 'Username already exists'})
        user = User.objects.create_user(username=username, password=password)
        messages.success(request, 'Signup successful! You can now log in.')
    return render(request,"operations/signup.html")

def logoutUser(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('loginuser')

def home(request):
    students = student.objects.all()
    return render(request, 'operations/home.html', {'students': students})

def student_create(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Student added successfully!")
        return redirect('home')
    return render(request, 'operations/student_form.html', {'form': form})

def student_update(request, pk):
    stud = get_object_or_404(student, pk=pk)
    form = StudentForm(request.POST or None, instance=stud)
    if form.is_valid():
        form.save()
        messages.success(request, "Student updated successfully!")
        return redirect('home')
    return render(request, 'operations/student_form.html', {'form': form})

def student_delete(request, pk):
    stud = get_object_or_404(student, pk=pk)
    if request.method == "POST":
        stud.delete()
        messages.success(request, "Student deleted successfully!")
    #     return redirect('home')
    # else:
    #     messages.error(request, 'Something went wrong. Please try again.')
    return render(request, 'operations/home.html', {'student': student})