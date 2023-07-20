

from django.db import models

class Facilities(models.Model):
    id = models.IntegerField(primary_key=True)
    facility = models.CharField(max_length=84)

    def __unicode__(self):
        return self.facility
        
    class Meta:
        app_label = 'logviewer'
        db_table = u'facilities'
        
class Priorites(models.Model):
    num = models.IntegerField(primary_key=True)
    severity = models.CharField(max_length=54)

    def __unicode__(self):
        return self.severity
        
    class Meta:
        db_table = u'priorites'
        
class Systemevents(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID')
    customerid = models.BigIntegerField(null=True, db_column='CustomerID', blank=True)
    receivedat = models.DateTimeField(null=True, db_column='ReceivedAt', blank=True)
    devicereportedtime = models.DateTimeField(null=True, db_column='DeviceReportedTime', blank=True)
    facility = models.OneToOneField(Facilities, db_column='Facility', on_delete=models.CASCADE)
    priority = models.OneToOneField(Priorites, db_column='Priority',  on_delete=models.CASCADE)
    fromhost = models.CharField(max_length=180, db_column='FromHost', blank=True) 
    message = models.TextField(db_column='Message', blank=True) 
    ntseverity = models.IntegerField(null=True, db_column='NTSeverity', blank=True) 
    importance = models.IntegerField(null=True, db_column='Importance', blank=True) 
    eventsource = models.CharField(max_length=180, db_column='EventSource', blank=True) 
    eventuser = models.CharField(max_length=180, db_column='EventUser', blank=True) 
    eventcategory = models.IntegerField(null=True, db_column='EventCategory', blank=True) 
    eventid = models.IntegerField(null=True, db_column='EventID', blank=True) 
    eventbinarydata = models.TextField(db_column='EventBinaryData', blank=True) 
    maxavailable = models.IntegerField(null=True, db_column='MaxAvailable', blank=True) 
    currusage = models.IntegerField(null=True, db_column='CurrUsage', blank=True) 
    minusage = models.IntegerField(null=True, db_column='MinUsage', blank=True) 
    maxusage = models.IntegerField(null=True, db_column='MaxUsage', blank=True) 
    infounitid = models.IntegerField(null=True, db_column='InfoUnitID', blank=True) 
    syslogtag = models.CharField(max_length=180, db_column='SysLogTag', blank=True) 
    eventlogtype = models.CharField(max_length=180, db_column='EventLogType', blank=True) 
    genericfilename = models.CharField(max_length=180, db_column='GenericFileName', blank=True) 
    systemid = models.IntegerField(null=True, db_column='SystemID', blank=True) 
    processid = models.CharField(max_length=180)
    class Meta:
        db_table = u'SystemEvents'

 


