"""logistics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('about-us',views.about,name='about'),
    path('services',views.services,name='services'),
    path('pricing',views.pricing,name='pricing'),
    path('contact-us',views.contact,name='contact'),
    path('get-quote',views.quote,name='quote'),
    path('service-detail',views.service_detail,name='service-detail'),
    path('service/cargo/',views.cargo,name='cargo'),
    path('service/logistics/',views.logistics,name='logistics'),
    path('service/packaging/',views.packaging,name='packaging'),
    path('service/trucking/',views.trucking,name='trucking'),
    path('service/warehousing/',views.warehousing,name='warehousing'),
    path('privacy-policy',views.privacy,name='privacy'),
]
