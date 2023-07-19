from django.views.generic import ListView

from main.models import BackgroungImage
from .models import CategoryPrice, AlertPrice


class ZhannaPrice(ListView):
    model = CategoryPrice
    template_name = 'price/price.html'
    context_object_name = 'price'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = 'Прайс-лист'
        context['backgroung_photo'] = BackgroungImage.objects.filter(id=1).first()
        context['comment'] = AlertPrice.objects.all()
        return context
