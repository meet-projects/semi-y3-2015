from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'app/index.html', {})
def home(request):
	return render(request, 'app/home.html', {})
def signup(request):
	return render(request, 'app/signup.html', {})
def login(request):
	return render(request, 'app/login.html', {})
