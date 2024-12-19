from django.contrib.auth.models import Group, User
from .models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 'username', 'email', 'groups']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class ContinentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Continent
        fields = '__all__'
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}

class CohortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cohort
        fields = '__all__'
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}

class RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reward
        fields = '__all__'
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}

class TransactionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionType
        fields = '__all__'
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}

class TransactionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Transaction
        fields = '__all__'
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}

class AccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Access
        fields = '__all__'
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}

class MemberRewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberReward
        fields = '__all__'
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}

class EventTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventType
        fields = '__all__'
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}

class RoleAccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleAccess
        fields = '__all__'
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}

class MemberStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberStatus
        fields = '__all__'
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}

class MemberTimelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberStatusTimeline
        fields = '__all__'
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}

class SessionAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SessionAttendance
        fields = '__all__'
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}

class AlertTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlertType
        fields = '__all__'
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}

class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = '__all__'
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}

class MemberScoreCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberScoreCard
        fields = '__all__'
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}

class MemberScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberScore
        fields = '__all__'
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}

class PaymentModeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMode
        fields = '__all__'
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}

class TribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tribe
        fields = '__all__'
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}

class MemberTribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberTribe
        fields = '__all__'
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}

class CohortRolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CohortRole
        fields = '__all__'
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}

class RegionalRolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegionRole
        fields = '__all__'
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}

class CohortRolesAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CohortRoleAssignment
        fields = '__all__'
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}

class RegionalRolesAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegionRoleAssignment
        fields = '__all__'
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}

class CohortCalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CohortCalendar
        fields = '__all__'
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}

class RegionCalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegionCalendar
        fields = '__all__'
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}

class CityCalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityCalendar
        fields = '__all__'
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}

class StateCalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = StateCalendar
        fields = '__all__'
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}

class CountryCalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryCalendar
        fields = '__all__'
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}

class ContinentCalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContinentCalendar
        fields = '__all__'
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}

class InvitationCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = InvitationCategory
        fields = '__all__'
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}

class InviteeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitee
        fields = '__all__'
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}

class CohortInvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CohortInvitation
        fields = '__all__'
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}

class RegionInvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegionInvitation
        fields = '__all__'
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}

class CohortAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CohortAttendance
        fields = '__all__'
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}

class RegionAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegionAttendance
        fields = '__all__'
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}

class CohortScoreCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CohortScoreCard
        fields = '__all__'
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}

class CohortScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = CohortScore
        fields = '__all__'
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}

class RegionScoreCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegionScoreCard
        fields = '__all__'
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}

class RegionScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegionScore
        fields = '__all__'
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}

class MembershipApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MembershipApplication
        fields = '__all__'
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}

class ApplicationCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationCategory
        fields = '__all__'
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}

class MembershipApplicationStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = MembershipApplicationStatus
        fields = '__all__'
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}

