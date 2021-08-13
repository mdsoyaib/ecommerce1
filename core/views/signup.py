from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from core.models.customer import Customer
from django.contrib.auth.hashers import make_password, check_password
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
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

        error_message = self.validateCustomer(customer)

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

    def validateCustomer(self, customer):
        error_message = None
        if not customer.firstname:
            error_message = "First Name required!!"
        elif len(customer.firstname) < 4:
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
