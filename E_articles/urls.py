from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^en_all/$', 'E_articles.views.en_articles'),
    url(r'^en_get/(?P<en_article_id>\d+)/$', 'E_articles.views.en_article'),
    url(r'^en_create/$', 'E_articles.views.en_create'),
    url(r'^en_like/(?P<en_article_id>\d+)/$', 'E_articles.views.en_like_article'),
    url(r'^en_add_comment/(?P<en_article_id>\d+)/$', 'E_articles.views.en_add_comment'),
    url(r'^en_delete_comment/(?P<en_comment_id>\d+)/$', 'E_articles.views.en_delete_comment'),
    url(r'^en_add_commentsecond/(?P<en_article_id>\d+)/$', 'E_articles.views.en_add_commentsecond'),
    url(r'^en_delete_commentsecond/(?P<en_article_id>\d+)/$', 'E_articles.views.en_delete_commentsecond'),

)
