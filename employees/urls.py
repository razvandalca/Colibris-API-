from colibris.core.routers import SimpleRouter
from employees.views import EmployeeViewSet


router = SimpleRouter()

router.register("employees", EmployeeViewSet, basename="employees")
