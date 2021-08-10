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


def validateCustomer(customer):
    error_message = None
    if not customer.firstname:
        error_message = "First Name required!!"
    elif len(customer.firstname)<4:
        error_message = "First name must be 4 character long!"
    elif not customer.lastname:
        error_message = "Last Name required!!"
    elif len(customer.lastname) < 4:
        error_message = "Last name must be 4 character long!"
    elif not customer.phone:
        error_message = "Phone Number required!!"
    elif len(customer.phone) < 10:
        error_message = "Last name must be 10 character long!"
    elif len(customer.password) < 6:
        error_message = "Password must be 6 char long!"
    elif len(customer.email) < 5:
        error_message = "Email must be 5 char long!!"
    elif customer.isExits():
        error_message = "Email already exits!"
    
    return error_message


def registerUser(request):
    postData = request.POST
    first_name = postData.get('firstname')
    last_name = postData.get('lastname')
    phone = postData.get('phone')
    email = postData.get('email')
    password = postData.get('password')

    # validataion
    value = {
        'first_name': first_name, 'last_name': last_name,
        'phone': phone, 'email': email
    }

    error_message = None

    customer = Customer(firstname=first_name, lastname=last_name,
                        phone=phone, email=email, password=password)

    error_message = validateCustomer(customer)

    # saving
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


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        return registerUser(request)


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password) 
            if flag:
                return redirect('homepage')
            else:
                error_message = "Email or Password Invalid!!"
        else:
            error_message = "Email or Password Invalid!!"
        return render(request, 'login.html', {'error': error_message})