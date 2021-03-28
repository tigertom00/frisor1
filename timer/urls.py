from rest_framework import routers
from .views import TimerViewSet

router = routers.DefaultRouter()
router.register('api/timer', TimerViewSet, 'timer')

urlpatterns = router.urls
