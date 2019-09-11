from rest_framework import routers
from app.viewsets import EquationsViewSet

router = routers.SimpleRouter()
router.register('equations', EquationsViewSet)

urlpatterns = router.urls
