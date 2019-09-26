#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserCertifyOpenQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserCertifyOpenQueryResponse, self).__init__()
        self._identity_info = None
        self._material_info = None
        self._passed = None

    @property
    def identity_info(self):
        return self._identity_info

    @identity_info.setter
    def identity_info(self, value):
        self._identity_info = value
    @property
    def material_info(self):
        return self._material_info

    @material_info.setter
    def material_info(self, value):
        self._material_info = value
    @property
    def passed(self):
        return self._passed

    @passed.setter
    def passed(self, value):
        self._passed = list()
        if isinstance(value, list):
            for i in value:
                self._passed.append(i)
        elif isinstance(value, str):
            self._passed.append(value)

    def parse_response_content(self, response_content):
        response = super(AlipayUserCertifyOpenQueryResponse, self).parse_response_content(response_content)
        if 'identity_info' in response:
            self.identity_info = response['identity_info']
        if 'material_info' in response:
            self.material_info = response['material_info']
        if 'passed' in response:
            self.passed = response['passed']
