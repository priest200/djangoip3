
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0007_alter_project_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='media/default.png', upload_to='media'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_pic',
            field=models.ImageField(default='media/default.png', upload_to='media'),
        ),
    ]
