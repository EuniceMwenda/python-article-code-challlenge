#!/usr/bin/env python3
import ipdb;
from lib import Article, Author, Magazine




if __name__ == '__main__':
#  WRITE YOUR TEST CODE HERE ###
   magazine1 = Magazine("Magazine 1", "Category A")
   magazine2 = Magazine("Magazine 2", "Category B")
   
   author1 = Author("Author 1")
   author2 = Author("Author 2")

   author1.add_article(magazine1, "Article 1 by Author 1")
   author1.add_article(magazine2, "Article 2 by Author 1")
   author2.add_article(magazine1, "Article 1 by Author 2")

 
print("Magazine Names:")
print(magazine1._name)  
print(magazine2._name)

print("\nAuthor Names:")
print(author1.author_name)
print(author2.author_name)

print("\nMagazine Categories:")
print(magazine1._category)
print(magazine2._category)

print("\nContributors of Magazine 1:")
contributors = magazine1._contributors
for contributor in contributors:
    print(contributor.author_name)

print("\nArticle Titles in Magazine 1:")
titles = Magazine.article_titles()
for title in titles:
    print(title)


   
# DO NOT REMOVE THIS
ipdb.set_trace()
