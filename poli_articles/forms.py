from django import forms
from poli_articles.models import Article, Comment , CommentSecond 

class ArticleForm(forms.ModelForm):  

    class Meta:
        model = Article
        fields = ('title', 'body', 'pub_date', 'thumbnail')
        
        
        
        
        
class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('first_name', 'second_name', 'body')


class CommentFormsecond(forms.ModelForm):
    
    class Meta:
        model = CommentSecond
        fields = ('first_name', 'second_name', 'body')
