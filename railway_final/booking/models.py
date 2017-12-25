from django.db import models


class Train(models.Model):
    ''' Train Information '''
    number = models.IntegerField(unique=True)
    name = models.CharField(max_length=300)
    date = models.DateField()
    departure = models.TimeField(blank=True, null=True)
    arrival = models.TimeField(blank=True, null=True)
    route = models.ForeignKey('Route')
    third_ac = models.PositiveIntegerField(default=10)
    second_ac = models.PositiveIntegerField(default=10)
    sleeper = models.PositiveIntegerField(default=10)
    fare = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def decrease_third_ac(self):
        self.third_ac -= 1
        self.save()

    def decrease_second_ac(self):
        self.second_ac -= 1
        self.save()

    def decrease_sleeper(self):
        self.second_ac -= 1
        self.save()


class Station(models.Model):
    ''' Station '''
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Route(models.Model):
    ''' Route '''
    name = models.CharField(max_length=20)
    source = models.ForeignKey('Station', related_name='source')
    destination = models.ForeignKey('Station', related_name='destination')
    route_path = models.ManyToManyField("Station", through="RoutePath")

    def __str__(self):
        return self.name


class RoutePath(models.Model):
    route = models.ForeignKey('Route')
    station = models.ForeignKey('Station')
    order = models.IntegerField()

    def __str__(self):
        return "%s-%s-%d" % (self.route.name, self.station.name, self.order)


class Ticket(models.Model):
    ''' Ticket '''
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    train = models.ForeignKey('Train')


    def __str__(self):
        return self.first_name + self.last_name

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name
