from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Product, Category
from .models.customer import Customer
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.


def index(request):
    product = None
    category = Category.get_all_category()
    categoryID = request.GET.get('category')
    if categoryID:
        product = Product.get_all_products_by_category_id(categoryID)
    else:
        product = Product.get_all_products()
    data = {}
    data['product'] = product
    data['category'] = category
    return render(request, "index.html", data)


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        #validataion
        value = {
            'first_name': first_name, 'last_name': last_name,
            'phone': phone, 'email': email
        }

        error_message = None

        customer = Customer(firstname=first_name, lastname=last_name, 
        phone=phone, email=email, password=password)

        if(not first_name):
            error_message = "First Name required!!"
        elif len(first_name)<4:
            error_message = "First name must be 4 character long!"
        elif not last_name:
            error_message = "Last Name required!!"
        elif len(last_name) < 4:
            error_message = "Last name must be 4 character long!"
        elif not phone:
            error_message = "Phone Number required!!"
        elif len(phone) < 10:
            error_message = "Last name must be 10 character long!"
        elif len(password) < 6:
            error_message = "Password must be 6 char long!"
        elif len(email) < 5:
            error_message = "Email must be 5 char long!!"
        elif customer.isExits():
            error_message = "Email already exits!"

        #saving
        if not error_message:
            print(first_name, last_name, phone, email, password)

            customer.password = make_password(customer.password)

            customer.register()

            # return redirect(index)
            return redirect("homepage")

        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)