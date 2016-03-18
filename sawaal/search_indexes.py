from haystack import indexes

from sawaal.models import Book


class BookIndex(indexes.SearchIndex, indexes.Indexable):
    abstract = indexes.CharField(model_attr='abstract')
    name = indexes.CharField(model_attr='name')
    text = indexes.CharField(document=True)
    pages = indexes.IntegerField(model_attr='pages', faceted=True)
    price = indexes.IntegerField(model_attr='price', faceted=True)
    rating = indexes.FloatField(model_attr='rating', faceted=True)
    book_id = indexes.CharField(model_attr='id', faceted=False)
    pubdate = indexes.DateField(model_attr='pubdate', faceted=True)
    category = indexes.CharField(model_attr='category', faceted=True)
    publisher = indexes.CharField(model_attr='publisher', faceted=True)
    pub_year = indexes.CharField(faceted=True)

    def get_model(self):
        return Book

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

    def prepare_author_set(self, obj):
        return [author.name for author in obj.authors.all().order_by('-name')]

    def prepare_pub_year(self, obj):
        return obj.pubdate.year

    def prepare_text(self, obj):
        return u'{} {}'.format(obj.name, obj.abstract)
