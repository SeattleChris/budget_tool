
from django.urls import path
from .views import BudgetListView, BudgetDetailView, BudgetCreateView, TransactionCreateView

urlpatterns = [
    path('', BudgetListView.as_view(), name='budget_list'),
    path('<int:id>', BudgetDetailView.as_view(), name='budget_detail'),
    path('new', BudgetCreateView.as_view(), name='budget_create'),
    path('transaction/new', TransactionCreateView.as_view(), name='transaction_create'),
    path('transaction/new/<int:id>', TransactionCreateView.as_view(), name='transaction_create'),
    # above is correct to create on budget of id? 
]
