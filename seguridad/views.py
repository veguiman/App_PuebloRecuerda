from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

# Create your views here.

def authlogin(request):

	if request.method == 'POST':
		action = request.POST.get('action', None)
		username = request.POST.get('username', None)
		password = request.POST.get('password', None)
		template = ""

		if action == 'singup':
			user = User.objects.create_user(username = username,
											password = password,
											) 
			user.save()
		
		elif action == 'login':
			user = authenticate(username = username,
								password = password,
								)
			login(request,user,)
		
		return redirect('/')

	return render(request, template, {},)

