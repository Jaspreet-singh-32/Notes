from django.contrib import admin

# Register your models here.

from show.models import Data,Contact

admin.site.register([Data,Contact])