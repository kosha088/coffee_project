from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from coffee_web.models import Coffee, OrderCoffee, OrderCoffeeList
from coffee_web.forms import OrderCoffeeForm, OrderCoffeeListForm
from blog.models import Post


@login_required(login_url='/login')
def index(request):
    coffee = Coffee.objects.all()
    posts = Post.objects.all()
    context = {
        'coffee_list': coffee,
        'form' : OrderCoffeeForm(),
        'form2': OrderCoffeeListForm(),
        'posts' : posts
        
    }
    return render(request=request, template_name='coffee_web/index.html', context=context)
  
@login_required(login_url='/login')
def create(request):
    form = OrderCoffeeForm(request.POST)
    # form2 = OrderCoffeeListForm(request.POST)
    order = form.save()
    coffee= Coffee.objects.get(id=request.POST.get('coffee'))
    quantity = request.POST.get('quantity')
    paid = request.POST.get('paid')
    print(order.first_name, order.id)
    if paid is None:
        OrderCoffeeList.objects.create(order=order, coffee= coffee, quantity=quantity)
    else:
        OrderCoffeeList.objects.create(order=order, coffee= coffee, quantity=quantity, paid=True)
    return redirect('main')

