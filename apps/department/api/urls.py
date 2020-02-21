from rest_framework.routers import DefaultRouter

from apps.department.api.views import DepartmentViewSet

router = DefaultRouter(trailing_slash='/')
router.register('departments', DepartmentViewSet)

urlpatterns = router.urls
