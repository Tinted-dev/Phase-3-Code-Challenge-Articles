# 
class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if len(name) == 0:
            raise ValueError("Name must be longer than 0 characters.")
        self._name = name
        self._articles = []  # To store articles written by the author

    @property
    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def magazines(self):
        return list({article.magazine for article in self._articles})

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        magazine.add_article(article)
        return article

    def topic_areas(self):
        if not self._articles:
            return None
        return list({article.magazine.category for article in self._articles})


class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if not (2 <= len(name) <= 16):
            raise ValueError("Name must be between 2 and 16 characters.")
        if not isinstance(category, str):
            raise TypeError("Category must be a string.")
        if len(category) == 0:
            raise ValueError("Category must be longer than 0 characters.")

        self.name = name
        self.category = category
        self._articles = []  # To store articles published in the magazine

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string.")
        if not (2 <= len(value) <= 16):
            raise ValueError("Name must be between 2 and 16 characters.")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise TypeError("Category must be a string.")
        if len(value) == 0:
            raise ValueError("Category must be longer than 0 characters.")
        self._category = value

    def articles(self):
        return self._articles

    def add_article(self, article):
        self._articles.append(article)

    def contributors(self):
        return list({article.author for article in self._articles})

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        from collections import Counter

        author_count = Counter(article.author for article in self._articles)
        result = [author for author, count in author_count.items() if count > 2]
        return result if result else None


class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise TypeError("Author must be of type Author.")
        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine must be of type Magazine.")
        if not isinstance(title, str):
            raise TypeError("Title must be a string.")
        if not (5 <= len(title) <= 50):
            raise ValueError("Title must be between 5 and 50 characters.")

        self._author = author
        self._magazine = magazine
        self._title = title

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise TypeError("Author must be of type Author.")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise TypeError("Magazine must be of type Magazine.")
        self._magazine = value


# Example Usage
if __name__ == "__main__":
    author = Author("John Doe")
    magazine = Magazine("Tech Times", "Technology")
    article = author.add_article(magazine, "The Future of AI")

    print(author.name)  # Output: John Doe
    print(magazine.name)  # Output: Tech Times
    print(article.title)  # Output: The Future of AI
    print(author.articles())  # Output: [<__main__.Article object>]
    print(author.magazines())  # Output: [<__main__.Magazine object>]
    print(magazine.articles())  # Output: [<__main__.Article object>]
    print(magazine.contributors())  # Output: [<__main__.Author object>]
