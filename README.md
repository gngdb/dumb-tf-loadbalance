
The dumbest load balancer for Tensorflow you can imagine. All it does is looks at the devices you have available, and then picks the one with the largest percentage of available memory. Uses `CUDA_VISIBLE_DEVICES` to mask all other devices when Tensorflow runs.

Installation
============

Just clone this repository and then, either:

```
python setup.py install
```

Or, with pip:

```
pip install .
```

Usage
=====

__Before importing tensorflow__:

```
import dumb_tf_loadbalance
dumb_tf_loadbalance.choose_gpu()
```
