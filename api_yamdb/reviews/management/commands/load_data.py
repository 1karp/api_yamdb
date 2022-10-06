import csv
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from reviews.models import Category, Comment, Genre, GenreTitle, Review, Title, User

TABLES_2_FILES_DICT = {
    User: 'users.csv',
    Category: 'category.csv',
    Genre: 'genre.csv',
    Title: 'titles.csv',
    Review: 'review.csv',
    Comment: 'comments.csv',
    GenreTitle: 'genre_title.csv'
}


class Command(BaseCommand):
    help = 'Import data from CSV files in static folder'

    def handle(self, *args, **options):
        for model, file in TABLES_2_FILES_DICT.items():
            with open(
                f'{settings.BASE_DIR}/static/data/{file}',
                'r', encoding='utf-8'
            ) as csv_file:
                reader = csv.reader(csv_file)
                model.objects.bulk_create(model(**data) for data in reader)
        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
