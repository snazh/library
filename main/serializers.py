import io

from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from .models import Book

'''
class BookModel:
    def __init__(self, title, description):
        self.title = title
        self.description = description
'''


class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    author_id = serializers.IntegerField()
    description = serializers.CharField()
    rating = serializers.FloatField()
    price = serializers.FloatField()
    time_create = serializers.DateTimeField()
    is_published = serializers.BooleanField(default=True)
    category_id = serializers.IntegerField()


'''
def encode():
    model = BookModel('Harry Potter', 'J. K. Rowling')
    model_sr = BookSerializer(model)
    print(model_sr.data, type(model_sr.data), sep='/n')
    json = JSONRenderer().render(model_sr.data)
    print(json)


def decode():
    stream = io.BytesIO(b'{"title":"Harry Potter","description":"J. K. Rowling"}')
    data = JSONParser().parse(stream)
    serializer = BookSerializer(data=data)
    serializer.is_valid()
    print(serializer.validated_data)
'''
