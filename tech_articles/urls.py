from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^t_all/$', 'tech_articles.views.t_articles'),
    url(r'^t_get/(?P<t_article_id>\d+)/$', 'tech_articles.views.t_articles'),

)
