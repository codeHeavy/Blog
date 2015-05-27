from django.shortcuts import render
from django.http import HttpResponse
from .forms import AddForm
from .models import BlogPost
# Create your views here.

def home_view(request):
	send_dict = {}
	send_dict['posts'] = BlogPost.objects.filter(post__contains="college").order_by("-id")
	return render(request,"home.html",send_dict)
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
	bp = BlogPost()
	form = AddForm()
	#title = "Enter title"
	#post = "Enter the post"
	
	if request.POST:
		form = AddForm(request.POST)
		if form.is_valid():
			form = AddForm(request.POST)
			#bp.title = form.cleaned_data['title']
			#bp.post = form.cleaned_data['post']
			#bp.user = form.cleaned_data['user']
			#bp.save()
			form.save()
			#print title,"\n",post,'\n',user
			#print "\n the form is valid"
		else:
			print "\n the form is invalid"		
	send_dict["value"] = form
	#send_dict["title"] = title
	#send_dict["post"] = post
	return render(request,"add.html",send_dict)