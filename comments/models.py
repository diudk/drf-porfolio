from django.db import models

from portfolios.models import Photo


class Comment(models.Model):
    user_name = models.CharField(max_length=150, null=True, blank=True)
    message = models.TextField(null=False, blank=False)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, null=False, blank=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-create_at']

    def __str__(self):
        return f"Comment to {self.photo.name}"
