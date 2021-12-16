import abc
from ray import serve

class AbstractDeployment(abc.ABC):
    async def __call__(self, request):
        data = await request.body()
        return self.process(data)

    @classmethod
    def create_deployment(cls):
        return serve.deployment(cls)

    @abc.abstractmethod
    def process(self, data):
        """ Process the request
        """