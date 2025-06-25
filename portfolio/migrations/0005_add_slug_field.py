from django.db import migrations, models
import django.utils.text
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, null=True),  # First add nullable field
        ),
    ]