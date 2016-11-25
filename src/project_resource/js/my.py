from django.shortcuts import render
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context

# Create your views here.

# Contactus Form:

from .forms import ContactForm

def contact(request):
    form = ContactForm

    return render(request, 'contact_temp.html', {'form':form})

    if request.method == 'POST':
        form = form(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('name')
            contact_email = request.POST.get('email')
            contact_no = request.POST.get('phone')
            form_content = request.POST.get('message')

            #email the Profile with the
            #content_information
            template = get_template('contact_template.txt')
            context = Context({
                'contact_name': name,
                'contact_email': email,
                'contact_no': phone,
                'form_content': message,
                })
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" + '',
                ['youremail@gmail.com'],
                headers = {'Reply-To': email}
                )
            email.send()
            return redirect('contact')
        return render(request, 'contact_temp.html', {
            'form': form,
            })