from graphene_django.types import DjangoObjectType
from django.contrib.auth.models import User
from .models import CryptoCurrency, FiatCurrency, PriceRecord


class CryptoCurrencyType(DjangoObjectType):
	class Meta:
		model = CryptoCurrency
		fields = '__all__'

class FiatCurrencyType(DjangoObjectType):
	class Meta:
		model = FiatCurrency
		fields = '__all__'

class PriceRecordType(DjangoObjectType):
	class Meta:
		model = PriceRecord
		fields = '__all__'