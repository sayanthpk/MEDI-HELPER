from diabetes_moule import views
from django.urls import path

urlpatterns = [
    path('', views.log),
    path('complaint',views.complaint),
    path('doctor',views.doctors),
    path('aprover',views.approver),
    path('rating',views.ratings),
    path('complaint_reply/<id>',views.replys),
    path('user',views.users),
    path('approved_doctors/<id>',views.approve_doctors),
    path('reject_doctors/<id>',views.reject_doctors),
    path('complaint',views.complaints),
    path('block/<id>',views.blockk),
    path('unblock/<id>',views.approve_doctors),
    path('home',views.home),

# ==================================================

    path('dhome',views.doctor_home),
    path('reg',views.registration),
    path('schedule',views.add_schedule),
    path('schedule_view',views.view_schedule),
    path('viewrating',views.view_rating),
    path('booking',views.view_booking),
    path('delete/<id>',views.delete_schedule),
    path('profile',views.view_profile),
    path('doctor_view_users',views.doctor_view_users),
    path('doctor_Chat_user/<id>',views.doctor_Chat_user),
    path('doctor_in_message2',views.doctor_in_message2),
    path('view_message2',views.view_message2),


# ==================================================

    path('and_login',views.and_log),
    path('and_complaint',views.and_complaint),
    path('and_reply',views.and_views),
    path('and_doctor',views.and_doctor),
    path('and_profile',views.and_viewprofile),
    path('and_update_profile',views.and_update_profile),
    path('and_schedule',views.and_schedule),
    path('and_reg',views.and_userregistration),
    path('and_book',views.and_book),
    path('and_booking',views.and_view_booking),

    # -------android chat---------------------------

 # path('in_message2',views.in_message2),
 path('view_message2',views.view_message2),
    path('view_th',views.and_chat_doctor),

    path('in_message_and', views.in_message_and),
    path('viewchat', views.viewchat),


    # =========================main section==========

    path('bmi_calc',views.bmii),
    path('diabetes_pred',views.diabet_prediction),
    path('skin_pred',views.skin_diseases),
    path('covid_pred',views.covid_prediction),
    path('obesity_pred',views.obesity_prediction),






]
