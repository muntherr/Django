#
# Serialization and Deserialization:
# The first thing we need for our API is to provide a way to serialize model instances into representations.
# Serialization is the
# process profile making a streamable representation of the data which we can transfer over the network.
#


from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer): # Pass a built in serializer method
    class Meta:
        model = Book
        fields = ['id','title','description', 'price','isPublished']
