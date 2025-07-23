from django.db import models
import uuid
# Create your models here.

class Userlist(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=25)
    email = models.EmailField()
    age = models.IntegerField()
    
    def __str__(self):
        return self.name