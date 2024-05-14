from django.db import models


# Represents a university
class University(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name + " (" + str(self.id) + ")"

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name
        }


# Represents a building within a university. Its ID as CharField is more descriptive
class Building(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=80)
    university = models.ForeignKey(University, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "university": self.university.id
        }


# Represents a site type to better understand it in logic
class SiteType(models.Model):
    type = models.CharField(primary_key=True, max_length=20)

    def __str__(self):
        return self.type

    def to_json(self):
        return {
            "type": self.type
        }


# Represents a site (classroom, hall, lab, elevator) in a building
class Site(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    name = models.CharField(max_length=80)
    img = models.ImageField(upload_to='media/sites')
    type = models.ForeignKey(SiteType, on_delete=models.CASCADE)
    neighbours = models.ManyToManyField(
        'self',
        through='SiteAdjacency',
        symmetrical=True
    )
    building = models.ForeignKey(Building, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name + " (" + self.id + ")"

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "img": self.img.url,
            "type": self.type.type,
            "building": self.building.id
        }


# Represents which sites are adjacent and to what distance in metres
class SiteAdjacency(models.Model):
    a_site = models.ForeignKey(Site, related_name='a_site', on_delete=models.CASCADE, null=True)
    b_site = models.ForeignKey(Site, related_name='b_site', on_delete=models.CASCADE, null=True)
    distanceInM = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.a_site} --- {self.b_site}, distance: {self.distanceInM}m"

    def to_json(self):
        return {
            "a_site": self.a_site.id,
            "b_site": self.b_site.id,
            "distanceInM": self.distanceInM
        }
