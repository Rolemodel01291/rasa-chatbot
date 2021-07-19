from django.contrib import admin
from django.urls import include,path

from .views import index_view

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('chat/', include('chat.urls')),
    path('', include('chat.urls')),
]
