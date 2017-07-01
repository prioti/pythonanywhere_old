# coding=utf-8
from django.shortcuts import render_to_response
from prioti.article.models import Article
from django.http import HttpResponse
from prioti.article.forms import ArticleForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf

# Create your views here.
def articles(request):
    """
    Список всех статей
    :param request:
    :return:
    """
    language = 'ru-ru'
    session_language = 'ru-ru'

    if 'lang' in request.COOKIES:
        language = request.COOKIES['lang']
    if 'lang' in request.session:
        session_language = request.session['lang']
    return render_to_response('articles.html',
                              {'articles': Article.objects.all(),
                               'language': language,
                               'session_language': session_language})

def article(request, article_id=1):
    """
    :param article_id:
    :return:
    """
    return render_to_response('article.html',
                              dict(article=Article.objects.get(id=article_id)))

def language(request, language='en-gb'):
    responce = HttpResponse('settings language to%s' % language)

    responce.set_cookie('lang', language)
    request.session['lang'] = language

    return responce

def create(request):
    if request.POST:
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/articles/all')
    else:
        form = ArticleForm()

    args = {}
    args.update(csrf(request))
    args['form'] = form

    return  render_to_response('create_article.html', args)

def hello(request):
    name = "Anton"
    http = "<html><head><title>Hi %s, is a Test</title></head><body<p>Test page</p></body>" % name
    return HttpResponse(http)
