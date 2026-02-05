from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, User, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Verwijder bestaande data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superhelden team')
        dc = Team.objects.create(name='DC', description='DC superhelden team')

        # Users
        users = [
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc),
        ]

        # Workouts
        w1 = Workout.objects.create(name='Hero HIIT', description='Intensieve HIIT voor helden')
        w2 = Workout.objects.create(name='Power Strength', description='Krachttraining voor superhelden')
        w1.suggested_for.set([marvel, dc])
        w2.suggested_for.set([marvel, dc])

        # Activities
        Activity.objects.create(user=users[0], type='Rennen', duration=30, date=timezone.now().date())
        Activity.objects.create(user=users[1], type='Fietsen', duration=45, date=timezone.now().date())
        Activity.objects.create(user=users[2], type='Zwemmen', duration=25, date=timezone.now().date())
        Activity.objects.create(user=users[3], type='Krachttraining', duration=60, date=timezone.now().date())

        # Leaderboard
        Leaderboard.objects.create(user=users[0], score=100)
        Leaderboard.objects.create(user=users[1], score=80)
        Leaderboard.objects.create(user=users[2], score=120)
        Leaderboard.objects.create(user=users[3], score=90)

        self.stdout.write(self.style.SUCCESS('octofit_db succesvol gevuld met testdata!'))
