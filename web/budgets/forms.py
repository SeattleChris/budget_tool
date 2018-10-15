from django.forms import ModelForm
from .models import Budget, Transaction


class BudgetForm(ModelForm):
    """ Will generate a form for input on whichever fields we include.
        Using Budget model, since we are adding a budget category
    """
    class Meta:
        model = Budget
        fields = ['name', 'total_budget']


class TransactionForm(ModelForm):
    """ Will generate a form for input on whichever fields we include.
        Using Transaction model, since we are adding a withdraw or deposit
    """
    class Meta:
        model = Transaction
        fields = ['description', 'type', 'amount']
        # TODO: maybe budget should be removed from fields once we are passing correct budget
