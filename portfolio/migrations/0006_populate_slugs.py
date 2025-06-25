from django.db import migrations
from django.utils.text import slugify


def create_unique_slugs(apps, schema_editor):
    Category = apps.get_model('portfolio', 'Category')
    for category in Category.objects.all():
        if not category.slug:
            base_slug = slugify(category.name)
            unique_slug = base_slug
            counter = 1
            while Category.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{counter}"
                counter += 1
            category.slug = unique_slug
            category.save()


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_add_slug_field'),
    ]

    operations = [
        migrations.RunPython(create_unique_slugs),
    ]