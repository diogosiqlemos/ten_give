from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Tip, Tiptype
from django.views.generic import CreateView, DetailView, ListView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from datetime import date

# Create your views here.

def index(request):
    num_tips = Tip.objects.all().count()
    num_users = User.objects.all().count()

    context = {
        'num_tips':num_tips,
        'num_users':num_users,
    }

    return render(request, 'give10/index.html', context=context)


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('give10:index')
    template_name = 'give10/signup.html'


class ViewByUser(LoginRequiredMixin, ListView):
    model = Tip
    template_name = 'give10/profile.html'
    paginate_by = 5

    def get_queryset(self):
        return Tip.objects.filter(tip_giver = self.request.user).all()

class ViewAll(LoginRequiredMixin, ListView):
    model = Tip
    template_name = 'give10/alltips.html'
    paginate_by = 5

    def get_queryset(self):
        return Tip.objects.all()

class SearchView(ListView):
    model = Tip
    template_name = 'give10/search.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
        result = super(SearchView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            postresult = Tip.objects.filter(title__contains=query) | Tip.objects.filter(tiptype__name__contains=query) | Tip.objects.filter(tip_giver__username__contains=query)
            result = postresult
        else:
            result = None
        return result


class TiptypeCreate(LoginRequiredMixin, CreateView):
    model = Tiptype
    fields = '__all__'
    success_url = reverse_lazy('give10:index')

class TipCreate(LoginRequiredMixin, CreateView):
    model = Tip
    fields = ['title','tiptype','why_10','more_information','link']
    success_url = reverse_lazy('give10:index')

    def form_valid(self, form):
        form.instance.tip_giver = self.request.user
        form.instance.tip_date = date.today()
        return super().form_valid(form)

class TipUpdate(LoginRequiredMixin, UpdateView):
    model = Tip
    fields = ['title','tiptype','why_10','more_information','tip_date','link']
    success_url = reverse_lazy('give10:index')

    def form_valid(self, form):
        form.instance.tip_giver = self.request.user
        return super().form_valid(form)

class TipDeleteView(LoginRequiredMixin, DeleteView):
    model = Tip
    success_url = reverse_lazy('give10:index')

class TipDetail(LoginRequiredMixin, DetailView):
    model = Tip

