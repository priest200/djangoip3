

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0011_prorating_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='comments',
        ),
    ]
