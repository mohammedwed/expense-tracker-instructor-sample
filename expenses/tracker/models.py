from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id) +" "+ self.title

class Book(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    publish_date = models.DateTimeField()
    distribution_expense = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title +" by " +self.author

class Report(models.Model):
    pass






