	
import graphene
from .models import User
from .types import UserType


class Query(graphene.ObjectType):
	users = graphene.List(UserType)
	user = graphene.Field(UserType, user__id=graphene.Int())
	
	def resolve_users(self, info, **kwargs):
		return User.objects.all()

	def resolve_user(self, info, user__id):
		return User.objects.first()

# class Mutation(graphene.ObjectType):
# 	pass

schema = graphene.Schema(query=Query)
	
