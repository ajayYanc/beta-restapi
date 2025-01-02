from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import json
# Create your models here.
User._meta.get_field('email')._unique = True

class Continent(models.Model):

  class Meta:
    permissions = [
        ("rename_continent", "Can rename the continent"),
        ("update_code_continent", "Can update code for a continent"),
    ]

  name = models.CharField(max_length=255)
  code = models.CharField(primary_key=True, max_length=25)

  created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
  created_at = models.DateTimeField(default=timezone.now, editable=False)

  #def save(self, *args, **kwargs):
    #self.created_by = self.request.user
  #  super(Continent, self).save(*args, **kwargs)

  def save(self, *args, **kwargs):

    #self.code = self.region.code + "-" + self.name
    
    detail = {}
   
    detail['name'] = self.name
    detail['code'] = self.code
     
    transaction = Transaction.objects.create(type_id=4, detail=detail, status=True,created_by=self.created_by)

    super(Continent, self).save(*args, **kwargs)    

#def __str__(self):
  #return self.code
    
class Country(models.Model):

  continent = models.ForeignKey(Continent, on_delete=models.CASCADE)
  name = models.CharField(max_length=255)
  code = models.CharField(primary_key=True, max_length=25)
 
  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=timezone.now, editable=False)
  
  def save(self, *args, **kwargs):
       
    detail = {}   
    detail['name'] = self.name
    detail['code'] = self.code
    detail['continent'] = self.continent.code

    transaction = Transaction.objects.create(type_id=10, detail=detail, status=True,created_by=self.created_by)

    super(Country, self).save(*args, **kwargs)  

  #def __str__(self):
  #  return self.code
  
class State(models.Model):
  country = models.ForeignKey(Country, on_delete=models.CASCADE)
  name = models.CharField(max_length=255)
  code = models.CharField(primary_key=True, max_length=25)

  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=timezone.now, editable=False)

  def save(self, *args, **kwargs):              
    detail = {}   
    detail['name'] = self.name
    detail['code'] = self.code
    detail['continent'] = self.country.code

    transaction = Transaction.objects.create(type_id=11, detail=detail, status=True,created_by=self.created_by)
    super(State, self).save(*args, **kwargs) 

 # def __str__(self):
  #  return self.code
  
class City(models.Model):
  state = models.ForeignKey(State, on_delete=models.CASCADE)
  name = models.CharField(max_length=255)
  code = models.CharField(primary_key=True, max_length=25)

  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=timezone.now, editable=False)

  def save(self, *args, **kwargs):              
    detail = {}   
    detail['name'] = self.name
    detail['code'] = self.code
    detail['continent'] = self.state.code

    transaction = Transaction.objects.create(type_id=12, detail=detail, status=True,created_by=self.created_by)
    super(City, self).save(*args, **kwargs)


  #def __str__(self):
   # return self.code
  
class Region(models.Model):
  city = models.ForeignKey(City, on_delete=models.CASCADE)
  name = models.CharField(max_length=255)
  code = models.CharField(max_length=25, primary_key=True)

  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=timezone.now, editable=False)
  
  def save(self, *args, **kwargs):              
    detail = {}   
    detail['name'] = self.name
    detail['code'] = self.code
    detail['continent'] = self.city.code

    transaction = Transaction.objects.create(type_id=12, detail=detail, status=True,created_by=self.created_by)
    super(Region, self).save(*args, **kwargs)


  #def __str__(self):
    #return self.code
  
class Cohort(models.Model):
  region = models.ForeignKey(Region, on_delete=models.CASCADE)
  name = models.CharField(max_length=255)
  code = models.CharField(max_length=25, primary_key=True)
  status = models.BooleanField()

  created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
  created_at = models.DateTimeField(default=timezone.now, editable=False)

  def save(self, *args, **kwargs):

    self.code = self.region.code + "-" + self.name
    
    detail = {}
    detail['region'] = self.region.code
    detail['name'] = self.name
    detail['code'] = self.code
    detail['status'] = self.status
  
    transaction = Transaction.objects.create(type_id=1, detail=detail, status=True, created_by=self.created_by)
    
    super(Cohort, self).save(*args, **kwargs)    

  #def __str__(self):
  #  return self.code
  
  
