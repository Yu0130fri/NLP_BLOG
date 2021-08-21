from django.shortcuts import render
from django.core.paginator import Page, Paginator

from .forms import CommentForm
from blog.models import PostArticle, Comment


def index(request):
    """
    Show all articles everyone posted
    """
    
    objs = PostArticle.objects.all()
    pagenator = Paginator(objs, 2)

    # http GET POSTの通信方法にて、POSTはformの送信など
    # GETは以下のようなURL形式
    # https://test.com/kiji/?page=1のようなもの
    page_number = request.GET.get('page')

    return render(request, 'blog/articles.html', context={
        'page_obj': pagenator.get_page(page_number),
        'page_number': page_number
    })

def show_article(request, pk):

    obj = PostArticle.objects.get(pk=pk)

    if request.POST:
        form = CommentForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.article = obj
            comment.save()
    
    comments = Comment.objects.filter(article=pk)

    return render(request, 'blog/show_article.html', context={
        'article': obj,
        'comments': comments,
    })