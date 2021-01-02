import graphene
from graphene_django.types import DjangoObjectType
from users.models import User
from .models import Transaction, Wallet, Asset
from .types import TransactionType, WalletType, AssetType


class Query(graphene.ObjectType):
	transactions = graphene.List(TransactionType, user_id=graphene.UUID())

	user_assets = graphene.List(AssetType)

	def resolve_transactions(self, info, user_id):
		return Transaction.objects.get(user__id=user_id)

	def resolve_user_assets(self, info, **kwargs):
		wallet = Wallet.objects.first()
		return Asset.objects.filter(wallet=wallet).all()


# class Mutation(graphene.ObjectType):
# 	pass

schema = graphene.Schema(query=Query)
