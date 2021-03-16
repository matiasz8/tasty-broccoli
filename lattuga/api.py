from tastypie.resources import ModelResource
from tastypie.constants import ALL
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie.authorization import Authorization
from lattuga.models import Book


class BookResource(ModelResource):
    class Meta:
        queryset = Book.objects.all()
        resource_name = "book"
        allowed_methods = ["get", "post", "put", "delete"]
        always_return_data = True
        filtering = {"title": ALL, "body": ALL}
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()
        # authorization = Authorization()

    def dehydrate_name(self, bundle):
        return bundle.data["title"].upper()
