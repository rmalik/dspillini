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

# DeadlineExceededError can live in two different places
# TODO(guido): simplify once this is fixed.
try:
  # When deployed
  from google.appengine.runtime import DeadlineExceededError
except ImportError:
  # In the development server
  from google.appengine.runtime.apiproxy_errors import DeadlineExceededError

# Django imports
# TODO(guido): Don't import classes/functions directly.
from django import forms
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponseForbidden, HttpResponseNotFound
from django.shortcuts import render_to_response
import django.template
from django.utils import simplejson

def entry_detail(request):
	pass

def archive_day(request):
	pass

def archive_month(request):
	pass

def archive_year(request):
	pass

def archive_index(request):
	
	return render_to_response('base.html')
