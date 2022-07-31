from django.urls import path, include
from rest_framework.routers import DefaultRouter

from backend.views import ClientViewset, NewsletterViewset, MessageViewset

router = DefaultRouter()
router.register('ClientViewset', ClientViewset)
router.register('NewsletterViewset', NewsletterViewset)
router.register('MessageViewset', MessageViewset)

app_name = 'backend'
urlpatterns = router.urls