from math import degrees, atan
from statistics import mean

SVO_TYPE_CLASSIFICATION_DICT = {
    'altruistic': [57.15, 90],
    'prosocial': [22.45, 57.15],
    'individualistic': [-12.04, 22.45],
    'competitive': [-90, -12.04]
}


def calcu_SVO_type(self_allocations, other_allocations):
    '''
    self_allocations -> list: list contains coins allocated to self
    other_allocations -> list: list contains coins allocated to the other
    '''
    As_mean = mean(self_allocations)
    Ao_mean = mean(other_allocations)

    SVO_degree = degrees(atan( (Ao_mean - 50) / (As_mean - 50) ))

    for k, v in SVO_TYPE_CLASSIFICATION_DICT.items():
        if v[0] < SVO_degree <= v[1]:
            return k

    return 'range error'

def calcu_SVO_degree(self_allocations, other_allocations):
    '''
    self_allocations -> list: list contains coins allocated to self
    other_allocations -> list: list contains coins allocated to the other
    '''
    As_mean = mean(self_allocations)
    Ao_mean = mean(other_allocations)

    SVO_degree = degrees(atan( (Ao_mean - 50) / (As_mean - 50) ))

    return SVO_degree

def get_SVO_type(svo_degree):
    '''
    svo_degree -> float: a number indicates SVO degree
    '''
    for k, v in SVO_TYPE_CLASSIFICATION_DICT.items():
        if v[0] < svo_degree <= v[1]:
            return k

    return 'range error'








