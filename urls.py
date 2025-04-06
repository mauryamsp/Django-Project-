from django.urls import path
from .import views,member_views
urlpatterns=[
path("",views.home,name="home"),
path("about/",views.about,name="about"),#"About/"-> end point
path("contact/",views.contact,name="contact"),
path("python/",views.python,name="python"),
path("core_java/",views.core_java,name="core_java"),
path("advance_java/",views.advance_java,name="advance_java"),
path("android/",views.android,name="android"),
path("iot/",views.iot,name="iot"),
path("courses/",views.courses,name="courses"),
path("mentors/",views.mentors,name="mentors"),
path("machine_learning/",views.machine_learning,name="machine_learning"),
path("registration/",member_views.registration,name="registration"),
path("student_login/",member_views.student_login,name="student_login"),
path("dashboard/", member_views.student_dashboard, name="dashboard"),
path("feedback/", member_views.feedback,name="feedback"),
path("querydoubt/",member_views.querydoubt,name="querydoubt"),
path("view_answer/",member_views.view_answer,name="view_answer"),
path("viewprofile/",member_views.viewprofile,name="viewprofile"),
path("logout/",member_views.logout,name="logout"),
path("rating/",member_views.rating,name="rating"),
path('connectedmediaclass/', member_views.connectedmediaclass, name='connectedmediaclass'),
path("faq/",views.faq,name="faq"),


]