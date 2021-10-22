from django.db import models

# Create your models here.
class account_info(models.Model):
    accountinfoid = models.CharField(max_length = 45,primary_key = True)
    firstname = models.CharField(max_length = 45)

    class Meta:
        db_table = "accountinfo_table"
