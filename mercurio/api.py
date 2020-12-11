from tastypie.resources import ModelResource
from tastypie.constants import ALL

from mercurio.models import Book


class BookResource(ModelResource):
    class Meta:
        queryset = Book.objects.all()
        resource_name = "book"
        allowed_methods = ["get", "post", "put"]
        always_return_data = True
        filtering = {"title": ALL, "body": ALL}

    def dehydrate_name(self, bundle):
        return bundle.data["title"].upper()
