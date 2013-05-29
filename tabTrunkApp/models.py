from django.db import models

class Tab(models.Model):
	NADA = 'N'
	SOME = 'S'
	PLAY = 'P'
	ALL = 'A'
	abilityChoices = (
	(NADA, "Nada"),
	(SOME, "Some"),
	(PLAY, "Play"),
	(ALL, "Hero"),
	)
	ability = models.CharField(max_length=3,
								choices=abilityChoices,
								default=NADA)
	songTitle = models.CharField(max_length=300)
	artist = models.CharField(max_length=300)
	tabURL = models.CharField(max_length=300, blank=True)
	addedDate = models.DateTimeField('date added')
	content = models.TextField(blank=True)
	username = models.TextField(max_length=30)
	
	def __unicode__(self):
		return self.artist + ' - ' + self.songTitle
		
	def was_added_recently(self):
		return self.addedDate >= timezone.now() - datetime.timedelta(days=7)