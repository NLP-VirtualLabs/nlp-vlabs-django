from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# adds custom fields in User_Profiles table
# which is linked to the default User table
class User_Profile(models.Model):
	user = models.OneToOneField(User)
	institute = models.CharField(max_length=200)
	course = models.CharField(max_length=200)


# table for all the experiments
class Experiments(models.Model):
	name = models.CharField(max_length=200)
	lab_category = models.CharField(max_length=200)
	lang = models.CharField(max_length=200)
	visit_count = models.IntegerField(default=0)
	completed_count = models.IntegerField(default=0)
	creation_date = models.DateTimeField('creation date')
	last_mod_date = models.DateTimeField('last modified date')
	prescribed_time = models.IntegerField(default=0)
	max_score = models.IntegerField(default=0)

	def __str__(self):
		return '%s, %s, %s, %s' %(self.name, self.lab_category, self.lang, self.prescribed_time)


# table for the stages in a particular experiment
class Experiment_Stage(models.Model):
	name = models.CharField(max_length=200)
	experiment = models.ForeignKey(Experiments)
	visit_count = models.IntegerField(default=0)
	completed_count = models.IntegerField(default=0)
	prescribed_time = models.IntegerField(default=0)
	max_score = models.IntegerField(default=0)

	def __str__(self):
		return '%s, %s, %s' %(self.name, self.experiment, self.prescribed_time)


# table containing details of the user and his experiments
class User_Experiments(models.Model):
	MODE = (('free style','test mode'),)

	user = models.ForeignKey(User)
	experiment = models.ForeignKey(Experiments)
	time = models.IntegerField(default=0)
	max_stage = models.ForeignKey(Experiment_Stage)
	score = models.IntegerField(default=0)
	mode =  models.CharField(max_length=10, choices=MODE)

	def __str__(self):
		return '%s, %s, %s' %(self.user, self.experiment, self.mode)


# table containing details of the user and his experiment stage
class User_Experiment_Stage(models.Model):
	user = models.ForeignKey(User)
	experiment_stage = models.ForeignKey(Experiment_Stage)
	experiment = models.ForeignKey(User_Experiments)
	time = models.IntegerField(default=0)
	score = models.IntegerField(default=0)
	attempt = models.IntegerField(default=0)

	def __str__(self):
		return '%s, %s, %s' %(self.user, self.experiment_stage, self.experiment)

