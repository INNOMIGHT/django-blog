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

#ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDntxxE6e9IhgeRiL8ErrAarYUu6nUXsvJHYVf+OMEKIjI7MS87JagsMzOCt202SYiU5OLqC9noNH7f3PDoR8nSzflLuT7bWvYKdGcAbFe2yYJJYfjIMRXrCeTl/5kVlRUVjWRpEmN5N1HZwHe5pylqmPegsu4R2lSOkmwkIjnlBt4jFv64p9CMwAB2ArTrXWNpkTI2LTLRxsa8sBUz34tzm72Wz/6AZ3cmHh6gxQqzoUWb3Tc8i5i94LQP3MoYx2hDOmupSY+f1sE0QH5TB6vpnA1eiBxUaGzFPfYxkUv9I4OWZxeT3Uy53n8dQpVGGVaS7dfz1MmIGSDgwmYmKMsH vaibhav shrivastava@INNOMIGH