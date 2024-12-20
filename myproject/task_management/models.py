from django.db import models


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    PRIORITY_CHOICES = [
        ('high', 'High'),
        ('mid', 'Mid'),
        ('low', 'Low'),
    ]
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='mid',
    )
    STATUS_CHOICES = [
        ('pending', 'PENDING'),
        ('in_progress', 'IN PROGRESS'),
        ('completed', 'COMPLETED'),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
    )
    due_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.title