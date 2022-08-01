from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from userdb.forms import RegisterForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if form.is_valid() and password1 == password2:
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, passoword=raw_password)
            login(request,user)
            return redirect('community:community_main')
    else:
        form = RegisterForm()
    return render(request, 'userdb/register.html', {'form':form})