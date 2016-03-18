from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    created_at = models.DateTimeField('date created', auto_now_add=True, null=True)
    updated_at = models.DateTimeField('date updated', auto_now=True, null=True)

    def __unicode__(self):
        return u'{}, {}'.format(self.name, self.pk)


class Publisher(models.Model):
    name = models.CharField(max_length=300)
    num_awards = models.IntegerField()
    created_at = models.DateTimeField('date created', auto_now_add=True, null=True)
    updated_at = models.DateTimeField('date updated', auto_now=True, null=True)

    def __unicode__(self):
        return u'{}, {}'.format(self.name, self.pk)


class Book(models.Model):
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    pubdate = models.DateField()
    abstract = models.TextField()
    category = models.CharField(max_length=30)
    created_at = models.DateTimeField('date created', auto_now_add=True, null=True)
    updated_at = models.DateTimeField('date updated', auto_now=True, null=True)

    def __unicode__(self):
        return u'{}, {}, {}, {}, {}'.format(self.name, self.authors.all().values_list('name', flat=True),
                                            self.publisher, self.category, self.pk)
