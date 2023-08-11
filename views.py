from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import ServiceRequest, Customer
from .forms import ServiceRequestForm, CustomerInfoForm

def submit_request(request):
    if request.method == 'POST':
        service_request_form = ServiceRequestForm(request.POST, request.FILES)
        if service_request_form.is_valid():
            customer, created = Customer.objects.get_or_create(email=service_request_form.cleaned_data['email'])
            service_request = service_request_form.save(commit=False)
            service_request.customer = customer
            service_request.save()
            return redirect('request_tracking')
    else:
        service_request_form = ServiceRequestForm()
    return render(request, 'submit_request.html', {'service_request_form': service_request_form})

def request_tracking(request):
    email = request.GET.get('email')
    if email:
        customer, created = Customer.objects.get_or_create(email=email)
        requests = ServiceRequest.objects.filter(customer=customer)
    else:
        requests = ServiceRequest.objects.all()
    return render(request, 'request_tracking.html', {'requests': requests})
