from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import index, transaction_list, add_transaction, edit_transaction, delete_transaction
from .viewsets import AccountViewSet, PartyViewSet, TransactionViewSet, JournalEntriesViewSet

# Create a router and register viewsets with it.
router = DefaultRouter()
router.register(r'accounts', AccountViewSet)
router.register(r'parties', PartyViewSet)
router.register(r'transactions', TransactionViewSet)
router.register(r'journal-entries', JournalEntriesViewSet)

# Define urlpatterns
urlpatterns = [
    path('', index, name='index'),  # Existing route
    path('api/', include(router.urls)),   # New API routes
    path('transactions/', transaction_list, name='transaction_list'),
    path('transactions/add/', add_transaction, name='add_transaction'),
    path('transactions/<int:pk>/edit/', edit_transaction, name='edit_transaction'),
    path('transactions/<int:pk>/delete/', delete_transaction, name='delete_transaction'),
]
