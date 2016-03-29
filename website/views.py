from django.views.generic.edit import FormView
from website.forms import ContactForm
from django.core.mail import send_mail

class ContactView(FormView):
	template_name = 'contact.html'
	form_class = ContactForm
	success_url = '/contact'

	def form_valid(self, form):
		message = "{0} / {1} dijo: ".format(form.cleaned_data.get('name'),form.cleaned_data.get('email'))
		message += "\n\n{0}".format(form.cleaned_data.get('message'))
		message += "\n\n Telefono: {0}".format(form.cleaned_data.get('telephone'))

		send_mail('Mensaje de leivaequipamientos.com.ar',message,'luchisds@gmail.com',['luchisds@gmail.com'])
		return super(ContactView, self).form_valid(form)