from dataclasses import fields
from pyexpat import model
import graphene
from graphene_django import DjangoObjectType
from .models import Books

class BooksType(DjangoObjectType):
    class Meta:
        model = Books
        fields = ('id','title','excerpt')

class Query(graphene.ObjectType):
    all_books = graphene.List(BooksType)
    retrive_book = graphene.Field(BooksType,id = graphene.Int())
    test_str = graphene.String(default_value="Hi!")

    def resolve_all_books(root,info):
        return Books.objects.all()

    def resolve_retrive_book(root,info,id):
        return Books.objects.get(pk=id)

schema = graphene.Schema(query=Query)