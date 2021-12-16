# ray-serve-repro
This is to reproduce the issue discussed here: https://github.com/ray-project/ray/issues/21095

**Python version:** 3.8.10

**Ray version:** 1.9

### Steps:
```bash
git clone https://github.com/G-Lauz/ray-serve-repro.git
ray start --head
cd ray-serve-repro.git
python deploy.py
```
After running deploy.py, expecting below error logs:
```bash
Traceback (most recent call last):
  File "deploy.py", line 17, in <module>
    ray_cluster.deploy(deployment=Counter)
  File "/home/glauz/projects/ray-serve-repro/foobar/foo/cluster.py", line 14, in deploy
    deployment.create_deployment().options(name="count", **config).deploy()
  File "/home/glauz/projects/ray-serve-repro/.venv/lib/python3.8/site-packages/ray/serve/api.py", line 789, in deploy
    return _get_global_client().deploy(
  File "/home/glauz/projects/ray-serve-repro/.venv/lib/python3.8/site-packages/ray/serve/api.py", line 93, in check
    return f(self, *args, **kwargs)
  File "/home/glauz/projects/ray-serve-repro/.venv/lib/python3.8/site-packages/ray/serve/api.py", line 248, in deploy
    self._wait_for_goal(goal_id)
  File "/home/glauz/projects/ray-serve-repro/.venv/lib/python3.8/site-packages/ray/serve/api.py", line 184, in _wait_for_goal
    raise async_goal_exception
RuntimeError: Deployment 'count' failed, deleting it asynchronously.
```
When we looked at ray's log, we can find:
```bash
ray.exceptions.RayActorError: The actor died because of an error raised in its creation task, ray::SERVE_REPLICA::count#cBeVKd:RayServeWrappedReplica.__init__ (pid=612354, ip=10.0.0.123)
  File "/usr/lib/python3.8/concurrent/futures/_base.py", line 437, in result
    return self.__get_result()
  File "/usr/lib/python3.8/concurrent/futures/_base.py", line 389, in __get_result
    raise self._exception
  File "/home/glauz/projects/ray-serve-repro/.venv/lib/python3.8/site-packages/ray/serve/replica.py", line 48, in __init__
    deployment_def = cloudpickle.loads(serialized_deployment_def)
ModuleNotFoundError: No module named 'foobar'
```