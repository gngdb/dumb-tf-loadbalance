#!/usr/bin/python

import os
from pynvml import *

def choose_gpu():
    nvmlInit()
    n_gpus = nvmlDeviceGetCount()
    gpu_memusage = []
    mostfree_index = 0
    for gpu_index in range(n_gpus):
        device_handle = nvmlDeviceGetHandleByIndex(gpu_index)
        meminfo = nvmlDeviceGetMemoryInfo(device_handle)
        gpu_memusage.append(float(meminfo.used)/float(meminfo.total))
        if gpu_memusage[-1] < gpu_memusage[mostfree_index]:
            mostfree_index = gpu_index
    os.environ['CUDA_VISIBLE_DEVICES'] = str(gpu_index)
    nvmlShutdown()
    return None
