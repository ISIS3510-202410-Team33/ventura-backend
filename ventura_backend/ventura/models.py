from django.db import models

# Create your models here.

class College(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name + " (" + str(self.id) + ")"

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    #id_college = models.ForeignKey(College, on_delete=models.CASCADE)
    
class College_location(models.Model):
    id = models.AutoField(primary_key=True)
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    floors = models.IntegerField()
    restaurants = models.IntegerField()
    green_zones = models.IntegerField()
    obstructions = models.BooleanField()

class User_calification(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    college_location = models.ForeignKey(College_location, on_delete=models.CASCADE)
    calification = models.IntegerField()
    description = models.TextField(max_length=300)  
    date = models.DateField(auto_now=True)

class User_frequency(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    college_location = models.ForeignKey(College_location, on_delete=models.CASCADE)
    frequency = models.IntegerField()
