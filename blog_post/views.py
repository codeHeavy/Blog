from django.shortcuts import render
from django.http import HttpResponse
from forms import AddForm
# Create your views here.

def home_view(request):
	return render(request,"home.html")
	#return HttpResponse(int(num1) + int(num2))
	
def sum_view(request):
	num1 = request.GET.get("num1")
	num2 = request.GET.get("num2")
	
	if num1 and num2:
		s = int(num1) + int(num2)
	else:
		s = "Addition cannot be performed"
	sum = {
		"value": s
	}
	return render(request,"sum.html",sum)
	
def form_sum_view(request):
	num1 = request.POST.get("num1")
	num2 = request.POST.get("num2")
	
	if num1 and num2:
		s = int(num1) + int(num2)
	else:
		s = "Addition cannot be performed"
	sum = {
		"value": s,
	}
	return render(request,"form.html",sum)
	
def django_form_view(request):
	send_dict = {}
	form = AddForm()
	title = "Enter title"
	post = "Enter the post"
	if request.POST:
		form = AddForm(request.POST)
		if form.is_valid():
			title = form.cleaned_data['title']
			post = form.cleaned_data['post']
			print title,"\n",post
			#print "\n the form is valid"
		else:
			print "\n the form is invalid"		
	send_dict["value"] = form
	send_dict["title"] = title
	send_dict["post"] = post
	return render(request,"forms2.html",send_dict)