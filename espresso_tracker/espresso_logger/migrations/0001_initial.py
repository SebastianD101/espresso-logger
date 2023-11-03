# Generated by Django 4.2.6 on 2023-10-30 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoffeeLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bean_name', models.CharField(blank=True, max_length=100, null=True)),
                ('roast_level', models.CharField(blank=True, choices=[('LIGHT', 'Light'), ('LIGHT_MEDIUM', 'Light-Medium'), ('MEDIUM', 'Medium'), ('MEDIUM_DARK', 'Medium-Dark'), ('DARK', 'Dark')], max_length=20, null=True)),
                ('dose', models.FloatField(blank=True, help_text='Dose in grams', null=True)),
                ('yield_amt', models.FloatField(blank=True, help_text='Yield in grams', null=True)),
                ('extraction_time', models.FloatField(blank=True, help_text='Time in seconds', null=True)),
                ('grind_size', models.CharField(blank=True, max_length=100, null=True)),
                ('water_temperature', models.FloatField(blank=True, help_text='Temperature in Celsius', null=True)),
                ('sourness_bitterness', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], help_text='1 = Bitter, 5 = Sour', null=True)),
                ('strength', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], help_text='1 = Weak, 5 = Strong', null=True)),
                ('tools_used', models.TextField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, help_text='Any additional notes or comments', null=True)),
            ],
        ),
    ]