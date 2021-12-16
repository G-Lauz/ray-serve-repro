from foobar.bar import AbstractDeployment
from foobar.foo import Cluster

class Counter(AbstractDeployment):

    def __init__(self) -> None:
        super().__init__()
        self.count = 0
    
    def process(self, data):
        print(data)
        self.count += 1
        return {"count": self.count}

if __name__ == "__main__":
    ray_cluster = Cluster()
    ray_cluster.deploy(deployment=Counter)