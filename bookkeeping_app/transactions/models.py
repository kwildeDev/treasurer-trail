from django.db import models
from django.contrib.auth.models import User # Import Django's built-in User model

# Create your models here.

class Account(models.Model):
    account_id = models.BigAutoField(primary_key=True)
    account_name = models.CharField(max_length=50)
    description = models.TextField()
    account_type = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return self.account_name

class Party(models.Model): # Payer/Payee Table
    party_id = models.BigAutoField(primary_key=True)
    party_name = models.CharField(max_length=255)
    party_type = models.CharField(max_length=50)
    contact_details = models.TextField()

    def __str__(self):
        return self.party_name

# the transaction model will have foreign keys to both 'Account' and 'Party'
# allowing transactions to be linked to specific accounts and parties

class Transaction(models.Model):
    transaction_id = models.BigAutoField(primary_key=True)
    transaction_date = models.DateField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField() # Descriptions can be lengthy
    party = models.ForeignKey(Party, on_delete=models.CASCADE) # reference to party model
    category = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE) # reference to User model

    def __str__(self):
        return f"{self.transaction_date} - {self.description} - {self.amount} - {self.user}"
    

class JournalEntries(models.Model):
    journal_entry_id = models.BigAutoField(primary_key=True)
    transaction = models.ForeignKey(Transaction,on_delete=models.CASCADE) # reference to transaction model
    entry_date = models.DateField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE) # reference to account model
    debit_amount = models.DecimalField(max_digits=12, decimal_places=2)
    credit_amount = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.entry_date} - {self.transaction} - {self.account} - {self.debit_amount} - {self.credit_amount}"