from graphene.test import Client
from pytest import fixture

from .schema import schema


@fixture
def client(db):
    return Client(schema)
