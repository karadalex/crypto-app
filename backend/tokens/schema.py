import graphene
from graphene_django.types import DjangoObjectType
from .models import CryptoCurrency, FiatCurrency, PriceRecord
from .types import CryptoCurrencyType, FiatCurrencyType, PriceRecordType


class Query(graphene.ObjectType):
	crypto_currencies = graphene.List(CryptoCurrencyType)
	crypto_currency = graphene.Field(CryptoCurrencyType, symbol=graphene.String())

	fiat_currencies = graphene.List(FiatCurrencyType)
	fiat_currency = graphene.Field(FiatCurrencyType, symbol=graphene.String())

	def resolve_crypto_currencies(self, info, **kwargs):
		return CryptoCurrency.objects.all()

	def resolve_crypto_currency(self, info, symbol):
		return CryptoCurrency.objects.get(symbol=symbol.upper())

	def resolve_fiat_currencies(self, info, **kwargs):
		return FiatCurrency.objects.all()

	def resolve_fiat_currency(self, info, symbol):
		return FiatCurrency.objects.get(symbol=symbol.upper())

# class Mutation(graphene.ObjectType):
# 	pass

schema = graphene.Schema(query=Query)
