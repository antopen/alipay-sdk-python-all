#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DeviceParams(object):

    def __init__(self):
        self._out_device_id = None
        self._device_name = None
        self._device_type = None

    @property
    def out_device_id(self):
        return self._out_device_id

    @out_device_id.setter
    def out_device_id(self, value):
        self._out_device_id = value
    @property
    def device_name(self):
        return self._device_name

    @device_name.setter
    def device_name(self, value):
        self._device_name = value
    @property
    def device_type(self):
        return self._device_type

    @device_type.setter
    def device_type(self, value):
        self._device_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_device_id:
            if hasattr(self.out_device_id, 'to_alipay_dict'):
                params['out_device_id'] = self.out_device_id.to_alipay_dict()
            else:
                params['out_device_id'] = self.out_device_id
        if self.device_name:
            if hasattr(self.device_name, 'to_alipay_dict'):
                params['device_name'] = self.device_name.to_alipay_dict()
            else:
                params['device_name'] = self.device_name
        if self.device_type:
            if hasattr(self.device_type, 'to_alipay_dict'):
                params['device_type'] = self.device_type.to_alipay_dict()
            else:
                params['device_type'] = self.device_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeviceParams()
        if 'out_device_id' in d:
            o.out_device_id = d['out_device_id']
        if 'device_name' in d:
            o.device_name = d['device_name']
        if 'device_type' in d:
            o.device_type = d['device_type']
        return o


