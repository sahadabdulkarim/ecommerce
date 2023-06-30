from django.urls import path, re_path
from .views import *

urlpatterns = [
    path("", ToIndex),
    path("toLogin", ToLogin, name="toLogin"),
    path("loginAction", LoginAction, name="loginAction"),
    path("toNewCategory", ToNewCategory, name="toNewCategory"),
    path("categoryAction", CategoryAction, name="categoryAction"),
    path("toViewCategory", ToViewCategory, name="toViewCategory"),
    path("toHome", ToHome, name="toHome"),
    path("adminToProduct", ToProduct, name="adminToProduct"),
    path("toAdminOrders", ToAdminOrders, name="toAdminOrders"),
    path("toAdminPendingOrders", ToAdminPendingOrders, name="toAdminPendingOrders"),
    re_path(r"^toApproveOrder/(?P<oid>\d+)/$", ToApproveOrder, name="toApproveOrder"),
    path("toAllBuyers", ToAllBuyers, name="toAllBuyers"),
    path("sign_Out", Sign_Out, name="sign_Out"),
    path("validate_email", ValidateEmail, name="validate_email"),
    path("toIndex", ToIndex, name="toIndex"),
    path("toMyProduct", ToMyProduct, name="toMyProduct"),
    path("toNewProduct", ToNewProduct, name="toNewProduct"),
    path("productAction", ProductAction, name="productAction"),
    path("toMyOrders", ToMyOrders, name="toMyOrders"),
    re_path(r"^updateOrder/(?P<oid>\d+)/$", UpdateOrder, name="updateOrder"),
]
