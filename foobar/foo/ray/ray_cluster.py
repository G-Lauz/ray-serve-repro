import ray

class RayCluster():
    def __init__(self) -> None:
        if not ray.is_initialized():
            ray.init(address="ray://10.0.0.123:10001", namespace="serve")