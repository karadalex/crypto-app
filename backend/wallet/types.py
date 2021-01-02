from graphene_django.types import DjangoObjectType
from django.contrib.auth.models import User
from .models import Transaction, Wallet, Asset
from django.contrib.contenttypes.models import ContentType


class ContentObjectType(DjangoObjectType):
	class Meta:
		model = ContentType

class TransactionType(DjangoObjectType):
	class Meta:
		model = Transaction
		fields = '__all__'

class WalletType(DjangoObjectType):
	class Meta:
		model = Wallet
		fields = '__all__'

class AssetType(DjangoObjectType):
	class Meta:
		model = Asset
		fields = '__all__'