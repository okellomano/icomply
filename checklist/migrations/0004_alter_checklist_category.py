# Generated by Django 3.2 on 2022-07-15 03:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0003_auto_20220714_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklist',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='checklist.category'),
        ),
    ]
