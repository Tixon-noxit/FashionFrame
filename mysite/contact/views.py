from django.views.generic import ListView
from main.models import BackgroungImage
from .models import Contact, AlertContact


class Contacts(ListView):
    model = Contact
    template_name = 'contact/contact.html'
    context_object_name = 'contact'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = 'Контакты'
        context['Show_Contact'] = Contact.objects.filter(id=1)
        context['backgroung_photo'] = BackgroungImage.objects.filter(id=1).first()
        context['Show_Alert'] = AlertContact.objects.all()
        return context
