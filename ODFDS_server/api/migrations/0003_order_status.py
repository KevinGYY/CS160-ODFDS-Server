# Generated by Django 2.1.7 on 2019-03-25 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190325_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('S1', 'Looking drivers'), ('S2', 'Waiting pick up'), ('S3', 'Sending an order'), ('S4', 'delivered')], default='S1', max_length=2),
        ),
    ]