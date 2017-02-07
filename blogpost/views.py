from django.shortcuts import render,render_to_response,get_object_or_404
from blogpost.models import Bolgpost

# Create your views here.
def index(request):
    return render_to_response('index.html',{'posts':Bolgpost.objects.all()[:5]})