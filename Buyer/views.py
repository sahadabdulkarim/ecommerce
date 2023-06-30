from django.shortcuts import render

from .models import *
from django.http import HttpResponse, JsonResponse

# Create your views here.


def ToCreateAccount(request):
    return render(request, "Home/NewAccount.html")


def AccountAction(request):
    if request.method == "POST":
        buyer = Buyer_Tb.objects.create(
            FirstName=request.POST["fname"],
            LastName=request.POST["lname"],
            Gender=request.POST["gender"],
            Address=request.POST["address"],
            ContactNumber=request.POST["number"],
            City=request.POST["city"],
            State=request.POST["state"],
            Zip=request.POST["zip"],
            Email=request.POST["email"],
            Password=request.POST["password"],
        )
        buyer.save()
        return render(request, "Home/login.html")
    return HttpResponse("Invalid Request")


def ToCartAction(request):
    session = request.session["id"]
    if session:
        proId = request.GET.get("product")
        product = product_tb.objects.get(id=proId)
        user = Buyer_Tb.objects.get(id=session)
        exist = Cart_Tb.objects.filter(User=session, Product=product)
        if exist:
            quantity = int(exist[0].Quantity) + 1
            total = int(exist[0].Total) + int(product.Price)
            exist.update(Quantity=quantity, Total=total)
            message = "updated"
        else:
            cart = Cart_Tb(User=user, Product=product, Quantity=1, Total=product.Price)
            cart.save()
            message = "added"
        return HttpResponse(message)
    else:
        return render(request, "Home/Login.html")


def ToCart(request):
    session = request.session["id"]
    if session:
        cart = Cart_Tb.objects.filter(User=session, Status="Pending")
        totalPrice = 0
        for products in cart:
            totalPrice = totalPrice + int(products.Total)
        return render(request, "Buyer/MyCart.html", {"cart": cart, "total": totalPrice})
    else:
        return render(request, "Home/Login.html")


def ToBuyerHome(request):
    session = request.session["id"]
    if session:
        product = product_tb.objects.all()
        return render(request, "Buyer/Index.html", {"product": product})
    else:
        return render(request, "Home/Login.html")


def ChangeProductQuantity(request):
    session = request.session["id"]
    if session:
        cartId = request.GET.get("cart")
        count = request.GET.get("count")
        carts = Cart_Tb.objects.filter(User=session)
        Cart = Cart_Tb.objects.filter(User=session, id=cartId)
        if Cart:
            if int(Cart[0].Quantity) == 1 and int(count) == -1:
                update = Cart.delete()
                data = {"removeProduct": True}
            else:
                quantity = int(Cart[0].Quantity) + int(count)
                total = int(Cart[0].Product.Price) * quantity
                update = Cart.update(Quantity=quantity, Total=total)
                message = "Updated"
                userCart = Cart_Tb.objects.filter(User=session)
                totalPrice = 0
                for products in userCart:
                    totalPrice = totalPrice + int(products.Total)
                data = {"total": totalPrice}
            return JsonResponse(data)
        else:
            message = "oops, something worng"
            return HttpResponse(message)
    else:
        return render(request, "Home/Login.html")


def RemoveCart(request):
    session = request.session["id"]
    if session:
        cartId = request.GET.get("cart")
        remove = Cart_Tb.objects.filter(id=cartId).delete()
        return HttpResponse()
    else:
        return render(request, "Home/Login.html")


def ToPlaceOrder(request):
    session = request.session["id"]
    if session:
        cart = Cart_Tb.objects.filter(User=session)
        totalPrice = 0
        for products in cart:
            totalPrice = totalPrice + int(products.Total)
        return render(request, "Buyer/PlaceOrder.html", {"total": totalPrice})
    else:
        return render(request, "Home/Login.html")


def ConfirmOrder(request):
    session = request.session["id"]
    if session:
        user = Buyer_Tb.objects.get(id=session)
        cart = Cart_Tb.objects.filter(User=session, Status="Pending")
        totalPrice = 0
        for product in cart:
            productid = product_tb.objects.get(id=product.Product.id)
            totalPrice = totalPrice + int(product.Total)
            data = Order_Tb.objects.filter(
                Product=productid, User=session, Status="Pending"
            )
            if data:
                for d in data:
                    totalQuantity = int(d.Quantity) + int(product.Quantity)
                    data.update(Quantity=totalQuantity)
            else:
                order = Order_Tb(
                    User=user,
                    Product=productid,
                    Quantity=product.Quantity,
                    Total=totalPrice,
                )
                order.save()
            count = int(productid.Quantity) - int(product.Quantity)
            product_tb.objects.filter(id=productid.id).update(Quantity=count)
            totalPrice = totalPrice + int(product.Total)
            Cart_Tb.objects.filter(id=product.id).delete()
        return render(
            request, "Buyer/PlaceOrder.html", {"user": session, "total": totalPrice}
        )
    else:
        return render(request, "Home/Login.html")


def ToOrders(request):
    session = request.session["id"]
    if session:
        order = Order_Tb.objects.filter(User=session)
        totalPrice = 0
        for product in order:
            productCount = product_tb.objects.filter(id=product.Product.id)
            totalPrice = totalPrice + int(product.Product.Price) * int(product.Quantity)
        user = Buyer_Tb.objects.filter(id=session)
        return render(
            request,
            "Buyer/BuyerOrder.html",
            {"order": order, "total": totalPrice, "user": user},
        )
    else:
        return render(request, "Home/Login.html")
