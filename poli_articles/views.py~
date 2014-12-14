from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.template import Context, loader
from django.shortcuts import render_to_response
from django.views.generic.base import TemplateView
from poli_articles.models import Article
from poli_articles.models import Comment
from poli_articles.models import CommentSecond

from django.contrib import messages
from forms import ArticleForm
from forms import CommentForm
from forms import CommentFormsecond

from django.http import HttpResponseRedirect
from django.core.context_processors import csrf


# Create your views here.


def p_articles(request):
    return render_to_response('p_articles.html',
                             {'p_articles': Article.objects.all() })    


def p_article(request, p_article_id):
    return render_to_response('p_article.html',
                             {'p_article': Article.objects.get(id=p_article_id) })    




def p_create(request):
    
    if request.POST:
        
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    
            return HttpResponseRedirect('/p_articles/p_all')
    else:
        form = ArticleForm()
        
    args = {}
    args.update(csrf(request))
    
    args['form'] = form
    
    return render_to_response('p_create_article.html', args)




def p_like_article(request, p_article_id):
    if p_article_id:
        a = Article.objects.get(id=p_article_id)
        count = a.likes
        count += 1
        a.likes = count
        a.save()
    
    
        return HttpResponseRedirect('/p_articles/p_get/%s' % p_article_id)  


def p_add_comment(request, p_article_id):
    a = Article.objects.get(id=p_article_id)
    
    if request.method == "POST":
        f = CommentForm(request.POST)
        if f.is_valid():
            c = f.save(commit=False)
            c.pub_date = timezone.now()
            c.article = a
            c.save()            
            
            return HttpResponseRedirect('/p_articles/p_get/%s' % p_article_id)
        
    else:
        f = CommentForm()

    args = {}
    args.update(csrf(request))
    
    args['p_article'] = a
    args['form'] = f
    
    return render_to_response('p_add_comment.html', args)    


def p_delete_comment(request, p_comment_id):
    c = Comment.objects.get(id=p_comment_id)
    
    p_article_id = c.p_article.id
    
    c.delete()

    
    return HttpResponseRedirect("/p_articles/p_get/%s" % p_article_id)




def p_add_commentsecond(request, p_article_id):
    a = Article.objects.get(id=p_article_id)
    
    if request.method == "POST":
        form = CommentFormsecond(request.POST)
        if form.is_valid():
            cs = form.save(commit=False)
            cs.pub_date = timezone.now()
            cs.article = a
            cs.save()
            
            
            return HttpResponseRedirect('/p_articles/p_get/%s' % p_article_id)
        
    else:
        form = CommentFormsecond()

    args = {}
    args.update(csrf(request))
    
    args['p_article'] = a
    args['form'] = form
    
    return render_to_response('p_add_commentsecond.html', args)    





def p_delete_commentsecond(request, p_comment_id):
    c = CommentSecond.objects.get(id=p_commentsecond_id)
    
    p_article_id = c.p_article.id
    
    c.delete()

    
    return HttpResponseRedirect("/p_articles/p_get/%s" % p_article_id)
