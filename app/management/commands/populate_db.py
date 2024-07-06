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
        pdf_path = os.path.join(settings.BASE_DIR, 'response_file.pdf')
        
        # Check if the PDF file exists
        if not os.path.exists(pdf_path):
            self.stdout.write(self.style.ERROR(f'PDF file not found at: {pdf_path}'))
            return
        
        try:
            paragraphs = extract_paragraphs(pdf_path)
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error extracting paragraphs: {e}'))
            return

        for paragraph in paragraphs:
            if not paragraph == "" or not paragraph == " ":
                StudentResponse.objects.create(response=paragraph)
        
        self.stdout.write(self.style.SUCCESS('Successfully populated the database'))

def extract_paragraphs(pdf_path):
    paragraphs = []
    
    try:
        with fitz.open(pdf_path) as doc:
            for page in doc:
                text = page.get_text()
                paragraphs.extend(text.split('********'))
    except RuntimeError as e:
        raise RuntimeError(f'MuPDF error: {e}')
    
    return paragraphs
