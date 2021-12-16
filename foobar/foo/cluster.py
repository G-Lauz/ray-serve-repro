from ray import serve

from .ray import RayCluster

class Cluster():
    def __init__(self) -> None:
        self.ray_cluster = RayCluster()

    def deploy(self, deployment):
        config = {}
        serve.start(detached=True, http_options={"host":"0.0.0.0"})

        if isinstance(deployment, serve.api.Deployment):
            deployment.options(name="count", **config).deploy()
        else:
            deployment.create_deployment().options(name="count", **config).deploy()