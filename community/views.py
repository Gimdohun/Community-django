from django.shortcuts import render, redirect
from .models import Issue, Room
from .forms import RoomForm
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
    rooms = Room.objects.all()
    form = RoomForm()
    context = {'form': form, 'rooms': rooms}
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('community_main')
    return render(request, 'community/roomForm.html', context)

def deleteRoom(request, pk):
    rooms = Room.objects.all()
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('community_main')
    context = {'rooms':rooms, 'room':room}
    return render(request, 'community/deleteRoom.html', context)

def updateRoom(request, pk):
    rooms = Room.objects.all()
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('community_main')
    context = {'rooms':rooms, 'room':room, 'form':form}
    return render(request, 'community/roomForm.html', context)

