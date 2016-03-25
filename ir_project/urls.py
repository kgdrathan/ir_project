from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ir_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^timeline/', include('timeline.urls', namespace="timeline")),
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# urlpatterns = [
#     url(r'^polls/', include('polls.urls')),
#     url(r'^admin/', admin.site.urls),
# ]