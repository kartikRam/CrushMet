# Generated by Django 4.0.6 on 2023-03-05 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crushmetapp', '0003_demoprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='demoprofile',
            name='username',
            field=models.CharField(default='ABC', max_length=100),
        ),
    ]