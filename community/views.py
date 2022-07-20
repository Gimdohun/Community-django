from django.shortcuts import render
from .models import Community
# Create your views here.
def community_main(request):
    issues = Community.objects.all()
    return render(request, 'community/home.html', {'issues':issues})