from django.http import JsonResponse
from .models import *
from django.shortcuts import render
from Buyer.models import *
from django.contrib.auth import logout

# Create your views here.


def ToIndex(request):
    product = product_tb.objects.all()
    return render(request, "Home/Index.html", {"product": product})


def ToLogin(request):
    return render(request, "Home/Login.html")


def LoginAction(request):
    user = Admin_Tb.objects.filter(
        Email=request.POST["email"], Password=request.POST["password"]
    )
    if user.count() > 0:
        request.session["id"] = user[0].id
        product = product_tb.objects.all()
        return render(request, "Admin/Index.html", {"product": product})
    else:
        user = Buyer_Tb.objects.filter(
            Email=request.POST["email"], Password=request.POST["password"]
        )
        if user.count() > 0:
            request.session["id"] = user[0].id
            product = product_tb.objects.all()
            return render(request, "Buyer/Index.html", {"product": product})
        else:
            return render(request, "Home/Login.html")


def ToNewCategory(request):
    session = request.session["id"]
    if session:
        categories = Category_Tb.objects.all()
        return render(request, "Admin/NewCategory.html", {"category": categories})
    else:
        return render(request, "Home/Login.html")


def CategoryAction(request):
    session = request.session["id"]
    if session:
        category = Category_Tb(Name=request.POST["category"])
        category.save()
        categories = Category_Tb.objects.all()
        return render(request, "Admin/NewCategory.html", {"category": categories})
    else:
        return render(request, "Home/Login.html")


def ToViewCategory(request):
    session = request.session["id"]
    if session:
        categories = Category_Tb.objects.all()
        return render(request, "Admin/AllCategory.html", {"category": categories})
    else:
        return render(request, "Home/Login.html")


def ToHome(request):
    product = product_tb.objects.all()
    return render(request, "Admin/Index.html", {"product": product})


def ToProduct(request):
    session = request.session["id"]
    if session:
        products = product_tb.objects.all()
        return render(request, "Admin/Product.html", {"product": products})
    else:
        return render(request, "Home/Login.html")


def ToAdminOrders(request):
    session = request.session["id"]
    if session:
        orders = Order_Tb.objects.all()
        return render(request, "Admin/Orders.html", {"order": orders})
    else:
        return render(request, "Home/Login.html")


def ToAdminPendingOrders(request):
    session = request.session["id"]
    if session:
        orders = Order_Tb.objects.filter(Status="Pending")
        return render(request, "Admin/Orders.html", {"order": orders})
    else:
        return render(request, "Home/Login.html")


def ToApproveOrder(request, oid):
    session = request.session["id"]
    if session:
        Order_Tb.objects.filter(id=oid).update(Status="Approved")
        orders = Order_Tb.objects.all()
        return render(request, "Admin/Orders.html", {"order": orders})
    else:
        return render(request, "Home/Login.html")


def ToAllBuyers(request):
    session = request.session["id"]
    if session:
        buyers = Buyer_Tb.objects.all()
        return render(request, "Admin/Buyer.html", {"buyer": buyers})
    else:
        return render(request, "Home/Login.html")


def Sign_Out(request):
    logout(request)
    return render(request, "Home/Login.html")


def ToMyProduct(request):
    session = request.session["id"]
    if session:
        products = product_tb.objects.filter(Admin=session)
        return render(request, "Admin/MyProduct.html", {"product": products})
    else:
        return render(request, "Home/Login.html")


def ToNewProduct(request):
    session = request.session["id"]
    if session:
        category = Category_Tb.objects.all()
        return render(request, "Admin/NewProduct.html", {"category": category})
    else:
        return render(request, "Home/Login.html")


def ProductAction(request):
    session = request.session["id"]
    if session:
        productImage = ""
        if request.FILES:
            productImage = request.FILES["image"]
        else:
            productImage = "no_image"
        seller = Admin_Tb.objects.get(id=session)
        category = Category_Tb.objects.get(id=request.POST["category"])
        product = product_tb(
            Category=category,
            Admin=seller,
            Name=request.POST["name"],
            Price=request.POST["price"],
            Details=request.POST["details"],
            Quantity=request.POST["quantity"],
            Image=productImage,
        )
        product.save()
        category = Category_Tb.objects.all()
        return render(request, "Admin/NewProduct.html", {"category": category})


def ToMyOrders(request):
    session = request.session["id"]
    product = product_tb.objects.filter(Admin=session)
    data = []
    for id in product:
        orders = Order_Tb.objects.filter(Product=id.id).exclude(Status="Pending")
        for order in orders:
            total = int(order.Quantity) * int(order.Product.Price)
            data.append(
                {
                    "id": order.id,
                    "Fname": order.User.FirstName,
                    "lName": order.User.LastName,
                    "Address": order.User.Address,
                    "City": order.User.City,
                    "State": order.User.State,
                    "Number": order.User.ContactNumber,
                    "Category": order.Product.Category.Name,
                    "Name": order.Product.Name,
                    "Image": order.Product.Image.url,
                    "Quantity": order.Quantity,
                    "Total": total,
                    "Date": order.Date,
                    "Status": order.Status,
                }
            )
    print(data)
    return render(request, "Admin/MyOrders.html", {"order": data})


def UpdateOrder(request, oid):
    session = request.session["id"]
    update = Order_Tb.objects.filter(id=oid).update(Status="Dispatched")
    product = product_tb.objects.filter(Admin=session)
    data = []
    for id in product:
        orders = Order_Tb.objects.filter(Product=id.id).exclude(Status="Pending")
        for order in orders:
            total = int(order.Quantity) * int(order.Product.Price)
            data.append(
                {
                    "id": order.id,
                    "Fname": order.User.FirstName,
                    "lName": order.User.LastName,
                    "Address": order.User.Address,
                    "City": order.User.City,
                    "State": order.User.State,
                    "Number": order.User.ContactNumber,
                    "Category": order.Product.Category.Name,
                    "Name": order.Product.Name,
                    "Image": order.Product.Image.url,
                    "Quantity": order.Quantity,
                    "Total": total,
                    "Date": order.Date,
                    "Status": order.Status,
                }
            )
    print(data)
    return render(request, "Admin/MyOrders.html", {"order": data})


def ValidateEmail(request):
    Email = request.GET.get("data")
    data = {"is_taken": Buyer_Tb.objects.filter(Email=Email).exists()}
    if data["is_taken"]:
        data["error_msg"] = "Already Exists"
    else:
        data = {"is_taken": Admin_Tb.objects.filter(Email=Email).exists()}
        if data["is_taken"]:
            data["error_msg"] = "Already Exists"
    return JsonResponse(data)
