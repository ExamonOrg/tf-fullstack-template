from graphene_mongo import MongoengineObjectType
from graphene.relay import Node

from ..documents.metrics import Metrics as MetricsDocument


class Metrics(MongoengineObjectType):
    class Meta:
        model = MetricsDocument
        interfaces = (Node,)
