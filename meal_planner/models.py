from django.db import models

class Meal(models.Model):
    """A meal the user wants to plan."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the meal."""
        return self.text


class Dish(models.Model):
    """Specific dishes that comprise the meal."""
    topic = models.ForeignKey(Meal, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'dishes'

    def __str__(self):
        """Return a simple string representing the dish."""
        return self.name



from django.db import models

# Create your models here.
