from django.shortcuts import render_to_response

def home(request):
	arr = ['bar1', 'bar2', 'bar3']
	variable = 'foo'
	return render_to_response("home.html", locals())