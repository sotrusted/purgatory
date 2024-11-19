from django.db import models

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='team/')
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name

class Merchandise(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='merchandise/')
    stripe_checkout_url = models.URLField()  # For Stripe integration

    def __str__(self):
        return self.title
