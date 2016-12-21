from __future__ import unicode_literals

from django.db import models
import bcrypt

class UserManager(models.Manager):
    def validateRegistration(self, form):
        errors = []

        if len(form['first_name']) == 0:
            errors.append("First Name is required")
        elif len(form['first_name'])<3:
            errors.append("First Name must be longer than 3 characters")
        if len(form['last_name']) == 0:
            errors.append("Last Name is required")
        elif len(form['last_name'])<3:
            errors.append("Last Name must be longer than 3 characters!")
        if len(form['username']) < 3:
            errors.append("Username must be at least 3 characters")
        elif Users.objects.filter(username=form['username']):
            errors.append("Account already exists with that Username")

        if len(form['password']) == 0:
            errors.append("Password is required")
        elif len(form['password'])<8:
            errors.append("Password must be at least 8 characters")
        if form['passconf'] != form['password']:
            errors.append("Passwords Don't Match")

        return errors

    def register(self, form):
        hashed_pass = bcrypt.hashpw(form['password'].encode(), bcrypt.gensalt())
        return self.create(first_name=form['first_name'], last_name=form['last_name'], username=form['username'], password=hashed_pass)


    def check_login(self, form):
        check_user = self.filter(username=form['username'])
        if check_user:
            user = check_user[0]
            if bcrypt.hashpw(form['password'].encode(), user.password.encode()) == user.password:
                return user
        else:
            return None


# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    hiredate = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)
