"""
URL configuration for movie project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from online import views
from django.conf import settings
from django.conf.urls.static import static
app_name='online'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.MovieList.as_view(),name='home'),
    path('insertion',views.MovieAdd.as_view(),name='insertion'),
    # path('more/<p>',views.more,name='more'),
    path('h/<pk>',views.MovieDetail.as_view(),name='more'),
    path('update/<pk>', views.MovieUpdate.as_view(), name='update'),
    path('delete/<pk>', views.MovieDelete.as_view(), name='delete'),

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
