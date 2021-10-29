from django.db import models


# Create your models here.

class Consumerlist(models.Model):
     account_id = models.CharField(max_length = 45,  primary_key=True, default = ' ')
     meter_number = models.CharField(max_length = 45, blank = True, null = True)
     first_name = models.CharField(max_length = 45, blank = True, null = True)
     middle_name = models.CharField(max_length = 45, blank = True, null = True)
     last_name = models.CharField(max_length = 45, blank = True, null = True)
     address = models.CharField(max_length = 45, blank = True, null = True)

     def __str__(self):
        return self.Consumerlist

     class Meta:
         db_table = 'consumerinfo'


    
