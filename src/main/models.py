from django.db import models

# Create your models here.

# Ederick: This is where I created the tables for
# the PostgreSQL Database, classes acting as attributes
# Also a handy return string function to obtain of current instance information 

class Users(models.Model):						# Users Database Table
	uid = models.AutoField(primary_key=True)	# UID
	def __str__(self):
		return self.uid

	name = models.CharField(max_length=41)		# Name, First And Last Name Concatenated 
	def __str__(self):
		return self.name

	govid = models.IntegerField(default=0)		# State Government ID, will be obtained with RSA Keys
	def __str__(self):
		return self.govid

	ssn = models.CharField(max_length=255)		# Social Security Number, will be obtained with RSA Keys
	def __str__(self):
		return self.ssn

	password = models.CharField(max_length=255)	# Passwords, will be obtained with RSA Keys
	def __str__(self):
		return self.password

	is_it = models.BooleanField()				# Stored Boolean Value to know if it is an IT Adminstrator or Not
	def __str__(self):
		return str(self.is_it)

class Votee(models.Model):									# Votee Database Table
	uid = models.ForeignKey(Users, on_delete=models.CASCADE)	# UID to Stay in Sync
	def __str__(self):
		return str(self.uid)

class Voter(models.Model):									# Voter Database Table
	uid = models.ForeignKey(Users, on_delete=models.CASCADE)	# UID to Stay in Sync
	def __str__(self):
		return self.uid

	vote_history = models.CharField(max_length=255)	# Vote History to obtain and report back ballots from webpage to database
	def __str__(self):
		return self.vote_history