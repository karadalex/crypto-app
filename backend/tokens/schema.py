import graphene
from graphene_django.types import DjangoObjectType
from .models import CryptoCurrency, FiatCurrency, PriceRecord
from .types import CryptoCurrencyType, FiatCurrencyType, PriceRecordType


class Query(graphene.ObjectType):
	crypto_currencies = graphene.List(CryptoCurrencyType)
	crypto_currency = graphene.Field(CryptoCurrencyType, symbol=graphene.String())

	fiat_currencies = graphene.List(FiatCurrencyType)
	fiat_currency = graphene.Field(FiatCurrencyType, symbol=graphene.String())

	price_records = graphene.List(PriceRecordType, from_symbol=graphene.String(), to_symbol=graphene.String())
	latest_price_record = graphene.Field(PriceRecordType, from_symbol=graphene.String(), to_symbol=graphene.String())

	def resolve_crypto_currencies(self, info, **kwargs):
		return CryptoCurrency.objects.all()

	def resolve_crypto_currency(self, info, symbol):
		return CryptoCurrency.objects.get(symbol=symbol.upper())

	def resolve_fiat_currencies(self, info, **kwargs):
		return FiatCurrency.objects.all()

	def resolve_fiat_currency(self, info, symbol):
		return FiatCurrency.objects.get(symbol=symbol.upper())

	def resolve_price_records(self, info, from_symbol, to_symbol):
		from_currency = FiatCurrency.objects.get(symbol=from_symbol.upper())
		to_currency = CryptoCurrency.objects.get(symbol=to_symbol.upper())
		return PriceRecord.objects.filter(from_id=from_currency.id, to_id=to_currency.id).all()

	def resolve_latest_price_record(self, info, from_symbol, to_symbol):
		from_currency = FiatCurrency.objects.get(symbol=from_symbol.upper())
		to_currency = CryptoCurrency.objects.get(symbol=to_symbol.upper())
		return PriceRecord.objects.filter(from_id=from_currency.id, to_id=to_currency.id).order_by('-updated_at').first()

# class Mutation(graphene.ObjectType):
# 	pass

schema = graphene.Schema(query=Query)
