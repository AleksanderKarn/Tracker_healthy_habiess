from rest_framework import routers

from habit.views import HabitViewSet

router = routers.SimpleRouter()
router.register('api/habit', HabitViewSet, 'habit')

urlpatterns = router.urls

