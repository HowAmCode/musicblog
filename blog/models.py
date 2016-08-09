from django.db import models
from django.utils import timezone

AGES = (
    ('16+', '16+'),
	('18+', '18+'),
	('19+', '19+'),
	('21+', '21+'),
    ('All Ages', 'All Ages'),
)

GENRE = (
    ('Pop', 'Pop'),
    ('Rock', 'Rock'),
	('Metal', 'Metal'),
	('Electronic', 'Electronic'),
	('Indie', 'Indie'),
	('Country', 'Country'),
	('Jazz', 'Jazz'),
	('Rap/Hip Hop', 'Rap/Hip Hop'),
	('R&B', 'R&B'),
)

FEATURE_CHOICE = (
	(0, 'No'),
	(1,'Yes'),
)

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    contestlink = models.CharField(max_length=500, default='')
    host = models.CharField(max_length=200, default='')
    artist = models.CharField(max_length=200, default='')
    songs = models.CharField(max_length=200, default='None')
    featured = models.IntegerField(choices=FEATURE_CHOICE, default=0)
    genre = models.CharField(max_length=100,choices=GENRE, default='Rock')
    venue = models.CharField(max_length=200)
    city = models.CharField(max_length=200, default='')
    ages = models.CharField(max_length=200, choices=AGES, default="All Ages")
    entrymethod = models.CharField(max_length=200, default='')
    concertday = models.DateField(default=timezone.now)
    expires = models.DateTimeField(blank=True, null=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title