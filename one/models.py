from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=15)
    surname = models.CharField(max_length=15)
    portrait = models.ImageField(blank=True, null=True, upload_to="portraits/")
    def __str__(self):
        return f"{self.name} {self.surname}"
    
    
class Book(models.Model):
    title = models.CharField(max_length=250)
    pages = models.IntegerField()
    year = models.IntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    
    author = models.ForeignKey("Author", verbose_name="Автор", on_delete=models.CASCADE)
    preview = models.FileField(blank=True, null=True, upload_to="previews/")
    
    def __str__(self):
        return f"{self.title}"
    


    
    