from django.contrib import admin

# Register your models here.
from guardian.admin import GuardedModelAdmin
from yancapp.models import *

class ContinentAdmin(GuardedModelAdmin):
    pass

class CountryAdmin(GuardedModelAdmin):
    pass

class StateAdmin(GuardedModelAdmin):
    pass

class CityAdmin(GuardedModelAdmin):
    pass

class RegionAdmin(GuardedModelAdmin):
    pass

class CohortAdmin(GuardedModelAdmin):
    pass

class RoleAdmin(GuardedModelAdmin):
    pass

class RewardAdmin(GuardedModelAdmin):
    pass

class TransactionTypeAdmin(GuardedModelAdmin):
    pass

class TransactionAdmin(GuardedModelAdmin):
    pass

class SessionAdmin(GuardedModelAdmin):
    pass

class SessionAttendanceAdmin(GuardedModelAdmin):
    pass

class EventTypeAdmin(GuardedModelAdmin):
    pass

class MemberAdmin(GuardedModelAdmin):
    pass

class MemberRewardAdmin(GuardedModelAdmin):
    pass

class AccessAdmin(GuardedModelAdmin):
    pass

class RoleAccessAdmin(GuardedModelAdmin):
    pass

class CohortCalendarAdmin(GuardedModelAdmin):
    pass

class RegionCalendarAdmin(GuardedModelAdmin):
    pass

class CohortInvitationAdmin(GuardedModelAdmin):
    pass

class CohortSubstituteInvitationAdmin(GuardedModelAdmin):
    pass

class RegionInvitationAdmin(GuardedModelAdmin):
    pass

class PaymentAdmin(GuardedModelAdmin):
    pass

class PaymentModeAdmin(GuardedModelAdmin):
    pass

class TribeAdmin(GuardedModelAdmin):
    pass

class MemberTribeAdmin(GuardedModelAdmin):
    pass

class MemberStatusAdmin(GuardedModelAdmin):
    pass

class MemberStatusTimelineAdmin(GuardedModelAdmin):
    pass

class AlertTypeAdmin(GuardedModelAdmin):
    pass

class AlertAdmin(GuardedModelAdmin):
    pass

class MemberScoreCardAdmin(GuardedModelAdmin):
    pass

class MemberScoreAdmin(GuardedModelAdmin):
    pass

class CohortAttendanceAdmin(GuardedModelAdmin):
    pass

class RegionAttendanceAdmin(GuardedModelAdmin):
    pass

class CohortScoreCardAdmin(GuardedModelAdmin):
    pass

class CohortScoreAdmin(GuardedModelAdmin):
    pass

class CohortRoleAdmin(GuardedModelAdmin):
    pass

class CohortMemberRoleAdmin(GuardedModelAdmin):
    pass

class CohortRoleAssignmentAdmin(GuardedModelAdmin):
    pass

class RegionRoleAdmin(GuardedModelAdmin):
    pass

class CohortAttendanceAdmin(GuardedModelAdmin):
    pass

class InvitationCategoryAdmin(GuardedModelAdmin):
    pass

class InviteeAdmin(GuardedModelAdmin):
    pass

class MembershipApplicationAdmin(GuardedModelAdmin):
    pass

class MembershipApplicationStatusAdmin(GuardedModelAdmin):
    pass

class ApplicationCategoryAdmin(GuardedModelAdmin):
    pass


admin.site.register(Continent, ContinentAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Cohort, CohortAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Reward, RewardAdmin)
admin.site.register(TransactionType, TransactionTypeAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Access, AccessAdmin)
admin.site.register(MemberReward, MemberRewardAdmin)
admin.site.register(Session, SessionAdmin)
admin.site.register(EventType, EventTypeAdmin)
admin.site.register(MemberScoreCard, MemberScoreCardAdmin)
admin.site.register(MemberScore, MemberScoreAdmin)
admin.site.register(CohortScoreCard, CohortScoreCardAdmin)
admin.site.register(CohortScore, CohortScoreAdmin)
admin.site.register(Alert, AlertAdmin)
admin.site.register(AlertType, AlertTypeAdmin)
admin.site.register(MemberStatusTimeline, MemberStatusTimelineAdmin)
admin.site.register(RoleAccess, RoleAccessAdmin)
admin.site.register(MemberStatus, MemberStatusAdmin)
admin.site.register(CohortRole, CohortRoleAdmin)
admin.site.register(CohortMemberRole, CohortMemberRoleAdmin)
admin.site.register(CohortRoleAssignment, CohortRoleAssignmentAdmin)
admin.site.register(RegionRole, RegionRoleAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(CohortCalendar, CohortCalendarAdmin)
admin.site.register(RegionCalendar, RegionCalendarAdmin)
admin.site.register(CohortAttendance, CohortAttendanceAdmin)
admin.site.register(SessionAttendance, SessionAttendanceAdmin)
admin.site.register(CohortInvitation, CohortInvitationAdmin)
admin.site.register(RegionInvitation, RegionInvitationAdmin)
admin.site.register(InvitationCategory, InvitationCategoryAdmin)
admin.site.register(Invitee, InviteeAdmin)
admin.site.register(PaymentMode, PaymentModeAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Tribe, TribeAdmin)
admin.site.register(MemberTribe, MemberTribeAdmin)
admin.site.register(RegionAttendance, RegionAttendanceAdmin)
admin.site.register(MembershipApplication, MembershipApplicationAdmin)
admin.site.register(MembershipApplicationStatus, MembershipApplicationStatusAdmin)
admin.site.register(ApplicationCategory, ApplicationCategoryAdmin)
