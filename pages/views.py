from django.shortcuts import render
# Create your views here.
from django.views.generic import TemplateView

class HomePageView(TemplateView): #instead of def we create class "classes should be capitalized"
 template_name = "home.html"
#the TemplateView is a class-based view that is used to render a template
class AboutPageView(TemplateView): 
 template_name = "about.html"

'''
from django.http import HttpResponse
def homePageView(request):
    return HttpResponse("Hello, World!")'''