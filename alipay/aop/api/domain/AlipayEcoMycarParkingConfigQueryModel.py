#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoMycarParkingConfigQueryModel(object):

    def __init__(self):
        self._interface_name = None
        self._interface_type = None

    @property
    def interface_name(self):
        return self._interface_name

    @interface_name.setter
    def interface_name(self, value):
        self._interface_name = value
    @property
    def interface_type(self):
        return self._interface_type

    @interface_type.setter
    def interface_type(self, value):
        self._interface_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.interface_name:
            if hasattr(self.interface_name, 'to_alipay_dict'):
                params['interface_name'] = self.interface_name.to_alipay_dict()
            else:
                params['interface_name'] = self.interface_name
        if self.interface_type:
            if hasattr(self.interface_type, 'to_alipay_dict'):
                params['interface_type'] = self.interface_type.to_alipay_dict()
            else:
                params['interface_type'] = self.interface_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoMycarParkingConfigQueryModel()
        if 'interface_name' in d:
            o.interface_name = d['interface_name']
        if 'interface_type' in d:
            o.interface_type = d['interface_type']
        return o


