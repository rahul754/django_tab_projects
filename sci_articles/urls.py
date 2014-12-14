from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^s_all/$', 'sci_articles.views.s_articles'),
    url(r'^s_get/(?P<s_article_id>\d+)/$', 'sci_articles.views.s_article'),
    url(r'^s_create/$', 'sci_articles.views.s_create'),
    url(r'^s_like/(?P<s_article_id>\d+)/$', 'sci_articles.views.s_like_article'),
    url(r'^s_add_comment/(?P<s_article_id>\d+)/$', 'sci_articles.views.s_add_comment'),
    url(r'^s_delete_comment/(?P<s_comment_id>\d+)/$', 'sci_articles.views.s_delete_comment'),
    url(r'^s_add_commentsecond/(?P<s_article_id>\d+)/$', 'sci_articles.views.s_add_commentsecond'),
    url(r'^s_delete_commentsecond/(?P<s_article_id>\d+)/$', 'sci_articles.views.s_delete_commentsecond'),

)
