from django.db import models


TITLE_NAME_LENGTH = 200
TITLE_DESCRIPTION_LENGTH = 225
CATEGORY_NAME_LENGTH = 256
CATEGORY_SLUG_LENGTH = 50


class Category(models.Model):
    name = models.CharField(max_length=CATEGORY_NAME_LENGTH)
    slug = models.SlugField(max_length=CATEGORY_SLUG_LENGTH, unique=True)

    class Meta:
        verbose_name = 'Категория'

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=CATEGORY_NAME_LENGTH)
    slug = models.SlugField(max_length=CATEGORY_SLUG_LENGTH, unique=True)

    class Meta:
        verbose_name = 'Жанр'

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(max_length=TITLE_NAME_LENGTH)
    year = models.models.IntegerField()(unique=True)
    description = models.TextField(
        max_length=TITLE_DESCRIPTION_LENGTH,
        null=True,
        blank=True
    )
    category = models.ForeignKey(
        Category,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='categories',
        verbose_name='Категория',
    )
    genre = models.ManyToManyField(
        Genre,
        through='GenreTitle',
        related_name='genres',
        verbose_name='Жанр',
    )

    class Meta:
        verbose_name = 'Произведение'

    def __str__(self):
        return self.name


class GenreTitle(models.Model):
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE
    )
