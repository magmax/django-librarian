from django import test
from django.db.utils import IntegrityError

from librarian.models import Book
from factories import AuthorFactory


class book_creation(test.TestCase):
    def test(self):
        book = Book()

        self.assertIsNotNone(book)


class book_has_a_title(test.TestCase):
    def setUp(self):
        self.book = Book()

    def test_basic(self):
        self.book.title = 'Foo'
        self.book.save()

        book = Book.objects.get(title='Foo')

        self.assertEqual(book, self.book)
        self.assertEqual(book.title, self.book.title)

    def test_length_limit(self):
        self.book.title = 200 * 'a'
        self.book.save()

        book = Book.objects.filter()[0]

        self.assertEqual(book, self.book)

    def test_title_is_mandatory(self):
        self.book.title = None
        with self.assertRaises(IntegrityError):
            self.book.save()


class book_has_description(test.TestCase):
    def test_basic(self):
        book = Book()

        book.description = 'Foo'
        book.save()

        b = Book.objects.filter()[0]

        self.assertEqual(b, book)
        self.assertEqual(b.description, book.description)


class book_has_isbn_13(test.TestCase):
    def test_basic(self):
        book = Book()

        book.isbn_13 = '123-456-789'
        book.save()

        b = Book.objects.filter()[0]
        self.assertEqual(b, book)
        self.assertEqual(b.isbn_13, book.isbn_13)


class book_has_publisher(test.TestCase):
    def test_basic(self):
        book = Book()

        book.publisher = 'foo'
        book.save()

        b = Book.objects.filter()[0]
        self.assertEqual(b, book)
        self.assertEqual(b.publisher, book.publisher)


class book_has_year(test.TestCase):
    def test_basic(self):
        book = Book()

        book.year = 1492
        book.save()

        b = Book.objects.filter()[0]
        self.assertEqual(b, book)
        self.assertEqual(b.year, book.year)


class book_has_language(test.TestCase):
    def test_basic(self):
        book = Book()

        book.language = 'english'
        book.save()

        b = Book.objects.filter()[0]
        self.assertEqual(b, book)
        self.assertEqual(b.language, book.language)

    def _test_language_is_stored_lower_case(self):
        book = Book()

        book.language = 'EnGlIsH'
        book.save()

        b = Book.objects.filter()[0]
        self.assertEqual(b, book)
        self.assertEqual(b.language.lower(), book.language)


class book_has_authors(test.TestCase):
    def setUp(self):
        self.book = Book()
        self.book.save()

    def test_no_authors(self):
        book = Book.objects.filter()[0]

        self.assertEqual([], list(book.authors.values()))

    def test_one_author(self):
        author = AuthorFactory.create()
        self.book.authors.add(author)
        self.book.save()

        book = Book.objects.filter()[0]

        self.assertEqual([author], list(book.authors.filter()))

    def test_several_authors(self):
        author1 = AuthorFactory.create(name='Francisco', surname='Quevedo')
        author2 = AuthorFactory.create(name='Lope', surname='de Vega')
        self.book.authors.add(author1)
        self.book.authors.add(author2)
        self.book.save()

        book = Book.objects.filter()[0]

        self.assertEqual(set([author1, author2]),
                         set(book.authors.filter()))

