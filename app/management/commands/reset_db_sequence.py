from django.core.management.base import BaseCommand
from django.db import connection
from app.models import StudentResponse 

class Command(BaseCommand):
    help = 'Reset primary key sequence of MyModel'

    def handle(self, *args, **kwargs):
        # Delete all existing data
        StudentResponse.objects.all().delete()

        # Reset sequence
        with connection.cursor() as cursor:
            if connection.vendor == 'postgresql':
                cursor.execute("ALTER SEQUENCE myapp_mymodel_id_seq RESTART WITH 1;")
            elif connection.vendor == 'sqlite':
                cursor.execute("DELETE FROM sqlite_sequence WHERE name='myapp_mymodel';")
            elif connection.vendor == 'mysql':
                cursor.execute("ALTER TABLE myapp_mymodel AUTO_INCREMENT = 1;")

        self.stdout.write(self.style.SUCCESS('Successfully reset the primary key sequence'))
