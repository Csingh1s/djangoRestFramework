from django.shortcuts import render
from rbasis.views import *

from .models import *
from .serializers import *

# Create your views here.
class receiptView(ShAPIView):
    queryset = receipt.objects.all()
    serializer_class = receiptSerializer

    ########## get all receipts ############
    def list(self, request, *args, **kwargs):
        return super().list(request, args, kwargs)

    ########## create a new receipt ############
    def create(self, request, *args, **kwargs):
        return super().create(request, args, kwargs)

    ########## get particular user ############
    def retrieve(self, request, *args, **kwargs):
        try:
            name = kwargs["pk"]
            self.queryset = receipt.objects.filter(user_name=name)
            self.serializer_class = receiptSerializer
            return super().list(request, args, kwargs)
        except Exception as e:
            print (e)

    ########## update receipt ############
    def update(self, request, *args, **kwargs):
        return super().update(request, args, kwargs)

    ########## delete receipt ############
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, args, kwargs)

    pass

class userView(ShAPIView):
    queryset = user.objects.all()
    serializer_class = userSerializer
    pass

class ingredientView(ShAPIView):
    queryset = ingredient.objects.all()
    serializer_class = ingredientSerializer
    pass

class stepView(ShAPIView):
    queryset = step.objects.all()
    serializer_class = stepSerializer
    pass
