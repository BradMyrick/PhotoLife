from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from . import views

# Uncomment next two lines to enable admin:
#from django.contrib import admin
#from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('notifications/', views.notifications, name='notifications'),
    path('explore/', views.explore, name='explore'),
    path('signup/', views.signup, name='signup'),
    # Uncomment the next line to enable the admin:
    #path('admin/', admin.site.urls)
]
