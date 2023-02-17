from re import template
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, DetailView
from .models import *
from .forms import CallbackForm, FoodModelForm
from django.views.generic.edit import FormMixin


data = {
    'location': 'Mirabad st. 27/3B',
    'phone': '+998994287796',
    'mail': 'n.soatov@bk.ru'
}

# class HomeView(ListView):
#     template_name = 'index.html'
#     model = Category
#     context_object_name = 'categories'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["covers"] = Cover.objects.all()
#         return context


# def food_by_category(request, category_id):
#     category = Category.objects.get(id=category_id)
#     food_items = FoodModel.objects.filter(category=category)
#     context = {'category': category, 'food_items': food_items,
#                'covers': Cover.objects.all(), 'data': data, 'count': 'count'}
#     return render(request, 'fruit.html', context)


class FoodDetailView(FormMixin, DetailView):
    model = FoodModel
    template_name = "fruit.html"
    context_object_name = 'post'
    form_class = FoodModelForm
    success_url = reverse_lazy('#')

    def get(self, request, * args, **kwargs):
        # print(request.GET['search'])
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_valid(form)
    
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.post = self.get_object()
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.all()
        context['covers'] = Cover.objects.all()
        context['data'] = data
        context['food_items'] = FoodModel.objects.filter(category=category)
        return context
    
    


class HomeCreateView(CreateView):
    # model = Category
    template_name = "index.html"
    form_class = CallbackForm
    success_url = reverse_lazy('home')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["covers"] = Cover.objects.all()
        context['categories'] = Category.objects.all()
        context['data'] = data 
        return context
