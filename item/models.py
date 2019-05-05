from django.db import models
from django.utils import timezone

# Create your models here.


class Item(models.Model):
        owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
        itemName = models.CharField(max_length=2000)
        description = models.TextField()
        price = models.IntegerField(default=0)
        created_date = models.DateTimeField(default=timezone.now)


        def item(self):
                self.created_date = timezone.now()
                self.save()

        class Meta():
                db_table = "Item"

        def __str__(self):
                return self.itemName
