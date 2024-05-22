from django.contrib import admin
from .models import StudentResponse, ExpertResponse, User

# Register your models here.
admin.site.register(StudentResponse)
admin.site.register(ExpertResponse)
admin.site.register(User)


