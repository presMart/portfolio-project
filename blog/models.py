from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

# Create blog model
# title
# pub_date
# body (the text for a post)
# image


# Add the blog app to settings

# Create a migration

# Migrate

# Add to the admin
