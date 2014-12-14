from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.template import Context, loader
from django.shortcuts import render_to_response
from django.views.generic.base import TemplateView
from article.models import Article
from article.models import Comment
from article.models import CommentSecond

from django.contrib import messages
from forms import ArticleForm
from forms import CommentForm
from forms import CommentFormsecond

from django.http import HttpResponseRedirect
from django.core.context_processors import csrf


# Create your views here.


def index(request):
    return render_to_response('articles.html')

def articles(request):
    return render_to_response('articles.html',
                             {'articles': Article.objects.all() })    


def article(request, article_id):
    return render_to_response('article.html',
                             {'article': Article.objects.get(id=article_id) })    




def create(request):
    
    if request.POST:
        
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    
            return HttpResponseRedirect('/articles/all')
    else:
        form = ArticleForm()
        
    args = {}
    args.update(csrf(request))
    
    args['form'] = form
    
    return render_to_response('create_article.html', args)




def like_article(request, article_id):
    if article_id:
        a = Article.objects.get(id=article_id)
        count = a.likes
        count += 1
        a.likes = count
        a.save()
    
    
        return HttpResponseRedirect('/articles/get/%s' % article_id)  


def add_comment(request, article_id):
    a = Article.objects.get(id=article_id)
    
    if request.method == "POST":
        f = CommentForm(request.POST)
        if f.is_valid():
            c = f.save(commit=False)
            c.pub_date = timezone.now()
            c.article = a
            c.save()            
            
            return HttpResponseRedirect('/articles/get/%s' % article_id)
        
    else:
        f = CommentForm()

    args = {}
    args.update(csrf(request))
    
    args['article'] = a
    args['form'] = f
    
    return render_to_response('add_comment.html', args)    


def delete_comment(request, comment_id):
    c = Comment.objects.get(id=comment_id)
    
    article_id = c.article.id
    
    c.delete()

    
    return HttpResponseRedirect("/articles/get/%s" % article_id)




def add_commentsecond(request, article_id):
    a = Article.objects.get(id=article_id)
    
    if request.method == "POST":
        form = CommentFormsecond(request.POST)
        if form.is_valid():
            cs = form.save(commit=False)
            cs.pub_date = timezone.now()
            cs.article = a
            cs.save()
            
            
            return HttpResponseRedirect('/articles/get/%s' % article_id)
        
    else:
        form = CommentFormsecond()

    args = {}
    args.update(csrf(request))
    
    args['article'] = a
    args['form'] = form
    
    return render_to_response('add_commentsecond.html', args)    





def delete_commentsecond(request, comment_id):
    c = CommentSecond.objects.get(id=commentsecond_id)
    
    article_id = c.article.id
    
    c.delete()

    
    return HttpResponseRedirect("/articles/get/%s" % article_id)
