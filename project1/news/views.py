from django.shortcuts import render
from django import forms
from django.db import IntegrityError
from .models import New
from django.views.generic import ListView
from comments.models import Comment


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = "__all__"


class post_list(ListView):
    paginate_by = 9
    model = New
    template_name = '../templates/News.html'


def post_detail(request, id):
    template_name = '../templates/newsmore.html'
    post = New.objects.get(id=id)
    comments_qt = len(Comment.objects.filter(post=post))
    comments = Comment.objects.filter(post=post)
    popular_news = New.objects.all()[:5]

    if request.method == 'POST':
        user = request.user
        text = request.POST['text']
        try:
            Comment.objects.create(user=user, text=text, post=post)
         
        except IntegrityError:
            return render(request, template_name, context)       


    context = {
        'post': post,
        'comments_qt': comments_qt,
        'comments': comments,
        'popular_news': popular_news,
    }

    return render(request, template_name, context)
