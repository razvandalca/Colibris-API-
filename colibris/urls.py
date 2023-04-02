from django.urls import re_path, include

from colibris.core.routers import SimpleRouter
from employees.urls import router as employees_router

router = SimpleRouter(trailing_slash=False)
router.extends(employees_router)

urlpatterns = [
    re_path("api/", include(router.urls)),
]
