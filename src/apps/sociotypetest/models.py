from django.db import models

class Socionic_type(models.Model):
    symbol = models.CharField(max_length=3, default = '')
    symbol_dif = models.CharField(max_length=4, default = '')
    name = models.CharField(max_length = 50, default = '')
    name_dif = models.CharField(max_length=50, default = '')
    quadra = models.CharField(max_length=15, default = '')
    img_soc = models.ImageField(upload_to = 'sociotypetest/static/img_soc')
    img_description = models.CharField(max_length=200, default = 'none')
    description_short = models.TextField(max_length=5000, default = 'none')
    description = models.TextField(max_length = 10000, default = 'none')
    dichotomies = models.TextField(max_length = 10000, default = 'none')

    def __str__(self):
        return self.symbol + " - " + self.name_dif + " - " + self.name