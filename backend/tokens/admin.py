from django.contrib import admin
from .models import CryptoCurrency, FiatCurrency, PriceRecord


admin.site.register(CryptoCurrency)
admin.site.register(FiatCurrency)
admin.site.register(PriceRecord)
