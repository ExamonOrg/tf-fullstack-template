from graphene_mongo import MongoengineObjectType
from graphene.relay import Node

from ..documents.question import Question as QuestionDocument


class Question(MongoengineObjectType):
    class Meta:
        collection = 'questions'
        model = QuestionDocument
        interfaces = (Node,)
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith']
        }
