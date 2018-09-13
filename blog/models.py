from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

# To list entries my name in admin panel
    def __str__(self):
        return self.title





# Create blog model
# title
# pub_date
# body (the text for a post)
# image


# Add the blog app to settings

# Create a migration

# Migrate

# Add to the admin
