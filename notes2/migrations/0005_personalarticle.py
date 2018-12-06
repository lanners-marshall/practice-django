# Generated by Django 2.1.4 on 2018-12-04 22:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notes2', '0004_personalnote'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalArticle',
            fields=[
                ('articles_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='notes2.Articles')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('notes2.articles',),
        ),
    ]