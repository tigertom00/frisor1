from rest_framework import routers
from .views import TimerViewSet

router = routers.DefaultRouter()
router.register('', TimerViewSet, 'timer')

urlpatterns = router.urls
