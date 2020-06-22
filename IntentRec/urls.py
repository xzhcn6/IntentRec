"""IntentRec URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from . import view
from . import search

urlpatterns = [
    path('admin/', admin.site.urls),
	url(r'^$', view.Index, name='index'),
	url(r'^about/', view.About, name='about'),
	url(r'^showModel/', view.ShowModel, name='showModel'),
	url(r'^uploadData/', view.UploadData, name='uploadData'),
	url(r'^search-post$', search.search_post, name='search-post'),
	url(r'^recognition$', view.Recognition, name='recognition'),
	url(r'^add-intent$', search.add_intent, name='add-intent'),
	url(r'^getVerificationCode$', search.getVerificationCode, name='getVerificationCode'),
]
 
