from django.shortcuts import render

# Create your views here.
def restaurant(request):
	context = {
	'msg' : 'Hello World!'
	}
	return render(request, "task02.html", context)