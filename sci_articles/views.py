from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.template import Context, loader
from django.shortcuts import render_to_response
from django.views.generic.base import TemplateView
from sci_articles.models import Article
from sci_articles.models import Comment
from sci_articles.models import CommentSecond

from django.contrib import messages
from forms import ArticleForm
from forms import CommentForm
from forms import CommentFormsecond

from django.http import HttpResponseRedirect
from django.core.context_processors import csrf


# Create your views here.


def s_articles(request):
    return render_to_response('s_articles.html',
                             {'s_articles': Article.objects.all() })    


def s_article(request, s_article_id):
    return render_to_response('s_article.html',
                             {'s_article': Article.objects.get(id=s_article_id) })    




def s_create(request):
    
    if request.POST:
        
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    
            return HttpResponseRedirect('/s_articles/s_all')
    else:
        form = ArticleForm()
        
    args = {}
    args.update(csrf(request))
    
    args['form'] = form
    
    return render_to_response('s_create_article.html', args)




def s_like_article(request, s_article_id):
    if s_article_id:
        a = Article.objects.get(id=s_article_id)
        count = a.likes
        count += 1
        a.likes = count
        a.save()
    
    
        return HttpResponseRedirect('/s_articles/s_get/%s' % s_article_id)  


def s_add_comment(request, s_article_id):
    a = Article.objects.get(id=s_article_id)
    
    if request.method == "POST":
        f = CommentForm(request.POST)
        if f.is_valid():
            c = f.save(commit=False)
            c.pub_date = timezone.now()
            c.article = a
            c.save()            
            
            return HttpResponseRedirect('/s_articles/s_get/%s' % s_article_id)
        
    else:
        f = CommentForm()

    args = {}
    args.update(csrf(request))
    
    args['s_article'] = a
    args['form'] = f
    
    return render_to_response('s_add_comment.html', args)    


def s_delete_comment(request, s_comment_id):
    c = Comment.objects.get(id=s_comment_id)
    
    s_article_id = c.s_article.id
    
    c.delete()

    
    return HttpResponseRedirect("/s_articles/s_get/%s" % s_article_id)




def s_add_commentsecond(request, s_article_id):
    a = Article.objects.get(id=s_article_id)
    
    if request.method == "POST":
        form = CommentFormsecond(request.POST)
        if form.is_valid():
            cs = form.save(commit=False)
            cs.pub_date = timezone.now()
            cs.article = a
            cs.save()
            
            
            return HttpResponseRedirect('/s_articles/s_get/%s' % s_article_id)
        
    else:
        form = CommentFormsecond()

    args = {}
    args.update(csrf(request))
    
    args['s_article'] = a
    args['form'] = form
    
    return render_to_response('s_add_commentsecond.html', args)    





def s_delete_commentsecond(request, s_comment_id):
    c = CommentSecond.objects.get(id=s_commentsecond_id)
    
    s_article_id = c.s_article.id
    
    c.delete()

    
    return HttpResponseRedirect("/s_articles/s_get/%s" % s_article_id)
