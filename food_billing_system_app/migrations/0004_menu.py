# Generated by Django 3.2.4 on 2022-05-08 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_billing_system_app', '0003_auto_20220508_0051'),
    ]

    operations = [
        migrations.CreateModel(
            name='menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fnamr', models.CharField(max_length=100, null=True)),
                ('ftype', models.CharField(max_length=100, null=True)),
                ('cost', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
