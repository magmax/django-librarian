from django import test
# from django.db.utils import IntegrityError

from librarian.models import Author


class author_creation(test.TestCase):
    def test(self):
        author = Author()

        self.assertIsNotNone(author)


class author_has_name(test.TestCase):
    def test_basic(self):
        author = Author()
        author.name = 'Foo'

        author.save()

        a = Author.objects.filter()[0]

        self.assertEqual(author, a)
        self.assertEqual(author.name, a.name)


class author_has_surname(test.TestCase):
    def test_basic(self):
        author = Author()
        author.surname = 'Foo'

        author.save()

        a = Author.objects.filter()[0]

        self.assertEqual(author, a)
        self.assertEqual(author.surname, a.surname)


class author_name_styled(test.TestCase):

    def test_basic(self):
        author = Author()
        author.name = 'Foo'
        author.surname = 'Bar'

        self.assertEqual('Bar, Foo', str(author))
