from matcher.main.models import Capability, Employee, Location, Task, Shift, Attendance
import factory
import datetime
from django_factory_boy.auth import UserF, GroupF
from django.contrib.auth.models import User

def createRootUser(self): 
    self.root_user = User.objects.create_superuser('root', 'root@gnu.org', 'root')
    self.root_user.save()
    

def createZBPFixture(self):
    self.kassa_cap = CapabilityFactory(name='Kassa', description='Afrekenen')
    self.boeken_cap = CapabilityFactory(name='Boeken', description='Boeken prijzen en sorteren')
    self.zbp = LocationFactory(name='ZBP', description='Zeeburgerpad')
    self.marjolein_user = UserF(first_name='Marjolein', username='marjolein')
    self.beatrice_user = UserF(first_name='Beatrice', username='beatrice')
    self.marjolein = EmployeeFactory(parent=self.marjolein_user)
    self.marjolein.capabilities.add(self.boeken_cap)
    self.marjolein.save()
    self.beatrice = EmployeeFactory(parent=self.beatrice_user)
    self.beatrice.capabilities.add(self.kassa_cap)
    self.beatrice.save()
    self.kassa_boven = TaskFactory(name='Kassa studiedok',
                                   description="Kassa boven",
                                   location=self.zbp,
                                   capability=self.kassa_cap)
    self.boeken_sorteren = TaskFactory(name='Boeken sorteren',
                                   description="Boeken sorteren en censureren",
                                   location=self.zbp,
                                   capability=self.boeken_cap)
    self.marjolein_shift_ma = ShiftFactory(day_of_week=1,
                                      task=self.boeken_sorteren,
                                      employee=self.marjolein)
    self.marjolein_shift_wo = ShiftFactory(day_of_week=3,
                                      task=self.boeken_sorteren,
                                      employee=self.marjolein)
    self.beatrice_shift_ma = ShiftFactory(day_of_week=1,
                                      task= self.kassa_boven,
                                      employee=self.beatrice)
    

    

class CapabilityFactory(factory.Factory):
    FACTORY_FOR = Capability
    name = "Afwassen"
    description ="Met de blote hand servies reinigen"


class EmployeeFactory(factory.Factory):
    FACTORY_FOR = Employee
    parent = factory.SubFactory(UserF)
    type = Employee.VOLUNTEER


class LocationFactory(factory.Factory):
    FACTORY_FOR = Location
    name = "Zeeburgerpad"
    description = "Hoofdvestiging GNUDok"

class TaskFactory(factory.Factory):
    FACTORY_FOR = Task
    name = "Uitsmijter"
    description = "Zet vervelende klanten buiten de deur"
    location = factory.SubFactory(LocationFactory)
    capability = factory.SubFactory(CapabilityFactory)

class ShiftFactory(factory.Factory):
    FACTORY_FOR = Shift
    day_of_week = 1
    start_time = datetime.time(12, 30)
    stop_time = datetime.time(16, 30)
    task = factory.SubFactory(TaskFactory)
    employee = factory.SubFactory(EmployeeFactory)

class AttendanceFactory(factory.Factory):
    FACTORY_FOR = Attendance
    date = datetime.date(2012, 2, 22)
    shift = factory.SubFactory(ShiftFactory)
    start_time = datetime.time(12, 30)
    stop_time = datetime.time(16, 30)
    user_comment = "Voldaan gevoel"

