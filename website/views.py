from django.shortcuts import render
from django.views.generic.edit import FormView
from website.forms import ContactForm
from django.core.mail import EmailMessage
from django.core.mail import BadHeaderError
import smtplib

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/contact'
    
    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        tel = form.cleaned_data.get('telephone')
        message = form.cleaned_data.get('message')

        content = f'{name} / {email} dijo: '
        content += f'\n\n{message}'
        content += f'\n\n Telefono: {tel}'

        email_subject = 'Mensaje de Leiva Equipamientos'
        to_email = 'hola@luciano.im'
        
        try:
            mail = EmailMessage(email_subject, content, to=[to_email], from_email=email, reply_to=[email])
            mail.send()
        except BadHeaderError:
            print('Invalid header found.')
        except smtplib.SMTPException:
            print('Error: Unable to send email')

        return super(IndexView, self).form_valid(form)