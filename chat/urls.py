# from django.conf.urls import patterns, include, url
# from django.contrib import admin
from chat.views import index_view, get_garan
from django.urls import include,path
# admin.autodiscover()


urlpatterns = [
    path('', index_view, name='chat_index'),
    path('get_garan/', get_garan, name='get_garan'),

]