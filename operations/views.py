from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import student, department
from .forms import StudentForm ,departmentForm
from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse

## Superuser: admin
# ## Password: admin
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

# @login_required(login_url='loginuser')
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

@login_required(login_url='loginuser')
def logoutUser(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('loginuser')

@login_required(login_url='loginuser')
def home(request):
    students = student.objects.all()
    depart = department.objects.all()
    return render(request, 'operations/home.html', {'students': students,'department':depart})

@login_required(login_url='loginuser')
def student_create(request):
    form = StudentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            department_id = form.cleaned_data.get('department')
            if not department_id:
                messages.error(request, "Please select a department!")
                return render(request, 'operations/student_form.html', {'form': form})
            
            try:
                department.objects.get(id=department_id.id)
                student = form.save()
                messages.success(request, "Student added successfully!")
                return redirect('home')
            except department.DoesNotExist:
                messages.error(request, "Selected department does not exist!")
                return render(request, 'operations/student_form.html', {'form': form})
    
    return render(request, 'operations/student_form.html', {'form': form})

@login_required(login_url='loginuser')
def student_update(request, pk):
    stud = get_object_or_404(student, pk=pk)
    form = StudentForm(request.POST or None, instance=stud)
    if form.is_valid():
        form.save()
        messages.success(request, "Student updated successfully!")
        return redirect('home')
    return render(request, 'operations/student_form.html', {'form': form})

@login_required(login_url='loginuser')
def student_delete(request, pk):
    stud = get_object_or_404(student, pk=pk)
    if request.method == "POST":
        stud.delete()
        messages.success(request, "Student deleted successfully!")
    #     return redirect('home')
    # else:
    #     messages.error(request, 'Something went wrong. Please try again.')
        students = student.objects.all()
    depart = department.objects.all()
    return render(request, 'operations/home.html', {'students': students,'department':depart})

@login_required(login_url='loginuser')
def departmentAdd(request):
    if request.method == 'POST':
        form = departmentForm(request.POST)
        if form.is_valid():
            department_name = form.cleaned_data['name']
            if department.objects.filter(name__iexact=department_name).exists():
                messages.error(request, "Department with this name already exists!")
                return render(request, 'operations/add_department.html', {'form': form})

            form.save()
            messages.success(request, "Department added successfully!")
            return redirect('home')  # or wherever you want to redirect
    else:
        form = departmentForm()
    return render(request, 'operations/add_department.html', {'form': form})