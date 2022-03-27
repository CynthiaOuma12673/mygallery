from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    @classmethod
    def all_locations(cls):
        locations = Location.objects.all()
        return locations

    @classmethod
    def update_location(cls, id, name):
        cls.objects.filter(id = id).update(ame = name)

    def __str__(self):
        return self.name
