class Magazine:
   all_magazines = []

   def __init__(self, name, category):
        self._name = name
        self._category = category
        self._contributors = []
        Magazine.all_magazines.append(self)

   def add_contributor(self, author):
        if author not in self._contributors:
            self._contributors.append(author)

   @classmethod
   def article_titles(cls):
        from .Article import Article
        titles = []
        for magazine in cls.all_magazines:
            for article in Article.all_articles:  
                if article.magazine == magazine:
                    titles.append(article.article_title())
        return titles


pass