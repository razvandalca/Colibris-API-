from rest_framework.routers import SimpleRouter as BaseSimpleRouter


class SimpleRouter(BaseSimpleRouter):
    def extends(self, other: BaseSimpleRouter):
        self.registry.extend(other.registry)
