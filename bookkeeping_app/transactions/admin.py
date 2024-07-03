from django.contrib import admin
from .models import Account, Party, Transaction, JournalEntries

# Register your models here.

admin.site.register(Account)
admin.site.register(Party)
admin.site.register(Transaction)
admin.site.register(JournalEntries)