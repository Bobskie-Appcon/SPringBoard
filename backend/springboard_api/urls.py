from django.urls import path
from .controllers.StudentController import RegisterStudent, LoginStudent, LogoutStudent, StudentView, UpdateGroupFK
from .controllers.TeacherController import RegisterTeacher, LoginTeacher, LogoutTeacher, TeacherView, GetTeacherById
from .controllers.AdminController import RegisterAdmin, LoginAdmin, AdminView, LogoutAdmin
from .controllers.GroupController import CreateGroup, GetGroupById, GetGroupsAndProjects, GetGroupByClassId, UpdateGroup
from .controllers.ClassroomController import CreateClassroom, GetAllClassrooms, GetClassroomGroupsAndProjects, GetClassroom, GetClassroomById,  GetTopProjectsByClassroom
from .controllers.ProjectController import ProjectCreateView, ProjectView, GetProjectsByGroupId, GetActiveProjectsView, GetProjectById, GetPublicProjectsByGroupId, InactiveProjectsView, ProjectCreateView, ProjectUpdateView, UpdateProjectStatusView, UpdateProjectScoreView, DeleteProjectView

urlpatterns = [
    path('api/register-student', RegisterStudent.as_view()),
    path('api/login-student', LoginStudent.as_view()),
    path('api/active-student', StudentView.as_view()),
    path('api/logout-student', LogoutStudent.as_view()),

    path('api/register-teacher', RegisterTeacher.as_view()),
    path('api/login-teacher', LoginTeacher.as_view()),
    path('api/active-teacher', TeacherView.as_view()),
    path('api/logout-teacher', LogoutTeacher.as_view()),

    path('api/register-admin', RegisterAdmin.as_view()),
    path('api/login-admin', LoginAdmin.as_view()),
    path('api/active-admin', AdminView.as_view()),
    path('api/logout-admin', LogoutAdmin.as_view()),

    path('api/group/<int:group_id>/projects', GetProjectsByGroupId.as_view()),
    path('api/group/create', CreateGroup.as_view()),
    path('api/group/<int:group_id>', GetGroupById.as_view()),
    path('api/group/group_proj', GetGroupsAndProjects.as_view()),
    path('api/update-group-fk/<int:user_id>', UpdateGroupFK.as_view()),
    path('api/group/<int:group_id>/update', UpdateGroup.as_view()),

    path('api/group/<int:group_id>/projects', GetProjectsByGroupId.as_view()),
    path('api/group/<int:group_id>/public-projects',
         GetPublicProjectsByGroupId.as_view()),
    path('api/project', ProjectView.as_view()),
    path('api/project/<int:project_id>', GetProjectById.as_view()),
    path('api/project/public', GetActiveProjectsView.as_view()),
    path('api/project/create', ProjectCreateView.as_view()),
    path('api/project/<int:project_id>/update', ProjectUpdateView.as_view()),
    path('api/project/<int:project_id>/update_score',
         UpdateProjectScoreView.as_view()),
    path('api/project/<int:project_id>/update_status',
         UpdateProjectStatusView.as_view()),
    path('api/project/<int:project_id>/delete', DeleteProjectView.as_view()),

    path('api/inactive_proj', InactiveProjectsView.as_view()),

    path('api/classroom/create', CreateClassroom.as_view()),
    path('api/classroom/all', GetAllClassrooms.as_view()),
    path('api/classroom/<int:teacher_fk_id>/all', GetClassroom.as_view()),
    path('api/classroom/<int:class_id>', GetClassroomById.as_view()),
    path('api/classroom/<int:class_id>/group', GetGroupByClassId.as_view()),
    path('api/classroom/<int:class_id>/class_group_proj',
         GetClassroomGroupsAndProjects.as_view()),
    path('api/classroom/<int:classroom_id>/groupproject',
         GetTopProjectsByClassroom.as_view()),


]
