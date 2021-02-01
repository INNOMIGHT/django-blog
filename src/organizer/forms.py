from django.forms import ModelForm
from .models import Tag, Startup
from django.core.exceptions import ValidationError


class LowerCaseNameMixin:

    def clean_name(self):
        return self.cleaned_data['name'].lower()


class SlugCleanMixin:

    def clean_slug(self):
        slug = self.cleaned_data['slug']
        if slug == 'create':
            raise ValidationError(
                "Tag may not be created."
            )
        return slug


class TagForm(LowerCaseNameMixin, ModelForm):

    class Meta:
        model = Tag
        fields = "__all__"


class StartupForm(SlugCleanMixin, LowerCaseNameMixin, ModelForm):

    class Meta:
        model = Startup
        fields = "__all__"