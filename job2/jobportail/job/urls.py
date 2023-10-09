
from django.urls import path


from job import views

urlpatterns = [

    path('', views.index,name='index'),
    path('admin_login/',views.admin_login, name='admin_login'),
    path('user_login',views.user_login,name='user_login'),
    path('user_signup',views.user_signup,name='user_signup'),
    path('user_home',views.user_home,name='user_home'),
    path('recruiter_home',views.recruiter_home,name='recruiter_home'),
    path('admin_home',views.admin_home,name='admin_home'),
    path('view_users',views.view_users,name='view_users'),
    path('recruiter_pending',views.recruiter_pending,name='recruiter_pending'),
    path('delete_users/<int:pid>',views.delete_users,name='delete_users'),
    path('delete_recruiter/<int:pid>',views.delete_recruiter,name='delete_recruiter'),
    path('change_status/<int:pid>',views.change_status,name='change_status'),
    path('change_companylogo/<int:pid>',views.change_companylogo,name='change_companylogo'),
    path('edit_jobdetail/<int:pid>',views.edit_jobdetail,name='edit_jobdetail'),
    path('delete_jobdetail/<int:pid>',views.delete_jobdetail,name='delete_jobdetail'),
    path('Logout',views.Logout,name='Logout'),
    path('change_passwordadmin',views.change_passwordadmin,name='change_passwordadmin'),
    path('change_passworduser',views.change_passworduser,name='change_passworduser'),
    path('change_passwordrecruiter',views.change_passwordrecruiter,name='change_passwordrecruiter'),
    path('recruiter_signup',views.recruiter_signup,name='recruiter_signup'),
    path('recruiter_accepted',views.recruiter_accepted,name='recruiter_accepted'),
    path('recruiter_rejected',views.recruiter_rejected,name='recruiter_rejected'),
    path('recruiter_all',views.recruiter_all,name='recruiter_all'),
    path('add_job',views.add_job,name='add_job'),
    path('contact/',views.contact,name='contact'),
    path('job_list/',views.job_list,name='job_list'),
    path('job_detail/<int:pid>',views.job_detail,name='job_detail'),
    path('latest_jobs',views.latest_jobs,name='latest_jobs'),
    path('user_latestjobs',views.user_latestjobs,name='user_latestjobs'),
    path('applyforjob/<int:pid>',views.applyforjob, name='applyforjob'),
    path('applied_candidatelist',views.applied_candidatelist,name='applied_candidatelist'),
    path('recruiter_login',views.recruiter_login,name='recruiter_login'),
]