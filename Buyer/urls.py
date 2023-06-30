from django.urls import path
from .views import *

urlpatterns = [
    path("toCreateAccount", ToCreateAccount, name="toCreateAccount"),
    path("accountAction", AccountAction, name="accountAction"),
    path("toCartAction", ToCartAction, name="toCartAction"),
    path("tocart", ToCart, name="tocart"),
    path("toBuyerHome", ToBuyerHome, name="toBuyerHome"),
    path("changeProductQuantity", ChangeProductQuantity, name="changeProductQuantity"),
    path("removeCart", RemoveCart, name="removeCart"),
    path("toPlaceOrder", ToPlaceOrder, name="toPlaceOrder"),
    path("confirmOrder", ConfirmOrder, name="confirmOrder"),
    path("toOrders", ToOrders, name="toOrders"),
]
