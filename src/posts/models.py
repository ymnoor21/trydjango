from __future__ import unicode_literals

from django.db import models


def upload_location(instance, filename):
    "images/posts/%s/%s" % (instance.id, filename)
    return "images/posts/%s/%s" % (instance.id, filename)


class Post(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to=upload_location,
        width_field="width_field",
        height_field="height_field",
    )

    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)

    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at", "-updated_at"]
