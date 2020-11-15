from django.db import models

# Create your models here.

# Ederick: This is where I created the tables for
# the PostgreSQL Database, classes acting as attributes
# Also a handy return string function to obtain of current instance information 

class Users(models.Model):
	uid = models.AutoField(primary_key=True)
	def __str__(self):
		return self.uid

	name = models.CharField(max_length=40)
	def __str__(self):
		return self.name

	govid = models.IntegerField(default=0)
	def __str__(self):
		return self.govid

	ssn = models.CharField(max_length=11)
	def __str__(self):
		return self.ssn

	password = models.CharField(max_length=255)
	def __str__(self):
		return self.password

	is_it = models.BooleanField()
	def __str__(self):
		return str(self.is_it)

class Votee(models.Model):
	uid = models.ForeignKey(Users, on_delete=models.CASCADE)
	def __str__(self):
		return str(self.uid)

class Voter(models.Model):
	uid = models.ForeignKey(Users, on_delete=models.CASCADE)
	def __str__(self):
		return self.uid

	vote_history = models.CharField(max_length=255)
	def __str__(self):
		return self.vote_history