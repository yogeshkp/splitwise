from django.contrib import admin

# Register your models here.
from .models import Group, Debts, Transaction

admin.site.register(Group)
admin.site.register(Debts)
admin.site.register(Transaction)
