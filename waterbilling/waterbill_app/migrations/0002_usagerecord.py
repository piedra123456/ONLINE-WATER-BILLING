# Generated by Django 3.2 on 2021-11-05 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('waterbill_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='usagerecord',
            fields=[
                ('accountid', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('rateid', models.CharField(default=' ', max_length=45)),
                ('prevyeardue', models.FloatField(default=0)),
                ('excesspayment', models.FloatField(default=0)),
                ('commulative_bill', models.FloatField(default=0)),
                ('year', models.BigIntegerField(default=2021)),
                ('accountinfoid', models.CharField(default='', max_length=50)),
                ('amountpaid_history', models.TextField(default='')),
                ('datepaid_history', models.TextField(default='')),
                ('postedby_history', models.TextField(default='')),
                ('or_number_history', models.TextField(default='')),
                ('previous_reading', models.FloatField(default=0)),
                ('reading_jan', models.FloatField(default=0)),
                ('reading_date_jan', models.CharField(default=' ', max_length=45)),
                ('reading_postedby_jan', models.CharField(default=' ', max_length=45)),
                ('usage_jan', models.FloatField(default=0)),
                ('penalty_jan', models.FloatField(default=0)),
                ('bill_jan', models.FloatField(default=0)),
                ('totalbill_jan', models.FloatField(default=0)),
                ('paidamt_jan', models.FloatField(default=0)),
                ('datepaid_jan', models.TextField(default=' ')),
                ('dateposted_jan', models.CharField(default=' ', max_length=45)),
                ('postedby_jan', models.TextField(default=' ')),
                ('txrefnum_jan', models.CharField(default=' ', max_length=45)),
                ('ior_jan', models.CharField(default=' ', max_length=50)),
                ('amountpaid_str_jan', models.TextField(default='')),
                ('reading_feb', models.FloatField(default=0)),
                ('reading_date_feb', models.CharField(max_length=45)),
                ('reading_postedby_feb', models.CharField(max_length=45)),
                ('usage_feb', models.FloatField(default=0)),
                ('penalty_feb', models.FloatField(default=0)),
                ('bill_feb', models.FloatField(default=0)),
                ('totalbill_feb', models.FloatField(default=0)),
                ('paidamt_feb', models.FloatField(default=0)),
                ('datepaid_feb', models.TextField(default=' ')),
                ('dateposted_feb', models.CharField(default=' ', max_length=45)),
                ('postedby_feb', models.TextField(default=' ')),
                ('txrefnum_feb', models.CharField(default=' ', max_length=45)),
                ('ior_feb', models.CharField(default=' ', max_length=50)),
                ('amountpaid_str_feb', models.TextField(default='')),
                ('reading_mar', models.FloatField(default=0)),
                ('reading_date_mar', models.CharField(max_length=45)),
                ('reading_postedby_mar', models.CharField(max_length=45)),
                ('usage_mar', models.FloatField(default=0)),
                ('penalty_mar', models.FloatField(default=0)),
                ('bill_mar', models.FloatField(default=0)),
                ('totalbill_mar', models.FloatField(default=0)),
                ('paidamt_mar', models.FloatField(default=0)),
                ('datepaid_mar', models.TextField(default=' ')),
                ('dateposted_mar', models.TextField(default=' ')),
                ('postedby_mar', models.TextField(default=' ')),
                ('txrefnum_mar', models.CharField(default=' ', max_length=45)),
                ('ior_mar', models.CharField(default=' ', max_length=50)),
                ('amountpaid_str_mar', models.TextField(default='')),
                ('reading_apr', models.FloatField(default=0)),
                ('reading_date_apr', models.CharField(max_length=45)),
                ('reading_postedby_apr', models.CharField(max_length=45)),
                ('usage_apr', models.FloatField(default=0)),
                ('penalty_apr', models.FloatField(default=0)),
                ('bill_apr', models.FloatField(default=0)),
                ('totalbill_apr', models.FloatField(default=0)),
                ('paidamt_apr', models.FloatField(default=0)),
                ('datepaid_apr', models.TextField(default=' ')),
                ('dateposted_apr', models.CharField(default=' ', max_length=45)),
                ('postedby_apr', models.TextField(default=' ')),
                ('txrefnum_apr', models.CharField(default=' ', max_length=45)),
                ('ior_apr', models.CharField(default=' ', max_length=50)),
                ('amountpaid_str_apr', models.TextField(default='')),
                ('reading_may', models.FloatField(default=0)),
                ('reading_date_may', models.CharField(max_length=45)),
                ('reading_postedby_may', models.CharField(max_length=45)),
                ('usage_may', models.FloatField(default=0)),
                ('penalty_may', models.FloatField(default=0)),
                ('bill_may', models.FloatField(default=0)),
                ('totalbill_may', models.FloatField(default=0)),
                ('paidamt_may', models.FloatField(default=0)),
                ('datepaid_may', models.TextField(default=' ')),
                ('dateposted_may', models.CharField(default=' ', max_length=45)),
                ('postedby_may', models.TextField(default=' ')),
                ('txrefnum_may', models.CharField(default=' ', max_length=45)),
                ('ior_may', models.CharField(default=' ', max_length=50)),
                ('amountpaid_str_may', models.TextField(default='')),
                ('reading_jun', models.FloatField(default=0)),
                ('reading_date_jun', models.CharField(max_length=45)),
                ('reading_postedby_jun', models.CharField(max_length=45)),
                ('usage_jun', models.FloatField(default=0)),
                ('penalty_jun', models.FloatField(default=0)),
                ('bill_jun', models.FloatField(default=0)),
                ('totalbill_jun', models.FloatField(default=0)),
                ('paidamt_jun', models.FloatField(default=0)),
                ('datepaid_jun', models.TextField(default=' ')),
                ('dateposted_jun', models.CharField(default=' ', max_length=45)),
                ('postedby_jun', models.TextField(default=' ')),
                ('txrefnum_jun', models.CharField(default=' ', max_length=45)),
                ('ior_jun', models.CharField(default=' ', max_length=50)),
                ('amountpaid_str_jun', models.TextField(default='')),
                ('reading_jul', models.FloatField(default=0)),
                ('reading_date_jul', models.CharField(max_length=45)),
                ('reading_postedby_jul', models.CharField(max_length=45)),
                ('usage_jul', models.FloatField(default=0)),
                ('penalty_jul', models.FloatField(default=0)),
                ('bill_jul', models.FloatField(default=0)),
                ('totalbill_jul', models.FloatField(default=0)),
                ('paidamt_jul', models.FloatField(default=0)),
                ('datepaid_jul', models.TextField(default=' ')),
                ('dateposted_jul', models.CharField(default=' ', max_length=45)),
                ('postedby_jul', models.TextField(default=' ')),
                ('txrefnum_jul', models.CharField(default=' ', max_length=45)),
                ('ior_jul', models.CharField(default=' ', max_length=50)),
                ('amountpaid_str_jul', models.TextField(default='')),
                ('reading_aug', models.FloatField(default=0)),
                ('reading_date_aug', models.CharField(max_length=45)),
                ('reading_postedby_aug', models.CharField(max_length=45)),
                ('usage_aug', models.FloatField(default=0)),
                ('penalty_aug', models.FloatField(default=0)),
                ('bill_aug', models.FloatField(default=0)),
                ('totalbill_aug', models.FloatField(default=0)),
                ('paidamt_aug', models.FloatField(default=0)),
                ('datepaid_aug', models.TextField(default=' ')),
                ('dateposted_aug', models.CharField(default=' ', max_length=45)),
                ('postedby_aug', models.TextField(default=' ')),
                ('txrefnum_aug', models.CharField(default=' ', max_length=45)),
                ('ior_aug', models.CharField(default=' ', max_length=50)),
                ('amountpaid_str_aug', models.TextField(default='')),
                ('reading_sept', models.FloatField(default=0)),
                ('reading_date_sept', models.CharField(max_length=45)),
                ('reading_postedby_sept', models.CharField(max_length=45)),
                ('usage_sept', models.FloatField(default=0)),
                ('penalty_sept', models.FloatField(default=0)),
                ('bill_sept', models.FloatField(default=0)),
                ('totalbill_sept', models.FloatField(default=0)),
                ('paidamt_sept', models.FloatField(default=0)),
                ('datepaid_sept', models.TextField(default=' ')),
                ('dateposted_sept', models.CharField(default=' ', max_length=45)),
                ('postedby_sept', models.TextField(default=' ')),
                ('txrefnum_sept', models.CharField(default=' ', max_length=45)),
                ('ior_sept', models.CharField(default=' ', max_length=50)),
                ('amountpaid_str_sept', models.TextField(default='')),
                ('reading_oct', models.FloatField(default=0)),
                ('reading_date_oct', models.CharField(max_length=45)),
                ('reading_postedby_oct', models.CharField(max_length=45)),
                ('usage_oct', models.FloatField(default=0)),
                ('penalty_oct', models.FloatField(default=0)),
                ('bill_oct', models.FloatField(default=0)),
                ('totalbill_oct', models.FloatField(default=0)),
                ('paidamt_oct', models.FloatField(default=0)),
                ('datepaid_oct', models.TextField(default=' ')),
                ('dateposted_oct', models.CharField(default=' ', max_length=45)),
                ('postedby_oct', models.TextField(default=' ')),
                ('txrefnum_oct', models.TextField(default=' ')),
                ('ior_oct', models.CharField(default=' ', max_length=50)),
                ('amountpaid_str_oct', models.TextField(default='')),
                ('reading_nov', models.FloatField(default=0)),
                ('reading_date_nov', models.CharField(max_length=45)),
                ('reading_postedby_nov', models.CharField(max_length=45)),
                ('usage_nov', models.FloatField(default=0)),
                ('penalty_nov', models.FloatField(default=0)),
                ('bill_nov', models.FloatField(default=0)),
                ('totalbill_nov', models.FloatField(default=0)),
                ('paidamt_nov', models.FloatField(default=0)),
                ('datepaid_nov', models.TextField(default=' ')),
                ('dateposted_nov', models.CharField(default=' ', max_length=45)),
                ('postedby_nov', models.TextField(default=' ')),
                ('txrefnum_nov', models.CharField(default=' ', max_length=45)),
                ('ior_nov', models.CharField(default=' ', max_length=50)),
                ('amountpaid_str_nov', models.TextField(default='')),
                ('reading_dec', models.FloatField(default=0)),
                ('reading_date_dec', models.CharField(max_length=45)),
                ('reading_postedby_dec', models.CharField(max_length=45)),
                ('usage_dec', models.FloatField(default=0)),
                ('penalty_dec', models.FloatField(default=0)),
                ('bill_dec', models.FloatField(default=0)),
                ('totalbill_dec', models.FloatField(default=0)),
                ('paidamt_dec', models.FloatField(default=0)),
                ('datepaid_dec', models.TextField(default=' ')),
                ('dateposted_dec', models.CharField(default=' ', max_length=45)),
                ('postedby_dec', models.TextField(default=' ')),
                ('txrefnum_dec', models.CharField(default=' ', max_length=45)),
                ('ior_dec', models.CharField(default=' ', max_length=50)),
                ('amountpaid_str_dec', models.TextField(default='')),
                ('consumerid', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='waterbill_app.consumerlist')),
            ],
            options={
                'db_table': 'accountrecord',
            },
        ),
    ]