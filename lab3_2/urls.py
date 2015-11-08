from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lab3_2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$','books.views.home'),
    url(r'searchbook/','books.views.searchbook'),
    url(r'bookinformation/','books.views.bookinformation'),
    url(r'^deletebook/','books.views.deletebook'),
    url(r'^afteraddbook/','books.views.afteraddbook'),
    url(r'^addbook/','books.views.addbook'),
    url(r'^afteraddauthor/','books.views.afteraddauthor'),
    url(r'^updatebook/','books.views.updatebook'),
)
