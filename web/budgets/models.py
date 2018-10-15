from django.contrib.auth.models import User
from django.db import models
# Create your models here.


class Budget(models.Model):
    """ A user can have many budgets (each could represent a category of spending).
        We want to track how much of their budget they have already spent (or
        how much they have gone over their target budget). We will also track
        when this budget was added and modified.
    """
    # id = auto-created.
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='budgets')
    name = models.CharField(max_length=180, default='Untitled')
    total_budget = models.FloatField()
    # TODO: ?? remaining_budget: Float (@property calculation)
    remaining_budget = models.FloatField(default=0.0)
    date_added = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'<Budget: {self.name}>'


class Transaction(models.Model):
    """ Transactions are the individual deposits and withdraws for a given budget
        for the user on a specific declared Budget.
    """
    # id = auto-created.
    # assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions', null=True, blank=True)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name='transaction')
    description = models.TextField(blank=True, null=True)
    amount = models.FloatField()
    date_added = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    STATES = (
        ('WITHDRAWAL', 'Withdrawal'),
        ('DEPOSIT', 'Deposit'),
    )
    type = models.CharField(
        max_length=16,
        choices=STATES,
        default='WITHDRAWAL'
    )

    def __str__(self):
        return '{} | {}'.format(self.type, self.description)

    def __repr__(self):
        return '<Transaction: {} | {}>'.format(self.type, self.description)
