from datetime import date

from django.db.models import (
    CharField,
    DateField,
    URLField,
    Model,
    ManyToManyField,
    SlugField,
)

from organizer.models import Tag, Startup
from django.urls import reverse


class Post(Model):

    title = CharField(max_length=63)
    slug = SlugField(max_length=63)
    pub_date = DateField("date published", default=date.today)
    link = URLField()
    tags = ManyToManyField(
        Tag,
        related_name="blog_posts"
    )
    startups = ManyToManyField(
        Startup,
        related_name="blog_posts"
    )

    class Meta:
        get_latest_by = "pub_date"
        ordering = ["-pub_date", "title"]
        verbose_name = "blog post"

    def __str__(self):
        date_string = self.pub_date.strftime("%Y-%m-%d")
        return f"{self.title} on {date_string}"

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={
            "year": self.pub_date.year,
            "month": self.pub_date.month,
            "slug": self.slug
        })
