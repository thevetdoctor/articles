from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Article, Reporter

import datetime

# Create your views here.


def article_all(request):
    a_list = Article.objects.all().order_by('-id')
    for a in a_list:
        if not a.headline.isupper():
            b = a.headline.upper()
            a.headline = b
            a.save()
        else:
            b = a.headline.lower()
            a.headline = b
            a.save()
    year = 'all reporters'
    print('list displayed')
    context = {'year': year, 'article_list': a_list}
    return render(request, 'articles/list.html', context)


def article_detail(request, id):
    a_list = Article.objects.filter(pk=id)
    print(a_list[0].id, id)
    print('detail displayed')
    context = {'article': a_list[0]}
    return render(request, 'articles/detail.html', context)


def redirect_url(request):
    response = redirect('/articles/')
    return response

def article_edit(request, id):
    print(request)
    e = Article.objects.filter(id=id)[0]
    v = e.id
    if not e.headline.isupper():
        s = e.headline.upper()
        e.headline = s
        e.save()
    else:
        s = e.headline.lower()
        e.headline = s
        e.save()
    print('article', v, 'edited')
    print(e.headline)
    new_list = Article.objects.all().order_by('-id')
    context = {'article': new_list}
    print(new_list)
    # return render(request, 'articles/list.html', context)
    return redirect_url(request)
    # return render(request, 'articles/edit.html', context)


def article_delete(request, id):
    e = Article.objects.filter(id=id)[0]
    v = e.id
    print('article', v, 'deleted')
    e.delete()
    new_list = Article.objects.all().order_by('-id')
    context = {'article': new_list}
    print(new_list)
    return redirect_url(request)
    # return render(request, 'articles/list.html', context)


def home(request):
    a_list = Article.objects.all()
    context = {'article_list': a_list}
    # return HttpResponse('<h1>Welcome!!!</h1><h3>...to the<a href="/articles/"> world </a> of possibiities!</h3>')
    return render(request, 'articles/index.html')





    # if a_list:
    #     r = a_list[len(a_list) - 1].id + 1
    #     print(len(a_list))
    #     print(r)
    #     headine = 'headline' + str(r)
    # r_list = Reporter.objects.filter(reporter=name)
    # if r_list:
    #     if len(r_list) == 5:
    #         b = Reporter.objects.all()
    #         c = len(b) + 1
    #         name = 'Oba femi' + str(c)
    #     else:
    #         p = Reporter.objects.create(full_name=name)
    # Article.objects.create(pub_date=datetime.datetime.now(), headline=headline, content='content', reporter=p)
