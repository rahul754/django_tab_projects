from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^e_all/$', 'edu_articles.views.e_articles'),
    url(r'^e_get/(?P<e_article_id>\d+)/$', 'edu_articles.views.e_article'),
    url(r'^e_create/$', 'edu_articles.views.e_create'),
    url(r'^e_like/(?P<e_article_id>\d+)/$', 'edu_articles.views.e_like_article'),
    url(r'^e_add_comment/(?P<e_article_id>\d+)/$', 'edu_articles.views.e_add_comment'),
    url(r'^e_delete_comment/(?P<e_comment_id>\d+)/$', 'edu_articles.views.e_delete_comment'),
    url(r'^e_add_commentsecond/(?P<e_article_id>\d+)/$', 'edu_articles.views.e_add_commentsecond'),
    url(r'^e_delete_commentsecond/(?P<e_article_id>\d+)/$', 'edu_articles.views.e_delete_commentsecond'),

)
