from django.contrib import admin

from .models import Person, Address, Messages, Mark

admin.site.register(Person)
admin.site.register(Address)
admin.site.register(Messages)
admin.site.register(Mark)
