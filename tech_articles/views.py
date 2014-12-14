from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render_to_response
from django.views.generic.base import TemplateView
from tech_articles.models import tech_Article


def t_articles(request):
    return render_to_response('tech_article.html',
                             {'article': edu_Article.objects.all() })    



def t_articles(request, article_id=1):
    return render_to_response('tech_article.html',
                             {'article': edu_Article.objects.get(id=article_id) })    

