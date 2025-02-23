# Generated by Django 2.2.6 on 2020-01-25 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Joke',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('custom_ordering', models.IntegerField(default=0)),
                ('about', models.CharField(help_text='What the joke is about : ex : Two Jews, Blacks, White', max_length=120)),
                ('build_up', models.CharField(help_text='Build up or first line of the joke', max_length=1300, null=True)),
                ('delivery', models.CharField(blank=True, help_text='2nd Part of joke : if joke is only one liner then leave this one empty', max_length=120, null=True)),
                ('type', models.CharField(blank=True, help_text='Type of joke : category', max_length=120, null=True)),
                ('thumb_slug', models.CharField(blank=True, help_text='Thumbnail Url - if any', max_length=120, null=True)),
                ('full_slug', models.CharField(blank=True, help_text='Full Resolution Url of Thumb - If Any', max_length=120, null=True)),
                ('gif_slug', models.CharField(blank=True, help_text='Gif Url - If Any', max_length=120, null=True)),
                ('nsfw', models.BooleanField(default=False, help_text='True : when joke not safe for work (for example sexually explicit jokes)')),
                ('religious', models.BooleanField(default=False, help_text='True : when joke against certain religions and their prejudices')),
                ('political', models.BooleanField(default=False, help_text='True : when joke against politics / politicians ')),
                ('thumbs_ups', models.IntegerField(default=0)),
                ('thumbs_downs', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
