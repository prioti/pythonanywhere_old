from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^hello/$', 'prioti.article.views.hello'),
    url(r'^all/$', 'prioti.article.views.articles'),
    url(r'^get/(?P<article_id>\d+)$', 'prioti.article.views.article'),
    url(r'^language/(?P<language>[a-z\-]+)$', 'prioti.article.views.language'),
    url(r'^create/$', 'prioti.article.views.create'),
    # Examples:
    # url(r'^$', 'prioti.views.home', name='home'),
    # url(r'^prioti/', include('prioti.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