class Role(models.Model):
  name = models.CharField(max_length=255)
  code = models.CharField(max_length=25, primary_key=True)

  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=timezone.now, editable=False)

  def __str__(self):
        return self.code
  
class Reward(models.Model):
  name = models.CharField(max_length=255)
  code = models.CharField(max_length=25, primary_key=True)

  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=timezone.now, editable=False)
  def save(self, *args, **kwargs):
    detail = {}
    detail['name'] = self.name        
    detail['code'] = self.code
    transaction = Transaction.objects.create(type_id=14, detail=detail, status=True, created_by=self.created_by) 
    #MT = MemberTribe.objects.create_user(username=self.invitee.email,first_name=self.invitee.first_name,last_name=self.invitee.last_name, email=self.invitee.email) 
    super(Reward, self).save(*args, **kwargs) 


 # def __str__(self):
 #       return self.code
  
 
class TransactionType(models.Model):
  name = models.CharField(max_length=255)
  code = models.CharField(max_length=25)

  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=timezone.now, editable=False)

  
  def __str__(self):
        return self.code
  
class Member(models.Model):
  cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)
  name = models.CharField(max_length=255)
  code = models.AutoField(primary_key=True)
  hobbies = models.CharField(max_length=255, null=True, blank=True)
  school = models.CharField(max_length=255, null=True, blank=True)  
  status = models.BooleanField()
  user = models.OneToOneField(User, related_name="user", on_delete=models.CASCADE)
  referred_by = models.ForeignKey(User, related_name="referred_by", on_delete=models.CASCADE)

  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=timezone.now, editable=False)
  
   
  def save(self, *args, **kwargs):
    
    #self.code = self.cohort.code + "-" + self.name          
    detail = {}
    detail['cohort'] = self.cohort.code
    detail['name'] = self.name    
    detail['hobbies'] = self.hobbies
    detail['school'] = self.school
    detail['status'] = self.status
    detail['referred_by'] = self.referred_by.email
    detail['user'] = self.user.username
    #print(detail)
    super(Member, self).save(*args, **kwargs)      
    detail['code'] = self.code
    transaction = Transaction.objects.create(type_id=5, detail=detail, status=True, created_by=self.created_by) 
    #MT = MemberTribe.objects.create_user(username=self.invitee.email,first_name=self.invitee.first_name,last_name=self.invitee.last_name, email=self.invitee.email) 

  #def __str__(self):
  #return self.cohort.code + " | " + self.name + " | " + str(self.code)

class InvitationCategory(models.Model):
  name = models.CharField(max_length=255)
  code = models.CharField(max_length=10, primary_key=True)

  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=timezone.now, editable=False)

  def __str__(self):
      return self.name

class Invitee(models.Model):
  category = models.ForeignKey(InvitationCategory, on_delete=models.CASCADE)
  email = models.EmailField()
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  member = models.ForeignKey(Member, on_delete=models.CASCADE)

  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=timezone.now, editable=False)

  def save(self, *args, **kwargs):
    detail = {}
    detail['category']=self.category.name
    detail['first_name']=self.first_name
    detail['last_name']=self.last_name
    detail['referred_by']=self.member.name
    transaction = Transaction.objects.create(type_id=8, detail=detail, status=True, created_by=self.created_by)
    super(Invitee, self).save(*args, **kwargs)   


  #def __str__(self):
      #return self.email

class Transaction(models.Model):
  type = models.ForeignKey(TransactionType, on_delete=models.CASCADE)
  detail = models.JSONField()
  status = models.BooleanField()

  created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
  created_at = models.DateTimeField(default=timezone.now, editable=False)


class Access(models.Model):
  name = models.CharField(max_length=255)
  code = models.CharField(max_length=25, primary_key=True)

  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=timezone.now, editable=False)


  def __str__(self):
        return self.code
  
