from coffee_web.models import Coffee, OrderCoffee, OrderCoffeeList
from coffee_web.forms import OrderCoffeeForm

from django.views.generic import(
    ListView,
    CreateView
)

class IndexView(ListView):
    template_name = 'coffee_web/index.html'
    model = Coffee
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['coffee_list']=Coffee.objects.all()
        context['form'] = OrderCoffeeForm()
        return context

class CreateOrderView(CreateView):
    model = OrderCoffee
    # model = OrderCoffee
    # model = OrderCoffeeList
    fields = ['first_name', 'last_name', 'address', 'city', 'email']
    http_method_names =["POST"]
    success_url = ''

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

