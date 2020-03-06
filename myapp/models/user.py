from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=60, blank=False, null=False)
    password = models.CharField(max_length=50, blank=False, null=False)
    cell_phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=False, null=False)
    word_attemp = models.IntegerField(default=7)
    active = models.BooleanField(default=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    update_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.user_name

    class Meta:
        ordering = ['created_at']
