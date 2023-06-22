from django.urls import path

from . import views

urlpatterns = [
    path("state-wise-list/", views.stateWiseList, name="stateWiseList"),
    path("calender-year-wise-list/", views.calenderWiseList, name="calenderWiseList"),
    path("financial-year-wise-list/", views.financialYearWiseList, name="financialYearWiseList"),
    path("received-application/", views.ReceivedApplication, name="ReceivedApplication"),
    path("search-record/", views.searchRecord, name="searchRecord"),
    path("registered-user/", views.registeredUsers, name="registeredUsers"),
    path("liquidation-list/", views.liquidationList, name="liquidationList"),
    path("bank-list/", views.bankList, name="bankList"),
    path("stateFetcher/", views.stateFetcher, name="stateFetcher"),
    path("districtFetcher/", views.districtFetcher, name="districtFetcher"),
    path("societyTypeFetcher/", views.societyTypeFetcher, name="societyTypeFetcher"),
    path("societyNameFetcher/", views.societyNameFetcher, name="societyNameFetcher"),
    path("userRegistration/", views.userRegistration, name="userRegistration"),
    path("deleteSociety/", views.deleteSociety, name="deleteSociety"),
    path("captchaFecther/", views.captchaFecther, name="captchaFecther"),
    path('loginUser/',views.loginUser,name="loginUser"),
    path('societyCountFetcher/',views.societyCountFetcher,name="societyCountFetcher"),
    path("", views.dataManipulator, name="dataManipulator"),

]