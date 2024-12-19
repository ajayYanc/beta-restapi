from django.shortcuts import render
from rest_framework import permissions, viewsets
from rest_framework.permissions import DjangoModelPermissions
from django.contrib.auth.models import Group, User
from .serializers import *

from .models import *
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class ContinentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows continents to be viewed or edited.
    """
    queryset = Continent.objects.all().order_by('code')
    serializer_class = ContinentSerializer
    #permission_classes = [permissions.DjangoObjectPermissions]

class CountryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows continents to be viewed or edited.
    """
    queryset = Country.objects.all().order_by('code')
    serializer_class = CountrySerializer
    #permission_classes = [permissions.DjangoObjectPermissions]

class StateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows continents to be viewed or edited.
    """
    queryset = State.objects.all().order_by('code')
    serializer_class = StateSerializer
    #permission_classes = [permissions.DjangoObjectPermissions]

class CityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows continents to be viewed or edited.
    """
    queryset = City.objects.all().order_by('code')
    serializer_class = CitySerializer
    #permission_classes = [permissions.DjangoObjectPermissions]

class RegionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows continents to be viewed or edited.
    """
    queryset = Region.objects.all().order_by('code')
    serializer_class = RegionSerializer
    #permission_classes = [permissions.DjangoObjectPermissions]

class CohortViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cohorts to be viewed or edited.
    """
    queryset = Cohort.objects.all().order_by('code')
    serializer_class = CohortSerializer
    #permission_classes = [permissions.DjangoObjectPermissions]

class RoleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows roles to be viewed or edited.
    """
    queryset = Role.objects.all().order_by('code')
    serializer_class = RoleSerializer
    #permission_classes = [permissions.DjangoObjectPermissions]

class RewardViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows rewards to be viewed or edited.
    """
    queryset = Reward.objects.all().order_by('code')
    serializer_class = RewardSerializer
    #permission_classes = [permissions.DjangoObjectPermissions]

class TransactionTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows transactiontype to be viewed or edited.
    """
    queryset = TransactionType.objects.all().order_by('code')
    serializer_class = TransactionTypeSerializer
    #permission_classes = [permissions.DjangoObjectPermissions]


class MemberViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows members to be viewed or edited.
    """
    queryset = Member.objects.all().order_by('code')
    serializer_class = MemberSerializer
    #permission_classes = [permissions.DjangoObjectPermissions]

class TransactionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows transaction to be viewed or edited.
    """
    queryset = Transaction.objects.all().order_by('created_at')
    serializer_class = TransactionSerializer
    #permission_classes = [permissions.DjangoObjectPermissions]
    def perform_create(self, serializer):
            serializer.save(created_by=self.request.user)

class AccessViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows members to be viewed or edited.
    """
    queryset = Access.objects.all().order_by('code')
    serializer_class = AccessSerializer
    #permission_classes = [permissions.DjangoObjectPermissions]

class MemberRewardViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows members to be viewed or edited.
    """
    queryset = MemberReward.objects.all().order_by('member')
    serializer_class = MemberRewardSerializer
    #permission_classes = [permissions.DjangoObjectPermissions]

class SessionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows members to be viewed or edited.
    """
    queryset = Session.objects.all().order_by('code')
    serializer_class = SessionSerializer
    #permission_classes = [permissions.DjangoObjectPermissions]

class EventTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows members to be viewed or edited.
    """
    queryset = EventType.objects.all().order_by('code')
    serializer_class = EventTypeSerializer
    #permission_classes = [permissions.DjangoObjectPermissions]

class RoleAccessViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows members to be viewed or edited.
    """
    queryset = RoleAccess.objects.all().order_by('role')
    serializer_class = RoleAccessSerializer
    #permission_classes = [permissions.DjangoObjectPermissions]

class MemberStatusViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows members to be viewed or edited.
    """
    queryset = MemberStatus.objects.all().order_by('code')
    serializer_class = MemberStatusSerializer
    #permission_classes = [permissions.DjangoObjectPermissions]

class MemberTimelineViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows members to be viewed or edited.
    """
    queryset = MemberStatusTimeline.objects.all().order_by('member')
    serializer_class = MemberTimelineSerializer
    #permission_classes = [permissions.DjangoObjectPermissions]

class SessionAttendanceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows members to be viewed or edited.
    """
    queryset = SessionAttendance.objects.all().order_by('session')
    serializer_class = SessionAttendanceSerializer
    #permission_classes = [permissions.DjangoObjectPermissions]

class AlertTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows members to be viewed or edited.
    """
    queryset = AlertType.objects.all().order_by('code')
    serializer_class = AlertTypeSerializer
    #permission_classes = [permissions.DjangoObjectPermissions]

class AlertViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows members to be viewed or edited.
    """
    queryset = Alert.objects.all().order_by('timestamp')
    serializer_class = AlertSerializer
    #permission_classes = [permissions.DjangoObjectPermissions]

class MemberScoreCardViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows members to be viewed or edited.
    """
    queryset = MemberScoreCard.objects.all().order_by('code')
    serializer_class = MemberScoreCardSerializer
    #permission_classes = [permissions.DjangoObjectPermissions]

class MemberScoreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows members to be viewed or edited.
    """
    queryset = MemberScore.objects.all().order_by('member')
    serializer_class = MemberScoreSerializer
    #permission_classes = [permissions.DjangoObjectPermissions]

class PaymentModeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows members to be viewed or edited.
    """
    queryset = PaymentMode.objects.all().order_by('code')
    serializer_class = PaymentModeSerializer
    #permission_classes = [permissions.DjangoObjectPermissions]

class TribeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows members to be viewed or edited.
    """
    queryset = Tribe.objects.all().order_by('code')
    serializer_class = TribeSerializer
    #permission_classes = [permissions.DjangoObjectPermissions]

class PaymentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows members to be viewed or edited.
    """
    queryset = Payment.objects.all().order_by('invitee')
    serializer_class = PaymentSerializer
    #permission_classes = [permissions.DjangoObjectPermissions]

class MemberTribeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows members to be viewed or edited.
    """
    queryset = MemberTribe.objects.all().order_by('member')
    serializer_class = MemberTribeSerializer
    #permission_classes = [permissions.DjangoObjectPermissions]

class CohortRoleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows members to be viewed or edited.
    """
    queryset = CohortRole.objects.all().order_by('code')
    serializer_class = CohortRolesSerializer
    #permission_classes = [permissions.DjangoObjectPermissions]

class RegionRoleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows members to be viewed or edited.
    """
    queryset = RegionRole.objects.all().order_by('code')
    serializer_class = RegionalRolesSerializer
    #permission_classes = [permissions.DjangoObjectPermissions]

class CohortRoleAssignmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows members to be viewed or edited.
    """
    queryset = CohortRoleAssignment.objects.all().order_by('cohort')
    serializer_class = CohortRolesAssignmentSerializer
    #permission_classes = [permissions.DjangoObjectPermissions]

class RegionRoleAssignmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows members to be viewed or edited.
    """
    queryset = RegionRoleAssignment.objects.all().order_by('role')
    serializer_class = RegionalRolesAssignmentSerializer
    #permission_classes = [permissions.DjangoObjectPermissions]

class CohortCalendarViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows members to be viewed or edited.
    """
    queryset = CohortCalendar.objects.all().order_by('cohort')
    serializer_class = CohortCalendarSerializer
    #permission_classes = [permissions.DjangoObjectPermissions]

class RegionCalendarViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows members to be viewed or edited.
    """
    queryset = RegionCalendar.objects.all().order_by('region')
    serializer_class = RegionCalendarSerializer
    #permission_classes = [permissions.DjangoObjectPermissions]

class CityCalendarViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows members to be viewed or edited.
    """
    queryset = CityCalendar.objects.all().order_by('city')
    serializer_class = CityCalendarSerializer
    #permission_classes = [permissions.DjangoObjectPermissions]

class StateCalendarViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows members to be viewed or edited.
    """
    queryset = StateCalendar.objects.all().order_by('state')
    serializer_class = StateCalendarSerializer
    #permission_classes = [permissions.DjangoObjectPermissions]

class CountryCalendarViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows members to be viewed or edited.
    """
    queryset = CountryCalendar.objects.all().order_by('country')
    serializer_class = CountryCalendarSerializer
    #permission_classes = [permissions.DjangoObjectPermissions]

class ContinentCalendarViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows members to be viewed or edited.
    """
    queryset = ContinentCalendar.objects.all().order_by('continent')
    serializer_class = ContinentCalendarSerializer
    #permission_classes = [permissions.DjangoObjectPermissions]

class InviteeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows members to be viewed or edited.
    """
    queryset = Invitee.objects.all().order_by('email')
    serializer_class = InviteeSerializer
    #permission_classes = [permissions.DjangoObjectPermissions]

class InvitationCategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows members to be viewed or edited.
    """
    queryset = InvitationCategory.objects.all().order_by('code')
    serializer_class = InvitationCategorySerializer
    #permission_classes = [permissions.DjangoObjectPermissions]

class CohortInvitationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows members to be viewed or edited.
    """
    queryset = CohortInvitation.objects.all().order_by('event')
    serializer_class = CohortInvitationSerializer
    #permission_classes = [permissions.DjangoObjectPermissions]

class RegionInvitationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows members to be viewed or edited.
    """
    queryset = RegionInvitation.objects.all().order_by('event')
    serializer_class = RegionInvitationSerializer
    #permission_classes = [permissions.DjangoObjectPermissions]

class CohortAttendanceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows members to be viewed or edited.
    """
    queryset = CohortAttendance.objects.all().order_by('event')
    serializer_class = CohortAttendanceSerializer
    #permission_classes = [permissions.DjangoObjectPermissions]

class RegionAttendanceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows members to be viewed or edited.
    """
    queryset = RegionAttendance.objects.all().order_by('event')
    serializer_class = RegionAttendanceSerializer
    #permission_classes = [permissions.DjangoObjectPermissions]

class CohortScoreCardViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows members to be viewed or edited.
    """
    queryset = CohortScoreCard.objects.all().order_by('code')
    serializer_class = CohortScoreCardSerializer
    #permission_classes = [permissions.DjangoObjectPermissions]

class CohortScoreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows members to be viewed or edited.
    """
    queryset = CohortScore.objects.all().order_by('score')
    serializer_class = CohortScoreSerializer
    #permission_classes = [permissions.DjangoObjectPermissions]

class RegionScoreCardViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows members to be viewed or edited.
    """
    queryset = RegionScoreCard.objects.all().order_by('code')
    serializer_class = RegionScoreCardSerializer
    #permission_classes = [permissions.DjangoObjectPermissions]

class RegionScoreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows members to be viewed or edited.
    """
    queryset = RegionScore.objects.all().order_by('score')
    serializer_class = RegionScoreSerializer
    #permission_classes = [permissions.DjangoObjectPermissions]

class MembershipApplicationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows members to be viewed or edited.
    """
    queryset = MembershipApplication.objects.all().order_by('applied_by')
    serializer_class = MembershipApplicationSerializer
    #permission_classes = [permissions.DjangoObjectPermissions]

class MembershipApplicationStatusViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows members to be viewed or edited.
    """
    queryset = MembershipApplicationStatus.objects.all().order_by('application')
    serializer_class = MembershipApplicationStatusSerializer
    #permission_classes = [permissions.DjangoObjectPermissions]

class ApplicationCategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows members to be viewed or edited.
    """
    queryset = ApplicationCategory.objects.all().order_by('code')
    serializer_class = ApplicationCategorySerializer
    #permission_classes = [permissions.DjangoObjectPermissions]
