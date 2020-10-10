# -*- coding: utf-8 -*-
from django import template

register = template.Library()


@register.filter
def split1(value):
    ls = value.split(',')
    return ls[0]

@register.filter
def split2(value):
    ls = value.split('|')
    return ls[1]

@register.filter
def split3(value):
    ls = value.split('|')
    return ls[2]