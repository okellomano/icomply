# Generated by Django 3.2 on 2022-07-19 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0009_checklist_brief_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklist',
            name='checklist_item',
            field=models.CharField(max_length=300),
        ),
    ]
