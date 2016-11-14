from django.shortcuts import render_to_response,render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf #protect against csrf
from django.http import HttpResponse
from django.template import RequestContext

def homepage(request):
    return render_to_response('homepage.html',context_instance = RequestContext(request))

def tourpage(request):
    return render_to_response('tourpage.html',context_instance = RequestContext(request))