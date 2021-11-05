from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm , UserUpdateForm , ProfileUpdateForm

# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)   #if request is POST then we will validate it as it will contain data
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request , 'Account created for {}.You can log in now!'.format(username))   #flasing a success message on account creation
            return redirect('login')   #redirecting to blog home page 

            #to flash our msg on screen upon user sign up we will include the message block in base.html of blog_app
            #so that even if we are redirected anywhere our flash msg can be seen there only

    else:
        form = UserRegistrationForm()   
    return render(request , 'blog_users_app/register.html' , {'form' : form})


@login_required #this is a decorator-> it adds extra functionality to our function 
def profile(request):

    #now check whether these forms are valid or not

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST , instance = request.user)
        p_form = ProfileUpdateForm(request.POST ,
                                    request.FILES ,  
                                    instance = request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            messages.success(request , 'Account updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)



    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }

    return render(request ,'blog_users_app/profile.html' , context)