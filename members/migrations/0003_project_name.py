

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_profile_user_alter_profile_profile_pic_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
