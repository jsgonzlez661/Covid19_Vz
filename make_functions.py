#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2020 Jose Gonzalez ~ All rights reserved. MIT license.

import unidecode


def find_state_data(datas, find):  # jsgonzlez661: Find number case in state
    value = 0
    for data in datas:
        unicode_data = unidecode.unidecode(data).replace(' ', '').lower()
        if unicode_data == find.replace('/', ''):
            value = datas[data]
    return value


def list_states(datas):  # jsgonzlez661: Convert name states
    unicode_states = []
    for data in datas:
        unicode_data = unidecode.unidecode(data).replace(' ', '').lower()
        unicode_states.append(unicode_data)
    return unicode_states
