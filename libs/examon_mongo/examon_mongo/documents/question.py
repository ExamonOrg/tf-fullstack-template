from mongoengine import Document
from mongoengine.fields import (
    ListField,
    StringField,
    EmbeddedDocumentField
)

from .metrics import Metrics


class Question(Document):
    name = StringField()
    tags = ListField(StringField())
    unique_id = StringField()
    internal_id = StringField()
    function_src = StringField()
    repository = StringField()
    hints = ListField(StringField())
    print_logs = ListField(StringField())
    correct_answer = StringField()
    metrics = EmbeddedDocumentField(Metrics)
