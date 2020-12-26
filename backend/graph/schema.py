import tokens.schema
import wallet.schema


class Query(tokens.schema.Query, wallet.schema.Query, graphene.ObjectType):
    pass

class Mutation(tokens.schema.Mutation, wallet.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)