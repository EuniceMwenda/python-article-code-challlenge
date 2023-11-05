#!/usr/bin/env python3
import ipdb;

from ..lib import *

if __name__ == '__main__':
#  WRITE YOUR TEST CODE HERE ###
    author1 = Author("Author 1")
    author2 = Author("Author 2")

    magazine1 = Magazine("Magazine 1", "Category A")
    magazine2 = Magazine("Magazine 2", "Category B")

    author1.add_article(magazine1, "Article 1")
    author1.add_article(magazine1, "Article 2")
    author1.add_article(magazine2, "Article 3")
    author2.add_article(magazine2, "Article 4")

    print(author1.articles())
    print(author1.magazines())
    print(author1.topic_areas())

    print(magazine1.contributors())
    print(magazine1.article_titles())
    print(magazine1.contributing_authors())

    print(Article.all())
   
# DO NOT REMOVE THIS
    ipdb.set_trace()
