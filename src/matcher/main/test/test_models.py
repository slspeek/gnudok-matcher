
'''
Test module
'''
from __future__ import absolute_import
from django.test.testcases import TestCase
from nose.plugins.attrib import attr
from .__init__ import createZBPFixture
from ..models import Shift


@attr('functional')
class TrySomeQueries(TestCase):
    """ preliminary testing """
        
    def setUp(self):
        createZBPFixture(self)


    def test_do_some_queries(self):
        """ Count shifts at ZBP on monday """
        shifts_at_zbp_on_monday = Shift.objects.filter(
                          task__location=self.zbp,
                          day_of_week=1)
        self.assertEquals(2, len(shifts_at_zbp_on_monday.all()))
        
        
        

