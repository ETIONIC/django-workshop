from django.db import models


class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

class Musicband(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Musician)

    def __str__(self):
        return self.name

class Album(models.Model):
    musicband = models.ForeignKey(Musicband, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()



"""


class Membership(models.Model):
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    group = models.ForeignKey(Musicband, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)





















ringo = Musician.objects.create(name="Ringo Starr")
paul = Musician.objects.create(name="Paul McCartney")
beatles = Musicband.objects.create(name="The Beatles")

m1 = Membership(
    person=ringo,
    group=beatles,
    date_joined=date(1962, 8, 16),
    invite_reason="Needed a new drummer."
)
m1.save()
beatles.members.all()

ringo.group_set.all()

m2 = Membership.objects.create(
    musician=paul,
    group=beatles,
    date_joined=date(1960, 8, 1),
    invite_reason="Wanted to form a band."
)
beatles.members.all()

######################################
# Beatles have broken up
beatles.members.clear()
Membership.objects.all()

######################################
# Find all the groups with a member whose name starts with 'Paul'
MusicBand.objects.filter(members__name__startswith='Paul')

######################################

Musician.objects.filter(
    musicband__name='The Beatles',
    membership__date_joined__gt=date(1961,1,1)
)

######################################

ringos_membership = Membership.objects.get(group=beatles, person=ringo)
ringos_membership.date_joined
ringos_membership.invite_reason

ringos_membership = ringo.membership_set.get(group=beatles)
ringos_membership.date_joined
ringos_membership.invite_reason

"""
