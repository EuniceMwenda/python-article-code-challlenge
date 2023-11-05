
class Author:
     all_authors = []

     def __init__(self, author_name):
        from .Article import Article
        self.author_name = author_name
        self._articles = []  
        Author.all_authors.append(self)

     def add_article(self, magazine, title):
        from .Article import Article
        article = Article(self, magazine, title)
        self._articles.append(article)  
        magazine.add_contributor(self)
     pass