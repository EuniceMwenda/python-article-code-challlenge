
class Article:
    all_articles = []

    def __init__(self, author, magazine, title):
        from .Author import Author
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all_articles.append(self)

    def article_title(self):
        return self.title

    def articles(self):
        return self._articles
    pass