from django.db import models

# Create your models here.
class Freezer(models.Model):
    title = models.CharField(max_length=100)
    # Другие поля морозилки

    def __str__(self):
        return self.title


class Shelf(models.Model):
    title = models.CharField(max_length=100)
    freezer = models.ForeignKey(Freezer, on_delete=models.CASCADE)
    # Другие поля полки

    def __str__(self):
        return self.title


class Box(models.Model):
    title = models.CharField(max_length=100)
    shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE)
    # Другие поля коробки

    def __str__(self):
        return self.title
    

class SampleLocation(models.Model):
    title = models.CharField(max_length=100)
    count_samples = models.IntegerField(default=0)
    count_rows = models.IntegerField(default=0)
    count_col = models.IntegerField(default=0)
    state_location = models.CharField(max_length=10, default='free')
    sample_id = models.IntegerField(default=-1)
    box = models.ForeignKey(Box, on_delete=models.CASCADE)
    # Другие поля места

    def __str__(self):
        return self.title