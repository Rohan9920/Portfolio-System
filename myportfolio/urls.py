from django.urls import path
from myportfolio.views import (
    PersonList,
    ProjectList,
    SkillList,
    PersonDetail,
    EducationDetail,
    ExperienceDetail,
    ProjectDetail,
    SkillDetail,
    EducationCreate,
    PersonCreate,
    ExperienceCreate,
    ProjectCreate,
    SkillCreate,
    PersonUpdate,
    EducationList,
    EducationUpdate,
    ExperienceList,
    ExperienceUpdate,
    ProjectUpdate,
    SkillUpdate,
    EducationDelete,
    PersonDelete,
    ExperienceDelete,
    ProjectDelete,
    SkillDelete,
)
urlpatterns = [
      path('person/',
           PersonList.as_view(),
           name='myportfolio_person_list_urlpattern'),

    path('person/<int:pk>/',
           PersonDetail.as_view(),
           name='myportfolio_person_detail_urlpattern'),

    path('person/create/',
           PersonCreate.as_view(),
           name='myportfolio_person_create_urlpattern'),

    path('person/<int:pk>/update/',
           PersonUpdate.as_view(),
           name='myportfolio_person_update_urlpattern'),

    path('person/<int:pk>/delete/',
           PersonDelete.as_view(),
           name='myportfolio_person_delete_urlpattern'),

    path('education/',
           EducationList.as_view(),
           name='myportfolio_education_list_urlpattern'),

    path('education/<int:pk>/',
           EducationDetail.as_view(),
           name='myportfolio_education_detail_urlpattern'),

    path('education/create/',
           EducationCreate.as_view(),
           name='myportfolio_education_create_urlpattern'),

    path('education/<int:pk>/update/',
           EducationUpdate.as_view(),
           name='myportfolio_education_update_urlpattern'),

    path('education/<int:pk>/delete/',
           EducationDelete.as_view(),
           name='myportfolio_education_delete_urlpattern'),

    path('experience/',
           ExperienceList.as_view(),
           name='myportfolio_experience_list_urlpattern'),

    path('experience/<int:pk>/',
           ExperienceDetail.as_view(),
           name='myportfolio_experience_detail_urlpattern'),

    path('experience/create/',
           ExperienceCreate.as_view(),
           name='myportfolio_experience_create_urlpattern'),

    path('experience/<int:pk>/update/',
           ExperienceUpdate.as_view(),
           name='myportfolio_experience_update_urlpattern'),

    path('experience/<int:pk>/delete/',
           ExperienceDelete.as_view(),
           name='myportfolio_experience_delete_urlpattern'),

    path('project/',
           ProjectList.as_view(),
           name='myportfolio_project_list_urlpattern'),

    path('project/<int:pk>/',
           ProjectDetail.as_view(),
           name='myportfolio_project_detail_urlpattern'),

    path('project/create/',
           ProjectCreate.as_view(),
           name='myportfolio_project_create_urlpattern'),

    path('project/<int:pk>/update/',
           ProjectUpdate.as_view(),
           name='myportfolio_project_update_urlpattern'),

    path('project/<int:pk>/delete/',
           ProjectDelete.as_view(),
           name='myportfolio_project_delete_urlpattern'),

    path('skill/',
           SkillList.as_view(),
           name='myportfolio_skill_list_urlpattern'),

    path('skill/<int:pk>/',
           SkillDetail.as_view(),
           name='myportfolio_skill_detail_urlpattern'),

    path('skill/create/',
           SkillCreate.as_view(),
           name='myportfolio_skill_create_urlpattern'),

    path('skill/<int:pk>/update/',
           SkillUpdate.as_view(),
           name='myportfolio_skill_update_urlpattern'),

    path('skill/<int:pk>/delete/',
           SkillDelete.as_view(),
           name='myportfolio_skill_delete_urlpattern'),
]
