from ray import serve
from foobar.bar import AbstractDeployment
from foobar.foo import Cluster

@serve.deployment
class Counter():
    def __init__(self) -> None:
        self.count = 0

    async def __call__(self, request):
        data = await request.body()
        print(data)
        self.count += 1
        return {"count": self.count}

class CounterInherit(AbstractDeployment):

    def __init__(self) -> None:
        super().__init__()
        self.count = 0

    def process(self, data):
        print(data)
        self.count += 1
        return {"count": self.count}

if __name__ == "__main__":
    ray_cluster = Cluster()
    ray_cluster.deploy(deployment=Counter) # No Error
    ray_cluster.deploy(deployment=CounterInherit) # Error