from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^p_all/$', 'poli_articles.views.p_articles'),
    url(r'^p_get/(?P<p_article_id>\d+)/$', 'poli_articles.views.p_article'),
    url(r'^p_create/$', 'poli_articles.views.p_create'),
    url(r'^p_like/(?P<p_article_id>\d+)/$', 'poli_articles.views.p_like_article'),
    url(r'^p_add_comment/(?P<p_article_id>\d+)/$', 'poli_articles.views.p_add_comment'),
    url(r'^p_delete_comment/(?P<p_comment_id>\d+)/$', 'poli_articles.views.p_delete_comment'),
    url(r'^p_add_commentsecond/(?P<p_article_id>\d+)/$', 'poli_articles.views.p_add_commentsecond'),
    url(r'^p_delete_commentsecond/(?P<p_article_id>\d+)/$', 'poli_articles.views.p_delete_commentsecond'),

)
