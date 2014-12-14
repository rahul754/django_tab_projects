from django.conf.urls import patterns, include, url
from article.views import articles
#from article.views import index
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^accounts/', include('userprofile.urls')),
    (r'^articles/',include('article.urls')),
    url(r'^$', 'article.views.index'),    
    url(r'^p_articles/',include('poli_articles.urls')),
    url(r'^e_articles/',include('edu_articles.urls')),
    url(r'^en_articles/',include('E_articles.urls')),
    url(r'^s_articles/',include('sci_articles.urls')),




    # user auth urls
    url(r'^accounts/login/$',  'django_test.views.login'),
    url(r'^accounts/auth/$',  'django_test.views.auth_view'),    
    url(r'^accounts/logout/$', 'django_test.views.logout'),
    url(r'^accounts/loggedin/$', 'django_test.views.loggedin'),
    url(r'^accounts/invalid/$', 'django_test.views.invalid_login'),  
    url(r'^accounts/register/$', 'django_test.views.register_user'),
    url(r'^accounts/register_success/$', 'django_test.views.register_success'),

   

    url(r'^admin/', include(admin.site.urls)),

)
