from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.template import Context, loader
from django.shortcuts import render_to_response
from django.views.generic.base import TemplateView
from E_articles.models import Article
from E_articles.models import Comment
from E_articles.models import CommentSecond

from django.contrib import messages
from forms import ArticleForm
from forms import CommentForm
from forms import CommentFormsecond

from django.http import HttpResponseRedirect
from django.core.context_processors import csrf


# Create your views here.


def en_articles(request):
    return render_to_response('en_articles.html',
                             {'en_articles': Article.objects.all() })    


def en_article(request, en_article_id):
    return render_to_response('en_article.html',
                             {'en_article': Article.objects.get(id=en_article_id) })    




def en_create(request):
    
    if request.POST:
        
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    
            return HttpResponseRedirect('/en_articles/en_all')
    else:
        form = ArticleForm()
        
    args = {}
    args.update(csrf(request))
    
    args['form'] = form
    
    return render_to_response('en_create_article.html', args)




def en_like_article(request, en_article_id):
    if en_article_id:
        a = Article.objects.get(id=en_article_id)
        count = a.likes
        count += 1
        a.likes = count
        a.save()
    
    
        return HttpResponseRedirect('/en_articles/en_get/%s' % en_article_id)  


def en_add_comment(request, en_article_id):
    a = Article.objects.get(id=en_article_id)
    
    if request.method == "POST":
        f = CommentForm(request.POST)
        if f.is_valid():
            c = f.save(commit=False)
            c.pub_date = timezone.now()
            c.article = a
            c.save()            
            
            return HttpResponseRedirect('/en_articles/en_get/%s' % en_article_id)
        
    else:
        f = CommentForm()

    args = {}
    args.update(csrf(request))
    
    args['en_article'] = a
    args['form'] = f
    
    return render_to_response('en_add_comment.html', args)    


def en_delete_comment(request, en_comment_id):
    c = Comment.objects.get(id=en_comment_id)
    
    en_article_id = c.en_article.id
    
    c.delete()

    
    return HttpResponseRedirect("/en_articles/en_get/%s" % en_article_id)




def en_add_commentsecond(request, en_article_id):
    a = Article.objects.get(id=en_article_id)
    
    if request.method == "POST":
        form = CommentFormsecond(request.POST)
        if form.is_valid():
            cs = form.save(commit=False)
            cs.pub_date = timezone.now()
            cs.article = a
            cs.save()
            
            
            return HttpResponseRedirect('/en_articles/en_get/%s' % en_article_id)
        
    else:
        form = CommentFormsecond()

    args = {}
    args.update(csrf(request))
    
    args['en_article'] = a
    args['form'] = form
    
    return render_to_response('en_add_commentsecond.html', args)    





def en_delete_commentsecond(request, en_comment_id):
    c = CommentSecond.objects.get(id=en_commentsecond_id)
    
    en_article_id = c.en_article.id
    
    c.delete()

    
    return HttpResponseRedirect("/en_articles/en_get/%s" % en_article_id)
