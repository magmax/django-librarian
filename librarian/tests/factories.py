import factory

from librarian import models


class AuthorFactory(factory.DjangoModelFactory):
    FACTORY_FOR = models.Author

    name = 'Francisco'
    surname = 'Quevedo'
