from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.template import Context, loader
from django.shortcuts import render_to_response
from django.views.generic.base import TemplateView
from edu_articles.models import Article
from edu_articles.models import Comment
from edu_articles.models import CommentSecond

from django.contrib import messages
from forms import ArticleForm
from forms import CommentForm
from forms import CommentFormsecond

from django.http import HttpResponseRedirect
from django.core.context_processors import csrf


# Create your views here.


def e_articles(request):
    return render_to_response('e_articles.html',
                             {'e_articles': Article.objects.all() })    


def e_article(request, e_article_id):
    return render_to_response('e_article.html',
                             {'e_article': Article.objects.get(id=e_article_id) })    




def e_create(request):
    
    if request.POST:
        
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    
            return HttpResponseRedirect('/e_articles/e_all')
    else:
        form = ArticleForm()
        
    args = {}
    args.update(csrf(request))
    
    args['form'] = form
    
    return render_to_response('e_create_article.html', args)




def e_like_article(request, e_article_id):
    if e_article_id:
        a = Article.objects.get(id=e_article_id)
        count = a.likes
        count += 1
        a.likes = count
        a.save()
    
    
        return HttpResponseRedirect('/e_articles/e_get/%s' % e_article_id)  


def e_add_comment(request, e_article_id):
    a = Article.objects.get(id=e_article_id)
    
    if request.method == "POST":
        f = CommentForm(request.POST)
        if f.is_valid():
            c = f.save(commit=False)
            c.pub_date = timezone.now()
            c.article = a
            c.save()            
            
            return HttpResponseRedirect('/e_articles/e_get/%s' % e_article_id)
        
    else:
        f = CommentForm()

    args = {}
    args.update(csrf(request))
    
    args['e_article'] = a
    args['form'] = f
    
    return render_to_response('e_add_comment.html', args)    


def e_delete_comment(request, e_comment_id):
    c = Comment.objects.get(id=e_comment_id)
    
    e_article_id = c.e_article.id
    
    c.delete()

    
    return HttpResponseRedirect("/e_articles/e_get/%s" % e_article_id)




def e_add_commentsecond(request, e_article_id):
    a = Article.objects.get(id=e_article_id)
    
    if request.method == "POST":
        form = CommentFormsecond(request.POST)
        if form.is_valid():
            cs = form.save(commit=False)
            cs.pub_date = timezone.now()
            cs.article = a
            cs.save()
            
            
            return HttpResponseRedirect('/e_articles/e_get/%s' % e_article_id)
        
    else:
        form = CommentFormsecond()

    args = {}
    args.update(csrf(request))
    
    args['e_article'] = a
    args['form'] = form
    
    return render_to_response('e_add_commentsecond.html', args)    





def e_delete_commentsecond(request, e_comment_id):
    c = CommentSecond.objects.get(id=e_commentsecond_id)
    
    e_article_id = c.e_article.id
    
    c.delete()

    
    return HttpResponseRedirect("/e_articles/e_get/%s" % e_article_id)
