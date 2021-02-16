from django.shortcuts import render

def home(request):
	return render(request, 'home.html', {})


def celebritygrid01(request):
	return render(request, 'celebritygrid01.html', {})

def celebritygrid02(request):
	return render(request, 'celebritygrid02.html', {})

def celebritysingle(request):
	return render(request, 'celebritysingle.html', {})

def celebritylist(request):
	return render(request, 'celebritylist.html', {})

def error(request):
	return render(request, '404.html', {})