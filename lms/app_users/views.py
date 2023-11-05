from django.shortcuts import render, redirect
from app_users.forms import UserForm, UserProfileInfoForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from curriculum.models import Standard
from .models import UserProfileInfo
from django.contrib.auth.models import User


# Create your views here.
# def index(request) :
#     return HttpResponse(request,'home.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(f'Username: {username}, Password: {password}')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT IS DEACTIVATED")
        else:
            # return HttpResponse("Please use correct id and password")
            return HttpResponseRedirect(reverse('register'))

    else:
        return render(request, 'app_users/login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

# Create your views here.
# def index(request):
#     return render(request,'home.html')
    

def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            # user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'app_users/register.html',
                            {'registered':registered,
                             'user_form':user_form,
                             'profile_form':profile_form})

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        standards = Standard.objects.all()
        teachers = UserProfileInfo.objects.filter(user_type='teacher')
        user_profile = UserProfileInfo.objects.get(user=self.request.user)
        context['standards'] = standards
        context['teachers'] = teachers
        context['user_profile'] = user_profile

        return context


@login_required
def view_profile(request, username):
    user = User.objects.get(username=username)
    user_profile = UserProfileInfo.objects.get(user=user)
    return render(request, 'app_users/view_profile.html', {'user_profile': user_profile})

@login_required
def update_profile(request):
    if request.method == "POST":
        form = UserProfileInfoForm(request.POST, request.FILES, instance=request.user.userprofileinfo)

        if form.is_valid():
            form.save()
            return redirect(reverse('view_profile', kwargs={'username': request.user.username}))
    else:
        form = UserProfileInfoForm(instance=request.user.userprofileinfo)

    return render(request, 'app_users/update_profile.html', {'form': form})


