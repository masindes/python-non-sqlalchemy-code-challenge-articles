class Article:

    all = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        self.all.append(self)   

    @property
    def title(self):
        return self._title


    @title.setter
    def title(self, new_title):
        if hasattr(self, 'title'):
            AttributeError('Title cannot be changed')
        else:
            if isinstance(new_title, str):
                if 5 <= len(new_title) <= 50 :
                    self._title = new_title
                else:
                    raise ValueError('Title must be between 5 and 50 characters')
            else:
                raise TypeError('Title must be a string')

    @property
    def author(self):
        return self._author

    
    @author.setter
    def author(self, new_author):
        if isinstance(new_author, Author):
            self._author = new_author
        else:
            raise TypeError('Author must be an instance of Author')
        
class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    
    @name.setter
    def name(self, new_name):
        if hasattr(self, 'name'):
            AttributeError('Name cannot be changed')
        else:
            if isinstance(new_name,str):
                if len(new_name):
                    self._name = new_name
                else:
                    raise ValueError('Name must be longer than 0 characters')
            else:
                raise TypeError('Name must be a string')

    def articles(self):
        pass

    def magazines(self):
        pass

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass