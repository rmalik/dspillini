# Python imports
import os
import cgi
import random
import re
import logging
import binascii
import datetime
import urllib
import md5
from xml.etree import ElementTree
from cStringIO import StringIO

# AppEngine imports
from google.appengine.api import mail
from google.appengine.api import memcache
from google.appengine.api import users
from google.appengine.api import urlfetch
from google.appengine.ext import db
from google.appengine.ext.db import djangoforms
try:
  from google.appengine.runtime import DeadlineExceededError
except ImportError:
  from google.appengine.runtime.apiproxy_errors import DeadlineExceededError

# Django imports
from django import forms
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponseForbidden, HttpResponseNotFound
from django.shortcuts import render_to_response
import django.template
from django.utils import simplejson

from blog.models import Entry

def login_required(func):
	"""Decorator that redirects to the login page if you're not logged in."""
	def login_wrapper(request, *args, **kwds):
		if users.get_current_user() is None:
			return HttpResponseRedirect(users.create_login_url(request.get_full_path().encode('utf-8')))
		return func(request, *args, **kwds)
	return login_wrapper


def entry_detail(request):
	return render_to_response('base.html')

def archive_day(request):
	return render_to_response('base.html')

def archive_month(request):
	return render_to_response('base.html')

def archive_year(request):
	return render_to_response('base.html')

def archive_index(request):
	entries = Entry.all()
	entries.order('-published')
	entries.fetch(limit=5)
	return render_to_response('base.html')#, {'entries': entries, 'events': events})

@login_required
def create(request):
	if request.is_ajax():
		e = Entry(title=request.POST['title'],
				  body=request.POST['editor_data'],
				  author = users.get_current_user())
		e.put()
		return archive_index(request)
	else:
		return render_to_response('blog/create.html')

def update(request):
	"""docstring for update"""
	pass
	
def delete(request):
	pass