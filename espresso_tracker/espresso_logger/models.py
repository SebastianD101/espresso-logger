from django.db import models

class CoffeeLog(models.Model):
    ROAST_LEVEL_CHOICES = [
        ('LIGHT', 'Light'),
        ('LIGHT_MEDIUM', 'Light-Medium'),
        ('MEDIUM', 'Medium'),
        ('MEDIUM_DARK', 'Medium-Dark'),
        ('DARK', 'Dark'),
    ]

    bean_name = models.CharField(max_length=100, blank=True, null=True)
    roast_level = models.CharField(max_length=20, choices=ROAST_LEVEL_CHOICES, blank=True, null=True)
    dose = models.FloatField(help_text="Dose in grams", blank=True, null=True)
    yield_amt = models.FloatField(help_text="Yield in grams", blank=True, null=True)
    extraction_time = models.FloatField(help_text="Time in seconds", blank=True, null=True)
    water_temperature = models.FloatField(help_text="Temperature in Celsius", blank=True, null=True)
    sourness_bitterness = models.IntegerField(choices=[(i, i) for i in range(1, 6)], help_text="1 = Bitter, 5 = Sour", blank=True, null=True)
    strength = models.IntegerField(choices=[(i, i) for i in range(1, 6)], help_text="1 = Weak, 5 = Strong", blank=True, null=True)

    def __str__(self):
        return f"{self.bean_name or 'Unknown'} | {self.dose or 'Unknown'}g | {self.extraction_time or 'Unknown'}s"
