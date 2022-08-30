from django.db import models
from accounts.models import User


class Portfolio(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=True, blank=True, default='')
    user_created = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name} - {self.id} - {self.user_created}"


class Photo(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True, default='')
    img = models.ImageField(null=False, blank=False)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-create_at']

    def __str__(self):
        return f"{self.name} - {self.id} - {self.portfolio}"

