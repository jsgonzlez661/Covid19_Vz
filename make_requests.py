#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2020 Jose Gonzalez ~ All rights reserved. MIT license.

import requests


class DataGET():

    @classmethod
    def get_summary(cls):  # jsgonzlez661: Extract informations Covid-19 in Venezuela
        contents = requests.get(
            'https://covid19.patria.org.ve/api/v1/summary').json()
        summary = contents
        return summary

    @classmethod
    def make_graph(cls, type_graph, title, datas):  # jsgonzlez661: Make graph function
        labels = []
        values = []
        for data in datas:
            labels.append(data)
            values.append(datas[data])
        # jsgonzlez661: Make json for post
        config = {
            "chart": {
                "type": type_graph,
                "format": "png",
                "data": {
                    "labels": labels,
                    "datasets": [
                        {
                            "label": title,
                            "data": values
                        }
                    ]
                }
            }
        }
        contents = requests.post(url='https://quickchart.io/chart/create',
                                 json=config).json()
        img_url = contents['url']  # jsgonzlez661: Extrar url
        return img_url


# summary = DataGET.get_summary()  # jsgonzlez661: Recopiled Information

# # jsgonzlez661: Numbers case confirmed
# case_confirmed = str(summary['Confirmed']['Count'])

# # jsgonzlez661: Numbers case recovered
# case_recovered = str(summary['Recovered']['Count'])

# # jsgonzlez661: Numbers case deaths
# case_deaths = str(summary['Deaths']['Count'])

# # jsgonzlez661: Numbers case for men
# distribuid_male = summary['Confirmed']['ByGender'][
#     'male']

# # jsgonzlez661: Numbers case for woman
# distribuid_female = summary['Confirmed']['ByGender'][
#     'female']

# bygender = summary['Confirmed']['ByGender']

# # jsgonzlez661: Numbers case for age
# byagerange = summary['Confirmed']['ByAgeRange']

# # jsgonzlez661: Numbers case for state
# bystate = summary['Confirmed']['ByState']
