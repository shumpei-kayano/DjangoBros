
from django.contrib import admin
from django.urls import path, include #includeを追記

urlpatterns = [
    path('admin/', admin.site.urls),
    #アプリのurls.pyを参照するようにする
    path('', include('blogs.urls')),
]
