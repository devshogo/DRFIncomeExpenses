# Generated by Django 4.0.2 on 2022-03-03 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0002_rename_expenses_expense'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expense',
            options={'ordering': ['-date']},
        ),
    ]
