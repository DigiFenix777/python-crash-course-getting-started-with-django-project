from django.db import models

class Pizza(models.Model):
    """A pizza the user wants to order."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text


class Topping(models.Model):
    """Something specific to put on the pizza."""
    topic = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a simple string representing the entry."""
        return self.name



