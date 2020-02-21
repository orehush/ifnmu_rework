from rest_framework.routers import DefaultRouter

from apps.faculty.api.views import FacultyViewSet, CourseViewSet

router = DefaultRouter(trailing_slash='/')
router.register('faculties', FacultyViewSet)
router.register('courses', CourseViewSet)

urlpatterns = router.urls
