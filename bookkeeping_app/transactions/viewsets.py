# myapp/viewsets.py

from rest_framework import viewsets
from .models import Account, Party, Transaction, JournalEntries
from .serializers import AccountSerializer, PartySerializer, TransactionSerializer, JournalEntriesSerializer

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class PartyViewSet(viewsets.ModelViewSet):
    queryset = Party.objects.all()
    serializer_class = PartySerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class JournalEntriesViewSet(viewsets.ModelViewSet):
    queryset = JournalEntries.objects.all()
    serializer_class = JournalEntriesSerializer
