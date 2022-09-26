from django.db import models
from django.contrib.auth.models import User
from tenants.models import TenantAwareModel

class Prospect(TenantAwareModel):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    join_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class Stock(TenantAwareModel):
    prospect = models.ForeignKey(Prospect, related_name='stocks', on_delete=models.CASCADE)
    stock = models.CharField(max_length=100)
    
    def __str__(self):
        return self.stock
    
    