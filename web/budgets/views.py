from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Budget, Transaction
from .forms import BudgetForm, TransactionForm
# Create your views here.


class BudgetListView(LoginRequiredMixin, ListView):
    """ A user may have a variety of Budgets, such as categories for different
        aspects they want to track. We want to be able to see and select them.
    """
    template_name = 'budgets/budget_list.html'
    model = Budget
    context_object_name = 'budgets'
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        """ Get all transactions for this user (??)
            May need additional filters or setup differently
        """
        context = super().get_context_data(**kwargs)
        context['transactions'] = Transaction.objects.filter(
            budget__user__username=self.request.user.username)
        return context

    def get_queryset(self):
        """ We only want to list the Budgest owned by the current user.
        """
        return Budget.objects.filter(
            user__username=self.request.user.username)

    # Inherits .as_view(self):


class BudgetDetailView(LoginRequiredMixin, DetailView):
    """ Within a given Budget there are a vareity of transactions (deposits,
        withdrawls). Seeing the details of a given Budget is looking at these
        transactions.
    """
    template_name = 'budgets/budget_detail.html'
    model = Transaction
    context_object_name = 'transaction'
    login_url = reverse_lazy('login')
    pk_url_kwarg = 'id'
    # TODO: Need to manage when the budget has no items? Maybe Not really ...
    # Why does 'Food' not show correctly?

    def get_context_data(self, **kwargs):
        """ Get all transactions for this user (??)
            May need additional filters or setup differently
        """
        context = super().get_context_data(**kwargs)
        context['transactions'] = Transaction.objects.filter(
            budget__user__username=self.request.user.username)
        return context

    def get_queryset(self):
        """ Associate the user (or Budget?) for this Transaction
        """
        return Transaction.objects.filter(
            budget__user__username=self.request.user.username)
        # TODO: Is there an issue to fix above here?

    # Inherits .as_view(self):


class BudgetCreateView(LoginRequiredMixin, CreateView):
    """ Control the display and handling of the user input form for creating
        a new budget category.
    """
    template_name = 'budgets/budget_create.html'
    model = Budget
    form_class = BudgetForm
    success_url = reverse_lazy('budget_list')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        """ Associate the user for this Budget
        """
        form.instance.user = self.request.user
        return super().form_valid(form)

    # Inherits .as_view(self):


class TransactionCreateView(LoginRequiredMixin, CreateView):
    """ Control the display and handling of the user input form for creating
        a new Transaction (within a Budget category).
    """
    template_name = 'budgets/transaction_create.html'
    model = Transaction
    form_class = TransactionForm
    success_url = reverse_lazy('budget_list')
    login_url = reverse_lazy('login')
    pk_url_kwarg = 'id'

    def form_valid(self, form):
        """ Associate the Budget for this Transaction (currently set as user?)
        """
        form.instance.user = self.request.user
        # form.instance.budget_id = self.request.pk_url_kwarg
        return super().form_valid(form)

    # Inherits .as_view(self):
