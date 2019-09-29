from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


def upload_image_to(instance, filename):
    return 'cycle/cycle_{0}/{1}'.format(instance.owner, filename)


class Cycle(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    image = models.ImageField(upload_to=upload_image_to)
    rent = models.IntegerField(default=0)
    is_picked = models.BooleanField(default=False)
    rating = models.DecimalField(default=1, max_digits=3, decimal_places=2, validators=[
                                MinValueValidator(1), MaxValueValidator(5)])
    picked_times = models.IntegerField(default=0)
    pick_id = models.IntegerField(default=0)


class Pickcycle(models.Model):
    cycle_id = models.ForeignKey(Cycle, on_delete=models.CASCADE)
    picked_by = models.ForeignKey(User, on_delete=models.CASCADE)
    pick_date = models.DateTimeField(default=timezone.now)


class Dropcycle(models.Model):
    pick_id = models.ForeignKey(Pickcycle, null=True, on_delete=models.CASCADE)
    drop_date = models.DateTimeField(default=timezone.now)


class Location(models.Model):
    area = models.CharField(max_length=30)
    near_by = models.CharField(
        max_length=30, blank=True, verbose_name="2nd area")
    near_by_t = models.CharField(
        max_length=30, blank=True, verbose_name="3rd area")
    gps_lat = models.CharField(
        max_length=30, blank=True, verbose_name="Latitude")
    gps_lon = models.CharField(
        max_length=30, blank=True, verbose_name="Longitude")
    cycle_id = models.OneToOneField(Cycle, on_delete=models.CASCADE)
