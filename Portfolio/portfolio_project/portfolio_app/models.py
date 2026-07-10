from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    subject = models.CharField(max_length = 150)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
    
class Projects(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    image = models.CharField(max_length=100)   # Store filename/path
    link = models.URLField(blank=True, null=True)
    technologies = models.CharField(max_length = 200)

    def __str__(self):
        return self.title
    
class Skills(models.Model):
    name = models.CharField(max_length = 100)
    level = models.IntegerField()

    def __str__(self):
        return self.name