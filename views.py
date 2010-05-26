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
from dateutil.parser import parse
from gdata.calendar.service import CalendarEventQuery, CalendarService
from blog.models import Entry


def login_required(func):
	"""Decorator that redirects to the login page if you're not logged in."""
	def login_wrapper(request, *args, **kwds):
		if users.get_current_user() is None:
			return HttpResponseRedirect(users.create_login_url(request.get_full_path().encode('utf-8')))
		return func(request, *args, **kwds)
	return login_wrapper

def fetch_events():
	username = 'illinideltasigs.org_j8s041ukg9akrei34tan8smri0@group.calendar.google.com'
	visibility = 'private-fa3dc4aa8a14f7da0099eb6fb34a036a'
	query = CalendarEventQuery(username, visibility)
	query.sortorder = 'a'
	query.futureevents = 'true'
	query.orderby = 'starttime'
	calendar_service = CalendarService()
	feed = calendar_service.CalendarQuery(query)
	return [{'title':item.title.text, 'start_time':parse(item.when[0].start_time), 'end_time':parse(item.when[0].end_time), 'location':item.where[0].value_string} for item in feed.entry]


def home(request):
	entries = Entry.all()
	entries.order('-published')
	entries.fetch(limit=5)
	events = fetch_events()
	return render_to_response('home.html', {'events': events[0:5], 'entries':entries})
	
def scholarship(request):
	return render_to_response('scholarship.html')
	
def costs(request):
	return render_to_response('costs.html')
	
def concerns(request):
	return render_to_response('concerns.html')

def schedule_visit(request):
	return render_to_response('schedule_visit.html')
	
def join_us(request):
	return render_to_response('how_to_join.html')
	
def carillon_archive(request):
	return render_to_response('carillon_archive.html')
