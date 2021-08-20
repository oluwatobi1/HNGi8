from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from django.core.mail import send_mail
from django.template import RequestContext


# Create your views here.
def index(request):
    return HttpResponse("Email Sent")

def contact_details(request):
    # if this is a POST request we need to process the form data
    success = "Not Sent"
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            

            recipients = ['akintunlesetobi@gmail.com']
            if email:
                recipients.append(name)

            send_mail(subject, message, name, recipients)
            print('mail sent')
            form.save()
            success= "sent"
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponse('Success')


    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()

    return render(request, 'resume/index.html', {'form': form, "success":success})


