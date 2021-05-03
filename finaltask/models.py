from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=50)
    homeworld = models.ForeignKey('Planet', on_delete=models.CASCADE, null=True, blank=True)
    gender = models.CharField(max_length=30, null=True)


    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Characters'

    def __str__(self):
        return self.name

class Planet(models.Model):
    name = models.CharField(max_length=50)
    gravity = models.CharField(max_length=50, null=True, blank=True)
    climate = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Planets'

    def __str__(self):
        return self.name
