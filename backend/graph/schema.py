import graphene
import users.schema
# import tokens.schema
# import wallet.schema


class Query(
	users.schema.Query,
	graphene.ObjectType
):
	pass

# class Mutation(users.schema.Mutation, graphene.ObjectType):
# 	pass


schema = graphene.Schema(query=Query)