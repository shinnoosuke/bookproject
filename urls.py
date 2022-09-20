from django. contrib import admin
from django.ulrs import path, include


urlpatterns=[
    path('admin/',admin.site.urls),
    path('', include('book.urls')),
]