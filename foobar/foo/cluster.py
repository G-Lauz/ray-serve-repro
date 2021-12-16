from ray import serve

from foobar.bar.abstract_deployment import AbstractDeployment

from .ray import RayCluster

class Cluster():
    def __init__(self) -> None:
        self.ray_cluster = RayCluster()

    def deploy(self, deployment:AbstractDeployment):
        config = {}
        serve.start(detached=True, http_options={"host":"0.0.0.0"})
        deployment.create_deployment().options(name="count", **config).deploy()