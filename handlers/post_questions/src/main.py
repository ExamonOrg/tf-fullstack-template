from mongoengine import connect
from .ingest import Ingest


def run():
    domain = "examon.lqzutab.mongodb.net"
    user = 'examon_writer'
    protocol = 'mongodb+srv'
    password = 'b1DPMW4hQjVgbVKt'
    uri = f"{protocol}://{user}:{password}@{domain}/?retryWrites=true&w=majority"

    db_name = "examon"
    connect(db_name, host=uri, alias="default")
    Ingest.run()
