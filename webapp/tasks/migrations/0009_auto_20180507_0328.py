

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0008_auto_20180507_0326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('adanger', 'Priority High'), ('bwarning', 'Priority Medium'), ('csuccess', 'Priority Low')], default='adanger', max_length=30),
        ),
    ]
