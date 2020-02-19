from django.shortcuts import render
from django.http import  HttpResponseRedirect
from django.contrib.auth.decorators import login_required

@login_required
def posts(request):
    print(request.user.is_authenticated)
    return render(request, 'posts/homepage.html')

