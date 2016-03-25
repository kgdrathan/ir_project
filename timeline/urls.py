from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.home, name = 'home'),
    url(r'^get_result$', views.get_result, name = 'get_result'),
    url(r'^admin/', admin.site.urls),
]

# urlpatterns = [
#     url(r'^$', views.index, name='index'),
# ]
