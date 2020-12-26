import graphene
from graphene_django.types import DjangoObjectType


class Query(graphene.ObjectType):
	pass

class Mutation(graphene.ObjectType):
	pass

schema = graphene.Schema(query=Query, mutation=Mutation)
	
