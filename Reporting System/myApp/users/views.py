from django.shortcuts import render
from django.contrib.auth import logout 
import os
from .models import Profile,MaintenanceRequest
from django.utils import timezone 


def home(request):
 return render(request,"Users/index.html")

def login(request):
 return render(request,"Users/login.html")

def signup(request):
 return render(request,"Users/signup.html")
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages

def home(request):
    return render(request, "Users/index.html")

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password)
        print(f"Username: {username}, Password: {password}")  # Debugging line
        print(f"User found: {user is not None}")  # Debugging line

        if user is not None:
            auth_login(request, user)
            messages.success(request, "Welcome back!")
            return redirect('landing')  
        else:
            messages.error(request, "Invalid username or password.")
    
    return render(request, "Users/login.html")

def signup(request):
    if request.method == "POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        unit_number = request.POST.get("unit_number")
        phone_number = request.POST.get("phone_number")

        if password == confirm_password:
            try:
                user = User.objects.create_user(
                    username=username,
                    first_name=firstname,
                    last_name=lastname,
                    email=email,
                    password=password
                )
                user.save()

                # Assuming you have a Profile model to save unit number and phone number
                Profile.objects.create(user=user, unit_number=unit_number, phone_number=phone_number)

                messages.success(request, "Account created successfully! You can now log in.")
                return redirect('login') 
            except Exception as e:
                messages.error(request, f"Error creating account: {e}")
        else:
            messages.error(request, "Passwords do not match.")
    
    return render(request, "Users/signup.html")

def landing(request):
    maintenance_requests = MaintenanceRequest.objects.filter(user=request.user)
    return render(request, "Users/landing.html", {'maintenance_requests': maintenance_requests})

def userInfo(request):
    user = request.user  
    
    
    user_data = {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'unit_number': user.profile.unit_number if hasattr(user, 'profile') else None,
        'phone_number': user.profile.phone_number if hasattr(user, 'profile') else None,
    }
    
    return render(request, "Users/userInfo.html", {'user': user_data})

def update_user_info(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('firstname')
        user.last_name = request.POST.get('lastname')
        user.email = request.POST.get('email')

        # Update phone number and unit number if they exist in the profile
        if hasattr(user, 'profile'):
            user.profile.phone_number = request.POST.get('phone_number')
            user.profile.save()
        
        user.save()
        messages.success(request, "Your information has been updated successfully!")
        return redirect('user_info')  # Redirect to the user info page

    return redirect('user_info')  # Handle other methods


def submit_maintenance_request(request):
    if request.method == "POST":
        block_number = request.POST.get('block-number')
        room_number = request.POST.get('room-number')
        unit_type = request.POST.get('unit-type')
        issue_description = request.POST.get('issue-description')
        attachment = request.FILES.get('attachment')  # Optional attachment

        # Create a new MaintenanceRequest instance
        MaintenanceRequest.objects.create(
            user=request.user,
            block_number=block_number,
            room_number=room_number,
            unit_type=unit_type,
            issue_description=issue_description,
            attachment=attachment,  # This can be None if no file is uploaded
            unit_number=request.user.profile.unit_number,  # Get the user's unit number from their profile
            status='Pending',  # Set default status to Pending
            created_at=timezone.now()  # Record the current date and time
        )

        messages.success(request, "Maintenance request submitted successfully!")
        return redirect('landing')  # Redirect to landing or another page

    return render(request, "Users/logSubmit.html") 



def signout(request):
    logout(request)
    messages.success(request,"Successfully Logout")
    return redirect('home')

def landing(request):
    user = request.user
    # Fetch all maintenance requests for the logged-in user
    maintenance_requests = MaintenanceRequest.objects.filter(user=user)

    return render(request, "Users/landing.html", {'maintenance_requests': maintenance_requests})