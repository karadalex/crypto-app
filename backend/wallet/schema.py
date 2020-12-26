import graphene
from graphene_django.types import DjangoObjectType
from .models import Transaction, Wallet, Asset
from .types import TransactionType, WalletType, AssetType


class Query(graphene.ObjectType):
	transactions = graphene.List(TransactionType, user_id=graphene.UUID())

	def resolve_transactions(self, info, user_id):
		return Transaction.objects.get(user__id=user_id)


# class Mutation(graphene.ObjectType):
# 	pass

schema = graphene.Schema(query=Query)
