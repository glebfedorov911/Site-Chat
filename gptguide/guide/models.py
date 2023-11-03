from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models

import random
import string

from django.utils.text import slugify


def generate_string(length):
    letters = string.ascii_lowercase
    rand_string = "".join(random.choice(letters) for i in range(length))
    return rand_string

class UserCustomModel(AbstractUser):
    ref = models.BooleanField(default=False)
    ref_signUp = models.BooleanField(default=False)
    msg = models.IntegerField(default=5)
    ref_code = models.CharField(max_length=8, blank=True, null=True)
    discount = models.IntegerField(default=0)
    rate = models.ForeignKey("Rate", on_delete=models.CASCADE, default=None, blank=True, null=True, related_name="Тариф")
    date_of_reg_ref = models.DateTimeField(default=datetime.now)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super(UserCustomModel, self).save(*args, **kwargs)

class Rate(models.Model):
    R1 = "Минимальный"
    R2 = "Cредний"
    R3 = "Максимальный"

    RATES = [
        (R1, "Минимальный"),
        (R2, "Cредний"),
        (R3, "Максимальный"),
    ]

    C1 = "100"
    C2 = "200"
    C3 = "300"

    COSTS = [
        (C1, 100),
        (C2, 200),
        (C3, 300),
    ]

    M1 = "10"
    M2 = "20"
    M3 = "30"

    MSG = [
        (M1, 10),
        (M2, 15),
        (M3, 20),
    ]

    name = models.CharField(max_length=50, blank=False, choices=RATES)
    cost = models.CharField(blank=False, choices=COSTS, max_length=50)
    count_message = models.CharField(choices=MSG, blank=True, max_length=50)

class Message(models.Model):
    from_user = models.ForeignKey("UserCustomModel", on_delete=models.CASCADE, default=None, blank=True, null=True, related_name="отправитель")
    to_user = models.ForeignKey("UserCustomModel", on_delete=models.CASCADE, default=None, blank=True, null=True, related_name="получатель")
    key = models.CharField(blank=True, null=True, max_length=100)
    msg = models.TextField(blank=True, null=True)
    audio = models.FileField(blank=True, null=True, upload_to="audio/%Y/%m/%d")
    date_create = models.DateTimeField(default=datetime.now)

class Pay(models.Model):
    user = models.ForeignKey("UserCustomModel", on_delete=models.CASCADE, default=None)
    rate = models.ForeignKey("Rate", on_delete=models.CASCADE, default=None, blank=True, null=True, related_name="Имя_тарифа")
    date_of_pay = models.DateTimeField(default=datetime.now)

class AdminPanelEdit(models.Model):
    avatar = models.ImageField(upload_to="photos/%Y/%m/%d", blank=True, null=True)
    instruction = models.CharField(max_length=256, blank=True, null=True)
    doc = models.FileField(upload_to="files/%Y/%m/%d", blank=True, null=True)
    url = models.CharField(max_length=256, blank=True, null=True)
    token = models.CharField(max_length=256, blank=True, null=True)

class WorkPiece(models.Model):
    text = models.CharField(max_length=256)