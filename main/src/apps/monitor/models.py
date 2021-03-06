from __future__ import unicode_literals

from django.db import models
from ..launchpad.models import Page

STATUSES = (
    (0, 'QUEUED'),
    (1, 'IN PROGRESS'),
    (2, 'PASS'),
    (3, 'FAIL'),
    (4, 'ERROR'),
)

BROWSERS = (
    (0, 'FIREFOX'),
    (1, 'CHROME')
)

class Test(models.Model):
    page = models.ForeignKey(Page)
    status = models.SmallIntegerField(default=0, choices=STATUSES)
    browser = models.SmallIntegerField(default=0, choices=BROWSERS)
    screenshot = models.CharField(max_length=255, null=True, default=None)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'tests'
        ordering = ['created_on',]
        get_latest_by = 'created_on'
