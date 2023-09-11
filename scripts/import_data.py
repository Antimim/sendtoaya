from projetstage.models import Article


def run():
    for i in range(5, 15):
        article = Article()
        article.titre = "Article N° #%d" % i
        article.desc = "Description N° #%d" % i
        article.image = "http://default"
        article.save()


print("opération réussie")