class MemberReward(models.Model):
  member = models.ForeignKey(Member, on_delete=models.CASCADE)
  reward = models.ForeignKey(Reward, on_delete=models.CASCADE)
  date = models.DateField()

  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=timezone.now, editable=False)


class Session(models.Model):
  name = models.CharField(max_length=255)
  code = models.CharField(max_length=25, primary_key=True)  
  duration = models.IntegerField()

  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=timezone.now, editable=False)


  def __str__(self):
      return self.code

class EventType(models.Model):
  name = models.CharField(max_length=255)
  code = models.CharField(max_length=25, primary_key=True)
  session = models.ManyToManyField(Session)

  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=timezone.now, editable=False)

  def save(self, *args, **kwargs):
    detail = {}
    detail['name'] = self.name
    detail['code'] = self.code
    
  
    transaction = Transaction.objects.create(type_id=7, detail=detail, status=True, created_by=self.created_by)
    
    super(EventType, self).save(*args, **kwargs) 
     
  #def __str__(self):
         # return self.code
  
class RoleAccess(models.Model):
  role = models.ForeignKey(Role, on_delete=models.CASCADE)
  access = models.ForeignKey(Access, on_delete=models.CASCADE)

  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=timezone.now, editable=False)


class MemberStatus(models.Model):
  name = models.CharField(max_length=255)
  code = models.CharField(max_length=25, primary_key=True)

  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=timezone.now, editable=False)


  def __str__(self):
      return self.code

class MemberStatusTimeline(models.Model):
  status = models.ForeignKey(MemberStatus, on_delete=models.CASCADE)
  start = models.DateField()
  end = models.DateField()
  member = models.ForeignKey(Member, on_delete=models.CASCADE)

  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=timezone.now, editable=False)


class SessionAttendance(models.Model):
  session = models.ForeignKey(Session, on_delete=models.CASCADE)
  invitee = models.ManyToManyField(Invitee)
  member = models.ManyToManyField(Member)
  notes = models.CharField(max_length=1024)

  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=timezone.now, editable=False)


class AlertType(models.Model):
  name = models.CharField(max_length=25)
  code = models.CharField(max_length=25, primary_key=True)

  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=timezone.now, editable=False)


  def __str__(self):
      return self.code

class Alert(models.Model):
  type = models.ForeignKey(AlertType, on_delete=models.CASCADE)
  timestamp = models.DateTimeField()   

  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=timezone.now, editable=False)

   

class MemberScoreCard(models.Model):
  activity = models.CharField(max_length=255)
  code = models.CharField(max_length=10, primary_key=True)
  score = models.IntegerField()

  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=timezone.now, editable=False)


class MemberScore(models.Model):
  score = models.IntegerField()
  member = models.OneToOneField(Member, on_delete=models.CASCADE)
  date = models.DateTimeField()

  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=timezone.now, editable=False)


class PaymentMode(models.Model):
  name = models.CharField(max_length=10)
  code = models.CharField(max_length=5, primary_key=True)

  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=timezone.now, editable=False)


  def __str__(self):
      return self.code

class Tribe(models.Model):
  name = models.CharField(max_length=15)
  code = models.CharField(max_length=5, primary_key=True)  
  fee = models.FloatField()
  discount = models.FloatField()

  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=timezone.now, editable=False)


  def __str__(self):
      return self.code

class MemberTribe(models.Model):
  member = models.ForeignKey(Member, on_delete=models.CASCADE)
  tribe = models.ForeignKey(Tribe, on_delete=models.CASCADE)
  start = models.DateField()
  end = models.DateField()
  

  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=timezone.now, editable=False)

  def save(self, *args, **kwargs):       
       detail = {}
       detail['member']=self.member.code
       detail['tribe'] = self.tribe.code
       detail['start']=self.start.strftime(("%m/%d/%Y, %H:%M:%S"))
       detail['end']=self.end.strftime(("%m/%d/%Y, %H:%M:%S"))
      
       transaction = Transaction.objects.create(type_id=6, detail=detail, status=True, created_by=self.created_by)
       super(MemberTribe, self).save(*args, **kwargs)  

