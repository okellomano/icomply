# Generated by Django 3.2 on 2022-07-17 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0006_userchecklist_is_checked'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='policiesdocuments',
            options={'verbose_name_plural': 'Policies Documents'},
        ),
        migrations.AlterModelOptions(
            name='userchecklist',
            options={'verbose_name_plural': 'User Checklists'},
        ),
        migrations.RemoveField(
            model_name='userchecklist',
            name='is_checked',
        ),
    ]
