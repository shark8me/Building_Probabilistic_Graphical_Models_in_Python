from bayesian.factor_graph import *
from bayesian.bbn import *

dictionary_asia = {'yes': 0.01, 'no': 0.99}

def f_asia(asia):
    return dictionary_asia[asia]

dictionary_tub = {('yes', 'no'): 0.95, ('no', 'no'): 0.99, ('no', 'yes'): 0.01, ('yes', 'yes'): 0.05}
def f_tub(asia, tub):
    return dictionary_tub[(asia, tub)]

dictionary_smoke = {'yes': 0.5, 'no': 0.5}

def f_smoke(smoke):
    return dictionary_smoke[smoke]

dictionary_lung = {('yes', 'no'): 0.9, ('no', 'no'): 0.99, ('no', 'yes'): 0.01, ('yes', 'yes'): 0.1}
def f_lung(smoke, lung):
    return dictionary_lung[(smoke, lung)]

dictionary_bronc = {('yes', 'no'): 0.4, ('no', 'no'): 0.7, ('no', 'yes'): 0.3, ('yes', 'yes'): 0.6}
def f_bronc(smoke, bronc):
    return dictionary_bronc[(smoke, bronc)]

dictionary_either = {('yes', 'yes', 'no'): 0.0, ('no', 'yes', 'yes'): 1.0, ('yes', 'yes', 'yes'): 1.0, ('no', 'no', 'yes'): 0.0, ('yes', 'no', 'no'): 0.0, ('no', 'no', 'no'): 1.0, ('no', 'yes', 'no'): 0.0, ('yes', 'no', 'yes'): 1.0}
def f_either(lung, tub, either):
    return dictionary_either[(lung, tub, either)]

dictionary_xray = {('yes', 'no'): 0.02, ('no', 'no'): 0.95, ('no', 'yes'): 0.05, ('yes', 'yes'): 0.98}
def f_xray(either, xray):
    return dictionary_xray[(either, xray)]

dictionary_dysp = {('yes', 'yes', 'no'): 0.1, ('no', 'yes', 'yes'): 0.7, ('yes', 'yes', 'yes'): 0.9, ('no', 'no', 'yes'): 0.1, ('yes', 'no', 'no'): 0.2, ('no', 'no', 'no'): 0.9, ('no', 'yes', 'no'): 0.3, ('yes', 'no', 'yes'): 0.8}
def f_dysp(bronc, either, dysp):
    return dictionary_dysp[(bronc, either, dysp)]

functions = [f_asia, f_tub, f_smoke, f_lung, f_bronc, f_either, f_xray, f_dysp]
domains_dict = {'dysp': ['yes', 'no'], 'bronc': ['yes', 'no'], 'asia': ['yes', 'no'], 'xray': ['yes', 'no'], 'lung': ['yes', 'no'], 'either': ['yes', 'no'], 'smoke': ['yes', 'no'], 'tub': ['yes', 'no']}

def create_graph():
    g = build_graph(
        *functions,
        domains = domains_dict)
    g.name = 'asia'
    return g

def create_bbn():
    g = build_bbn(
        *functions,
        domains = domains_dict)
    g.name = 'asia'
    return g

