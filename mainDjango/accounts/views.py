from django.shortcuts import render_to_response,render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf #protect against csrf
from django.contrib.auth.forms import UserCreationForm
from forms import MyRegistrationForm
from django.http import HttpResponse
#for profile
from forms import UserProfileForm
from django.contrib.auth.decorators import login_required

def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/loggedin')
    c ={}
    c.update(csrf(request))
    return render_to_response('accounts/login.html',c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')
 
@login_required   
def loggedin(request):
    return render_to_response('dashboard.html', 
                              {'full_name': request.user.username})

def invalid_login(request):
    return render_to_response('accounts/invalid_login.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

def register_user(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')
        
    else:
        form = MyRegistrationForm()
    args = {}
    args.update(csrf(request))
    
    args['form'] = form
    
    return render_to_response('accounts/register.html', args)

def register_success(request):
    return render_to_response('accounts/register_success.html')

@login_required
def user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/loggedin')
    else:
        user = request.user
        profile = user.profile
        form = UserProfileForm(instance=profile)
        
    args = {}
    args.update(csrf(request))
    
    args['form'] = form
    
    return render_to_response('accounts/profile_update.html', args)   


def profile(request):
    if request.user.is_authenticated():
        user = request.user
        profile = user.profile
        args = {}
        args['form'] = profile
        args['fullname'] = request.user.username
        args['email'] = request.user.email
        return render_to_response('accounts/profile.html', args)   
    else:
        return HttpResponseRedirect('/accounts/login')