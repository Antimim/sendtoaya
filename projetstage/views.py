from django.shortcuts import render
from .models import Article, Category
from django.http import HttpResponse


def home(request):
    list_articles = Article.objects.all()
    context = {"liste_articles": list_articles}
    return render(request, "index.html", context)


def detail(request, id_article):
    article = Article.objects.get(id=id_article)
    category = article.category
    articles_en_relation = Article.objects.filter(category=category)[:6]
    return render(
        request, "detail.html", {"article": article, "aer": articles_en_relation}
    )


def search(request):
    query = request.GET["article"]
    liste_article = Article.objects.filter(titre__icontains=query)
    return render(request, "search.html", {"liste_article": liste_article})


def sms(request):
    message = request.GET["body"]
    message_splited = message.split("-")
    titre = message_splited[0]
    desc = message_splited[1]

    agri_category = Category.objects.get(id=2)
    article = Article(
        titre=titre, category=agri_category, desc=desc, image="http://default"
    )
    article.save()
    print("data saved successfully")
    return HttpResponse("data saved successfully")


exit()
