# Generated by Django 4.2.6 on 2023-11-04 03:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('espresso_logger', '0003_alter_coffeelog_roast_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coffeelog',
            name='grind_size',
        ),
        migrations.RemoveField(
            model_name='coffeelog',
            name='notes',
        ),
        migrations.RemoveField(
            model_name='coffeelog',
            name='tools_used',
        ),
    ]
