# Generated by Django 3.2.4 on 2022-05-08 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food_billing_system_app', '0004_menu'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='fnamr',
            new_name='fname',
        ),
    ]
