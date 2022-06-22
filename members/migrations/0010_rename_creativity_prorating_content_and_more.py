

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0009_prorating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prorating',
            old_name='creativity',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='prorating',
            name='developer',
        ),
    ]