class CohortRole(models.Model):
  name = models.CharField(max_length=25)
  code = models.CharField(max_length=10, primary_key=True)

  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=timezone.now, editable=False)


class CohortMemberRole(models.Model):
  role = models.ForeignKey(CohortRole, on_delete=models.CASCADE)
  member = models.ForeignKey(Member, on_delete=models.CASCADE)
  start = models.DateTimeField()
  end = models.DateTimeField()

  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=timezone.now, editable=False)


  def __str__(self):
     return self.role.code + ' | ' + self.member.name

class CohortRoleAssignment(models.Model):
  cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)
  assignment = models.ManyToManyField(CohortMemberRole)

  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=timezone.now, editable=False)


class RegionRole(models.Model):
  name = models.CharField(max_length=25)
  code = models.CharField(max_length=10, primary_key=True)

  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=timezone.now, editable=False)


class RegionRoleAssignment(models.Model):
  member = models.ForeignKey(Member, on_delete=models.CASCADE)
  role = models.ManyToManyField(RegionRole)

  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=timezone.now, editable=False)


class CohortCalendar(models.Model):
  cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)
  event = models.ForeignKey(EventType, on_delete=models.CASCADE)
  day = models.DateTimeField()
  duration = models.IntegerField()
  location = models.CharField(max_length=255)

  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=timezone.now, editable=False)


  def __str__(self):
      return self.cohort.code + ' || ' + str(self.day)

class RegionCalendar(models.Model):
  region = models.ForeignKey(Region, on_delete=models.CASCADE)
  event = models.ForeignKey(EventType, on_delete=models.CASCADE)
  day = models.DateTimeField()
  duration = models.IntegerField()
  location = models.CharField(max_length=255)

  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=timezone.now, editable=False)


class CityCalendar(models.Model):
  city = models.ForeignKey(City, on_delete=models.CASCADE)
  event = models.ForeignKey(EventType, on_delete=models.CASCADE)
  day = models.DateTimeField()
  duration = models.IntegerField()
  location = models.CharField(max_length=255)

  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=timezone.now, editable=False)


class StateCalendar(models.Model):
  state = models.ForeignKey(State, on_delete=models.CASCADE)
  event = models.ForeignKey(EventType, on_delete=models.CASCADE)
  day = models.DateTimeField()
  duration = models.IntegerField()
  location = models.CharField(max_length=255)

  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=timezone.now, editable=False)


class CountryCalendar(models.Model):
  country = models.ForeignKey(Country, on_delete=models.CASCADE)
  event = models.ForeignKey(EventType, on_delete=models.CASCADE)
  day = models.DateTimeField()
  duration = models.IntegerField()
  location = models.CharField(max_length=255)

  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=timezone.now, editable=False)

class ContinentCalendar(models.Model):
  continent = models.ForeignKey(Continent, on_delete=Continent)
  event = models.ForeignKey(EventType, on_delete=models.CASCADE)
  day = models.DateTimeField()
  duration = models.IntegerField()
  location = models.CharField(max_length=255)

  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=timezone.now, editable=False)


class Payment(models.Model):
  payfor = models.ForeignKey(Tribe, on_delete=models.CASCADE)
  type = models.ForeignKey(PaymentMode, on_delete=models.CASCADE)
  invitee = models.ForeignKey(Invitee, on_delete=models.CASCADE)
  status = models.BooleanField()
  discount = models.FloatField()

  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=timezone.now, editable=False)

  def save(self, *args, **kwargs):
    user = User.objects.create_user(username=self.invitee.email,first_name=self.invitee.first_name,last_name=self.invitee.last_name, email=self.invitee.email)
          
    detail = {}
    detail['payfor'] = self.payfor.code
    detail['type'] = self.type.code
    detail['invitee'] = self.invitee.category.code
    detail['status'] = self.status
    detail['discount'] = self.discount
  
    #transaction = Transaction.objects.create(type=9,timestamp=timezone.now, detail=detail, status='OK')
    transaction = Transaction.objects.create(type_id=9,created_by=self.created_by, detail=detail, status=True)
    if not user:
        raise Exception("user not created!")
    super(Payment, self).save(*args, **kwargs)    

