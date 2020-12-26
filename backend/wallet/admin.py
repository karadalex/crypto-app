from django.contrib import admin
from .models import Transaction, Wallet, Asset


admin.site.register(Transaction)
admin.site.register(Wallet)
admin.site.register(Asset)
