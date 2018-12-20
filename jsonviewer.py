from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import json
import numpy as np
import os



roottype = [int, float, complex, long, str, unicode]
treetype = [tuple, list]


def print_tabs(times):
    for i in range(times):
        print("\t", end="")
        
def inner_view_json(data, depth):
#    print(depth)
    t = type(data)
    if t in roottype:
        print_tabs(depth)
        print("data: " + str(data))
    elif t in treetype:
        print_tabs(depth)
        print(str(t) + "len=" + str(len(data)))
        inner_view_json(data[0], depth + 1)
    elif t is dict:
        print_tabs(depth)
        print(str(t) +  "len=" + str(len(data.keys())))
        for key in data:
            print_tabs(depth+1)
            print("key=" + key)
            inner_view_json(data[key], depth + 2)
    else:
        raise ValueError("not support type", t)
        
        
def read_json(fname):
    with open(fname) as f:
        data = json.load(f)
    return data

def view_json(fname):
    data = read_json(fname)
    inner_view_json(data, 0)
