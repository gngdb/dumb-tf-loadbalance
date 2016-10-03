
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

FAQ
===

> I am an employer, and think that I wouldn't want to hire someone who would
> write something as stupid as this?

Might I remind you that [laziness is a virtue][virtue] and I've just thrown
this together in a spare half an hour. And I haven't maintained it _at all_.

Seriously though, in simple scripts for experiments this saves enough time in
setting the `CUDA_VISIBLE_DEVICES` environment variable that it was worth
writing.

[virtue]: http://c2.com/cgi/wiki?LazinessImpatienceHubris
