from __future__ import unicode_literals
from itertools import chain

from django.db import migrations


def populate_permissions_lists(apps):
    permission_class = apps.get_model('auth', 'Permission')

    person_permissions = permission_class.objects.filter(content_type__app_label='myportfolio',
                                                             content_type__model='person')

    education_permissions = permission_class.objects.filter(content_type__app_label='myportfolio',
                                                          content_type__model='education')

    experience_permissions = permission_class.objects.filter(content_type__app_label='myportfolio',
                                                                  content_type__model='experience')

    project_permissions = permission_class.objects.filter(content_type__app_label='myportfolio',
                                                                  content_type__model='project')

    skill_permissions = permission_class.objects.filter(content_type__app_label='myportfolio',
                                                           content_type__model='skill')

    proficiency_level_permissions = permission_class.objects.filter(content_type__app_label='myportfolio',
                                                         content_type__model='proficiencylevel')

    school_permissions = permission_class.objects.filter(content_type__app_label='myportfolio',
                                                          content_type__model='school')

    perm_view_person = permission_class.objects.filter(content_type__app_label='myportfolio',
                                                           content_type__model='person',
                                                           codename='view_person')

    perm_view_education = permission_class.objects.filter(content_type__app_label='myportfolio',
                                                        content_type__model='education',
                                                        codename='view_education')

    perm_view_experience = permission_class.objects.filter(content_type__app_label='myportfolio',
                                                               content_type__model='experience',
                                                               codename='view_experience')

    perm_view_project = permission_class.objects.filter(content_type__app_label='myportfolio',
                                                               content_type__model='project',
                                                               codename='view_project')

    perm_view_skill = permission_class.objects.filter(content_type__app_label='myportfolio',
                                                         content_type__model='skill',
                                                         codename='view_skill')

    perm_view_proficiency_level = permission_class.objects.filter(content_type__app_label='myportfolio',
                                                       content_type__model='proficiencylevel',
                                                       codename='view_proficiencylevel')

    perm_view_school = permission_class.objects.filter(content_type__app_label='myportfolio',
                                                        content_type__model='school',
                                                        codename='view_school')

    portfolio_user_permissions = chain(perm_view_person,
                                       perm_view_education,
                                       perm_view_experience,
                                       perm_view_project,
                                       perm_view_skill,
                                       perm_view_proficiency_level,
                                       perm_view_school)

    portfolio_clerk_permissions = chain(perm_view_person,
                                        perm_view_education,
                                        perm_view_experience,
                                        perm_view_project,
                                        perm_view_skill,
                                        proficiency_level_permissions,
                                        school_permissions)

    portfolio_operator_permissions = chain(person_permissions,
                                           education_permissions,
                                           experience_permissions,
                                           project_permissions,
                                           skill_permissions,
                                           perm_view_proficiency_level,
                                           perm_view_school)

    my_groups_initialization_list = [
        {
            "name": "portfolio_user",
            "permissions_list": portfolio_user_permissions,
        },
        {
            "name": "portfolio_clerk",
            "permissions_list": portfolio_clerk_permissions,
        },
        {
            "name": "portfolio_operator",
            "permissions_list": portfolio_operator_permissions,
        },
    ]
    return my_groups_initialization_list


def add_group_permissions_data(apps, schema_editor):
    groups_initialization_list = populate_permissions_lists(apps)

    group_model_class = apps.get_model('auth', 'Group')
    for group in groups_initialization_list:
        if group['permissions_list'] is not None:
            group_object = group_model_class.objects.get(
                name=group['name']
            )
            group_object.permissions.set(group['permissions_list'])
            group_object.save()


def remove_group_permissions_data(apps, schema_editor):
    groups_initialization_list = populate_permissions_lists(apps)

    group_model_class = apps.get_model('auth', 'Group')
    for group in groups_initialization_list:
        if group['permissions_list'] is not None:
            group_object = group_model_class.objects.get(
                name=group['name']
            )
            list_of_permissions = group['permissions_list']
            for permission in list_of_permissions:
                group_object.permissions.remove(permission)
                group_object.save()


class Migration(migrations.Migration):
    dependencies = [
        ('myportfolio', '0014_create_groups'),
    ]

    operations = [
        migrations.RunPython(
            add_group_permissions_data,
            remove_group_permissions_data
        )
    ]