class CohortInvitation(models.Model):
  cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)
  event = models.ForeignKey(CohortCalendar, on_delete=models.CASCADE)
  Invitee = models.ForeignKey(Invitee, on_delete=models.CASCADE)
  member = models.ForeignKey(Member, on_delete=models.CASCADE)

  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=timezone.now, editable=False)


class RegionInvitation(models.Model):
  region = models.ForeignKey(Region, on_delete=models.CASCADE)
  event = models.ForeignKey(RegionCalendar, on_delete=models.CASCADE)
  invitee = models.ManyToManyField(Invitee)
  referred_by = models.ForeignKey(Member, on_delete=models.CASCADE)

  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=timezone.now, editable=False)


class CohortAttendance(models.Model):
  cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)
  event = models.ForeignKey(CohortCalendar, on_delete=models.CASCADE)
  attendance = models.ManyToManyField(SessionAttendance)

  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=timezone.now, editable=False)


class RegionAttendance(models.Model):
  region = models.ForeignKey(Region, on_delete=models.CASCADE)
  event = models.ForeignKey(RegionCalendar, on_delete=models.CASCADE)
  attendance = models.ManyToManyField(SessionAttendance)

  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=timezone.now, editable=False)



class CohortScoreCard(models.Model):
  activity = models.CharField(max_length=255)
  code = models.CharField(max_length=10, primary_key=True)
  score = models.IntegerField()

  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=timezone.now, editable=False)


class CohortScore(models.Model):
  cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)
  score = models.IntegerField()
  date = models.DateTimeField()

  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=timezone.now, editable=False)


class RegionScoreCard(models.Model):
  activity = models.CharField(max_length=255)
  code = models.CharField(max_length=10, primary_key=True)
  score = models.IntegerField()

  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=timezone.now, editable=False)


class RegionScore(models.Model):
  region = models.ForeignKey(Region, on_delete=models.CASCADE)
  score = models.IntegerField()
  date = models.DateTimeField()

  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=timezone.now, editable=False)

class ApplicationCategory(models.Model):
  name = models.CharField(max_length=255, primary_key=True)
  code = models.CharField(max_length=15)

  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=timezone.now, editable=False)


class MembershipApplication(models.Model):
  applied_by = models.OneToOneField(Invitee, primary_key=True, on_delete=models.CASCADE)
  category = models.ForeignKey(ApplicationCategory, on_delete=models.CASCADE)
  info = models.CharField(max_length=255)

  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=timezone.now, editable=False)


class MembershipApplicationStatus(models.Model):
  application = models.OneToOneField(MembershipApplication, primary_key=True, on_delete=models.CASCADE)
  status = models.CharField(max_length=255)
  date = models.DateTimeField()

  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=timezone.now, editable=False)


class SupportCategory(models.Model):

  name = models.CharField(max_length=255)
  code = models.CharField(max_length=10, primary_key=True)

  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=timezone.now, editable=False)


class Support(models.Model):

  category = models.ForeignKey(SupportCategory, on_delete=models.CASCADE)
  description = models.CharField(max_length=255)
  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=timezone.now, editable=False)
  ticket_id = models.AutoField(primary_key=True)


class SupportTicketStatus(models.Model):
  name = models.CharField(max_length=255)
  code = models.CharField(max_length=10, primary_key=True)

  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=timezone.now, editable=False)


class SupportStatus(models.Model):
  ticket_id = models.ForeignKey(Support, on_delete=models.CASCADE)
  status = models.ForeignKey(SupportTicketStatus, on_delete=models.CASCADE)
  comments = models.CharField(max_length=255)

  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=timezone.now, editable=False)

