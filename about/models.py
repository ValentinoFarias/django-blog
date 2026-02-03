from django.db import models


class About(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_on"]

    def __str__(self) -> str:
        return self.title


class Collaborate(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self) -> str:
        return f"{self.name} ({self.email})"
