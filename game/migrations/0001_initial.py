# Generated by Django 3.2 on 2022-08-21 18:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('suit', models.CharField(choices=[('c', '♣'), ('d', '♦'), ('h', '♥'), ('s', '♠')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='CardInDeck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField(default=0)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.card')),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_ready', models.BooleanField(default=False)),
                ('bank', models.IntegerField(default=100)),
                ('bet', models.IntegerField(default=0)),
                ('position', models.IntegerField(default=0)),
                ('action', models.CharField(choices=[('r', 'raise'), ('c', 'check'), ('f', 'fold'), ('s', 'skp'), ('', 'no action')], default='f', max_length=1)),
                ('hand', models.ManyToManyField(blank=True, null=True, related_name='_game_membership_hand_+', to='game.Card')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('blind', models.IntegerField(default=10)),
                ('ante', models.IntegerField(default=0)),
                ('bank', models.IntegerField(default=0)),
                ('next_turn', models.DateTimeField(blank=True, null=True)),
                ('bet', models.IntegerField(default=0)),
                ('timeout', models.IntegerField(default=30)),
                ('status', models.CharField(choices=[('w', 'waiting for players'), ('r', 'ready'), ('c', 'under control'), ('e', 'ended')], default='w', max_length=1)),
                ('deck', models.ManyToManyField(related_name='_game_room_deck_+', through='game.CardInDeck', to='game.Card')),
                ('players', models.ManyToManyField(related_name='_game_room_players_+', through='game.Membership', to=settings.AUTH_USER_MODEL)),
                ('table', models.ManyToManyField(blank=True, null=True, related_name='_game_room_table_+', to='game.Card')),
            ],
        ),
        migrations.AddField(
            model_name='membership',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.room'),
        ),
        migrations.AddField(
            model_name='cardindeck',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.room'),
        ),
    ]
