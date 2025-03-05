from django.db import models
import uuid

class Permission(models.Model):
    permission_name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.permission_name

class Role(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    permissions = models.ManyToManyField(Permission, related_name='roles')

    def __str__(self):
        return self.title

class User(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Use Django's built-in password hashing
    is_active = models.BooleanField(default=True)
    roles = models.ManyToManyField(Role, related_name='users')

    def __str__(self):
        return self.email