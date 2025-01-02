"""
URL configuration for yancproj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from yancapp import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'continents', views.ContinentViewSet)
router.register(r'countries', views.CountryViewSet)
router.register(r'states', views.StateViewSet)
router.register(r'cities', views.CityViewSet)
router.register(r'regions', views.RegionViewSet)
router.register(r'cohorts', views.CohortViewSet)
router.register(r'roles', views.RoleViewSet)
router.register(r'members', views.MemberViewSet)
router.register(r'transactiontypes', views.TransactionTypeViewSet)
router.register(r'transactions', views.TransactionViewSet)
router.register(r'access', views.AccessViewSet)
router.register(r'memberrewards', views.MemberRewardViewSet)
router.register(r'sessions', views.SessionViewSet)
router.register(r'eventtypes', views.EventTypeViewSet)
router.register(r'roleaccess', views.RoleAccessViewSet)
router.register(r'memberstatus', views.MemberStatusViewSet)
router.register(r'membertimeline', views.MemberTimelineViewSet)
router.register(r'sessionattendance', views.SessionAttendanceViewSet)
router.register(r'alerttypes', views.AlertTypeViewSet)
router.register(r'alerts', views.AlertViewSet)
router.register(r'memberscorecards', views.MemberScoreCardViewSet)
router.register(r'memberscores', views.MemberScoreViewSet)
router.register(r'paymentmodes', views.PaymentModeViewSet)
router.register(r'tribes', views.TribeViewSet)
router.register(r'payments', views.PaymentViewSet)
router.register(r'membertribes', views.MemberTribeViewSet)
router.register(r'cohortcalendars', views.CohortCalendarViewSet)
router.register(r'regioncalendars', views.RegionCalendarViewSet)
router.register(r'citycalendars', views.CityCalendarViewSet)
router.register(r'statecalendars', views.StateCalendarViewSet)
router.register(r'countrycalendars', views.CountryCalendarViewSet)
router.register(r'continentcalendars', views.ContinentCalendarViewSet)
router.register(r'invitationcategories', views.InvitationCategoryViewSet)
router.register(r'invitees', views.InviteeViewSet)
router.register(r'cohortinvitations', views.CohortInvitationViewSet)
router.register(r'regioninvitations', views.RegionInvitationViewSet)
router.register(r'cohortattendance', views.CohortAttendanceViewSet)
router.register(r'regionattendance', views.RegionAttendanceViewSet)
router.register(r'cohortscorecard', views.CohortScoreCardViewSet)
router.register(r'cohortscores', views.CohortScoreViewSet)
router.register(r'regionscorecard', views.RegionScoreCardViewSet)
router.register(r'regionscores', views.RegionScoreViewSet)
router.register(r'cohortroles', views.CohortRoleViewSet)
router.register(r'regionroles', views.RegionRoleViewSet)
router.register(r'cohortroleassignments', views.CohortRoleAssignmentViewSet)
router.register(r'regionroleassignments', views.RegionRoleAssignmentViewSet)
router.register(r'applicationcategories', views.ApplicationCategoryViewSet)
router.register(r'membershipapplications', views.MembershipApplicationViewSet)
router.register(r'membershipapplicationstatus', views.MembershipApplicationStatusViewSet)
router.register(r'rewards', views.RewardViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', include('drfpasswordless.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
