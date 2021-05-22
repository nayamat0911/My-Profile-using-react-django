from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from Profile import views

urlpatterns = [
    path ('',views.home, name='home'),
    path('admin/', admin.site.urls),
    path('api/',include('Profile.urls')),
    re_path(r'^.*', TemplateView.as_view(template_name='index.html'))
]

