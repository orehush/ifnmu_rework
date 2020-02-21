from rest_framework.routers import DefaultRouter

from apps.subject.api.views import SubjectViewSet

router = DefaultRouter(trailing_slash='/')
router.register('subjects', SubjectViewSet)

urlpatterns = router.urls
