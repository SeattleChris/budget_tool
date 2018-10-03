from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from .models import Budget, Transaction

# Create your views here.


class BudgetListView(LoginRequiredMixin, ListView):
    """ A user may have a variety of Budgets, such as categories for different
        aspects they want to track. We want to be able to see and select them.
    """
    template_name = 'budgets/budget_list.html'
    context_object_name = 'budgets'
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['budgets'] = Budget.objects.filter(
            budget__user__username=self.request.user.username)
        return context

    def get_queryset(self):
        return Budget.objects.filter(
            user__username=self.request.user.username)

    # Inherits .as_view(self):


class BudgetDetailView(LoginRequiredMixin, DetailView):
    """ Within a given Budget there are a vareity of transactions (deposits,
        withdrawls). Seeing the details of a given Budget is looking at these
        transactions.
    """
    template_name = 'budgets/budget_detail.html'
    context_object_name = 'budget'
    login_url = reverse_lazy('login')
    pk_url_kwarg = 'id'

    def get_queryset(self):
        return Transaction.objects.filter(
            budget__user__username=self.request.user.username)

    # Inherits .as_view(self):
