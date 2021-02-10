from django.db import models


class Sector(models.Model):
    sector = models.CharField(max_length=250,
                              null=False, blank=False, default='')

    def __str__(self):
        return f"Sector: {self.sector}"


class Cia(models.Model):
    cia = models.CharField(max_length=50,
                           null=True, blank=False, default='')

    def __str__(self):
        return f"Company: {self.cia}"


class Type_goal(models.Model):
    type_goal = models.CharField(max_length=30,
                                 null=False, blank=False, default='')

    def __str__(self):
        return f"Type goal: {self.type_goal}"


class Goal(models.Model):
    title = models.CharField(max_length=150, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    initial_date = models.DateTimeField()
    end_date = models.DateTimeField()
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    cia = models.ForeignKey(Cia, on_delete=models.CASCADE)
    type_goal = models.ForeignKey(Type_goal, on_delete=models.CASCADE)

    def __str__(self):
        return f"Goal: {self.title} | End date: {self.end_date}"
