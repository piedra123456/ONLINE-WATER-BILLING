from django.db import models


# Create your models here.

class signin(models.Model):
    meter_num = models.CharField(max_length = 45, primary_key = True)

    def _str_(self):
        return self.meter_num


class customer_info(models.Model):
    meter_num = models.CharField(max_length = 45, primary_key = True)
    acc_id = models.CharField(max_length = 45)
    name = models.CharField(max_length = 45)
    address = models.CharField(max_length = 45)
    cell_num = models.CharField(max_length = 45)
    zipcode = models.CharField(max_length = 45)
    country = models.CharField(max_length = 45)

    def _str_(self):
        return self.customer_info

    class Meta:
        db_table = 'customerinfo'



class company_info(models.Model):
    name = models.CharField(max_length = 45)
    address = models.CharField(max_length = 45)
    phone = models.CharField(max_length = 45)
    zipcode = models.CharField(max_length = 45)
    country = models.CharField(max_length = 45)

    def _str_(self):
        return self.company_info

    class Meta:
        db_table = 'companyinfo'



class bill_info(models.Model):
        date = models.CharField(max_length = 45)
        payment_sched = models.CharField(max_length = 45)
        posted_on = models.CharField(max_length = 45)
        posted_by = models.TextField(default = " ")

        def _str_(self):
            return self.bill

        class Meta:
            db_table = 'billinfo'



class latest_bill(models.Model):
    current_reading = models.FloatField(max_length = 45)
    prev_reading = models.FloatField(max_length = 45)
    usage = models.FloatField(max_length = 45)
    bill = models.FloatField(max_length = 45)
    penalty = models.FloatField(max_length = 45)
    total_bill = models.FloatField(max_length = 45)
    prev_due = models.FloatField(max_length = 45)

    def _str_(self):
        return self.latest_bill

    class Meta:
        db_table = 'latestbill'



class usage_and_payment_history(models.Model):
    acc_id = models.CharField(max_length = 45)
    years = models.BigIntegerField()


    def _str_(self):
        return self.usage_and_payment_history

    class Meta:
        db_table = 'usage_and_payment_history'



class months(models.Model):
    commulative_bill = models.FloatField(max_length = 45)
    reading = models.FloatField(max_length = 45)
    usage = models.FloatField(max_length = 45)
    bill = models.FloatField(max_length = 45)
    penalty = models.FloatField(max_length = 45)
    total_bill = models.FloatField(max_length = 45)

    def _str_(self):
        return self.months

    class Meta:
        db_table = 'months'
