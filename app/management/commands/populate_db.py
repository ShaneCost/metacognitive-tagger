### $ heroku run python manage.py populate_db 
### $ python manage.py populate_db 

from django.core.management.base import BaseCommand
from app.models import StudentResponse
import fitz  # PyMuPDF
from django.conf import settings
import os

class Command(BaseCommand):
    help = 'Populate database with paragraphs from PDF'

    def handle(self, *args, **kwargs):
        
        pdf_path = os.path.join(settings.BASE_DIR, 'responses.pdf')
        paragraphs = extract_paragraphs(pdf_path)
        
        for paragraph in paragraphs:
            StudentResponse.objects.create(text=paragraph)
        
        self.stdout.write(self.style.SUCCESS('Successfully populated the database'))

def extract_paragraphs(pdf_path):
    paragraphs = []
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text = page.get_text()
            paragraphs.extend(text.split('**'))
    
    return paragraphs


