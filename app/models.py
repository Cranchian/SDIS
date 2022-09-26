from django.db import models
from django.contrib.auth.models import User
from django_mysql.models import ListCharField, ListTextField
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
    
    
class Employee(TenantAwareModel):
    id = models.AutoField(primary_key=True)
    empfname = models.CharField(max_length=100)
    emplname = models.CharField(max_length=100)
    empdept = models.CharField(max_length=100)
    emplocation = models.CharField(max_length=100, null=True)
    empphone = models.CharField(max_length=15, unique=True)
    empemail = models.CharField(max_length=100, unique=True)
    emppassword = models.CharField(max_length=125)
    empassignstatus = models.BooleanField(null=True)
    empintassignstatus = models.BooleanField(null=True)
    last_login = models.DateTimeField(null=True)
    last_logout = models.DateTimeField(null=True)
    languages = ListCharField(
        null=True,
        base_field=models.CharField(max_length=20),
        size=6,
        max_length=(20 * 7),  # 5 * 20 character nominals, plus commas
    )
    firstlan = models.CharField(max_length=255,null=True)
    seclan = models.CharField(max_length=255,null=True)
    thirdlan = models.CharField(max_length=255,null=True)
    source = ListCharField(
        base_field=models.CharField(max_length=20),
        size=6,
        max_length=(20 * 7),  # 5 * 20 character nominals, plus commas
        default='Organic'
    )
    columns_prospect = ListCharField(null=True,
        base_field=models.CharField(max_length=40),
        size=25,
        max_length=(50 * 25),  # 5 * 20 character nominals, plus commas
    )
    columns_investor = ListCharField(null=True,
        base_field=models.CharField(max_length=40),
        size=25,
        max_length=(50 * 25),  # 5 * 20 character nominals, plus commas
    )
    empnickname = models.CharField(max_length=100,null=True)
    profile_pic = models.ImageField(upload_to="ProfilePics/", null=True)
    empcreateddt = models.DateTimeField(auto_now_add=True)
    empupdateddt = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    deleted_by = models.IntegerField(null=True)
    reporting_to = models.CharField(max_length=100, null=True)
    cap = models.IntegerField(null=True)
    cap_reached = models.BooleanField(default=False)

    class Meta:
        db_table = 'employee'