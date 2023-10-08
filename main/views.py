from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import BookSerializer


# Create your views here.

class BookAPIView(APIView):
    def get(self, request):
        b = Book.objects.all()
        return Response({'Books': BookSerializer(b, many=True).data})

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(request.data)
        book_new = Book.objects.create(
            title=request.data['title'],
            description=request.data['description'],
            author_id=request.data['author'],
            rating=request.data['rating'],
            price=request.data['price'],
            category_id=request.data['category']
        )
        print({'Book': BookSerializer(book_new).data})
        return Response({'Book': BookSerializer(book_new).data})
