from django.contrib import admin

# Register your models here.
from .models import First,Second,Third,Fourth,Fifth,Sixth

admin.site.register([First,Second,Third,Fourth,Fifth,Sixth])