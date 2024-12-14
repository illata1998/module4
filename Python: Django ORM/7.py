from django.db import models


class Island(models.Model):
    name = models.CharField(max_length=200)

    def can_reach(self, island, *, by_ship):
        "Return True if one can reach the @island using a @by ship"
        # BEGIN
        return by_ship in self.ships.all() and by_ship in island.ships.all()
        # END


class Ship(models.Model):
    name = models.CharField(max_length=200)
    islands = models.ManyToManyField(Island, related_name='ships')
