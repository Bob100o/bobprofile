# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import Contact
# # Create your views here.
# def contact(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')

#         Contact.objects.create(name=name, email=email, message=message)

#         return HttpResponse("Thank you for your contacting!")
#     return render(request, 'contact/contact.html')

# from django.shortcuts import render
# from django.http import HttpResponse
# from .forms import ContactForm

# def contact_view(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("Thank you for contacting!")
#     else:
#         form = ContactForm()

#     return render(request, 'contact/contact.html', {'form': form})


from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ContactForm  # Assuming you have a ContactForm
from django.conf import settings

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Extracting data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Sending email
            subject = 'Contact Form Submission'
            body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            from_email = email
            to_email = settings.EMAIL_HOST_USER   # The email address where you want to receive the form data
            
            # Send the email
            send_mail(subject, body, from_email, [to_email])

            return render(request,'contact/success.html')
   
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})


