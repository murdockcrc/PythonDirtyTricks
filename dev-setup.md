# Dev setup

This is a list of installations which are required. Most of the dependencies are managed as `pip` or `conda` packages, so make sure you check the `environment.yml` too for more. This page also contains some commands with convenient tools.

# Monitoring GPU utilization

```
watch -n 5 nvidia-smi -a --display=utilization
```

# BLAS

Optimize running Tensor operations in your CPU

```
sudo apt-get install build-essential cmake unzip pkg-config libopenblas-dev liblapack-dev
```
