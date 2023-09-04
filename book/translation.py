from modeltranslation.translator import translator, TranslationOptions
from .models import Book,Author,Genre

class BookTranslationOptions(TranslationOptions):
    fields = ('title','bio')

translator.register(Book, BookTranslationOptions)


class AuthorTranslationOptions(TranslationOptions):
    fields = ('bio',)

translator.register(Author, AuthorTranslationOptions)

class GenreTranslationOptions(TranslationOptions):
    fields = ('type_genre',)

translator.register(Genre, GenreTranslationOptions)