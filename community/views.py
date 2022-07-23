from django.shortcuts import render, redirect
from .models import Issue, Room
from .forms import RoomForm, RegisterForm
from django.contrib.auth import login
# Create your views here.
def community_main(request):
    issues = Issue.objects.all()
    rooms = Room.objects.all()
    context = {'issues':issues, 'rooms':rooms}
    return render(request, 'community/issue.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    rooms = Room.objects.all()
    context = {'room':room, 'rooms':rooms}
    return render(request, 'community/room.html', context)

def createRoom(request):
    form = RoomForm()
    rooms = Room.objects.all()
    context = {'form': form, 'rooms':rooms}
    return render(request, 'community/roomForm.html', context)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        password = request.POST.get("UserPW")
        confirm_pw = request.POST.get("ReUserPW")
        if form.is_valid() and password == confirm_pw:
            user = form.save(commit=False)
            user.save()
            return redirect('community_main')
    else:
        form = RegisterForm()
    return render(request, 'community/register.html', {'form':form})
