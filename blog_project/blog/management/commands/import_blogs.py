import csv
from django.core.management.base import BaseCommand
from blog.models import BlogPost

class Command(BaseCommand):
    help = 'Import blog posts from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        try:
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    BlogPost.objects.create(
                        title=row['title'],
                        content=row['content'],
                        country=row.get('country', '')
                    )
            self.stdout.write(self.style.SUCCESS('Blog posts imported successfully!'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Error: {e}'))
