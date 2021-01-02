from django.shortcuts import render,redirect
from .forms import*
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def Index(request):
	x=ulogin()

	if request.method == 'POST':
		unm=request.POST.get('Username')
		pwd=request.POST.get('Password')

		user = authenticate(request,username=unm,password=pwd)

		if user is not None:
			login(request, user)
			messages.success(request, 'Login successfully for '+unm+' !!!')
			return redirect('Home',unm)
		else:
			messages.info(request,'Username and Password Incorrect !!!')

	xcontext={'user':x}
	return render(request,'login.html',xcontext)

def Register(request):	
	xuser=CreateUserForm()
	yuser=ProfileForm()
	
	if request.method == 'POST':
		xuser=CreateUserForm(request.POST)
		yuser=ProfileForm(request.POST)
		if xuser.is_valid() and yuser.is_valid():
			mx= xuser.save()
			userx = xuser.cleaned_data.get('username')
			yuser= yuser.save(commit=False)
			yuser.muser=mx
			yuser.save()
			messages.success(request, 'Account was created successfully for '+userx+' !!!')
			return redirect('login')

	xcontext={'user':xuser,'yuser':yuser}		
	return render(request,'Register.html',xcontext)

login_required(login_url='login')
def Home(request,pk):
	userdata= User.objects.get(username=pk)
	context={'userdata':userdata}
	return render(request,'Home.html',context)

def logout(request):
	# logout(request)
	return redirect('login')


