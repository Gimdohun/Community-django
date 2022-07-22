from django.shortcuts import render
from .models import Issue, Room
from .forms import RoomForm
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