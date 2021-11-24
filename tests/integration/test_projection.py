#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#####
# Author: Charlene Leong charleneleong84@gmail.com
# Created Date: Monday, November 8th 2021, 8:15:18 pm
# Last Modified: Wednesday, November 17th 2021,8:53:50 am
#####

from pathlib import Path
import ivis
import pytest
import json
import uuid
from pprint import pprint
import typing
from typing_extensions import get_args

from relevanceai.visualise.constants import DIM_REDUCTION, DIM_REDUCTION_DEFAULT_ARGS
from relevanceai.visualise.constants import CLUSTER, CLUSTER_DEFAULT_ARGS


@pytest.fixture(name='base_args')
def fixture_base_args():
    project = "dummy-collections"
    api_key = "UzdYRktIY0JxNmlvb1NpOFNsenU6VGdTU0s4UjhUR0NsaDdnQTVwUkpKZw"  # Read access
    base_url = "https://api-aueast.relevance.ai/v1"
    base_args = {
                "project": project, 
                "api_key": api_key, 
                "base_url": base_url,
            }
    return base_args

# @pytest.fixture
# def sample_doc():
#     return [{
#         "_id": uuid.uuid4().__str__(),
#         "value": random.randint(0, 1000),
#     }]


# @pytest.fixture(name='test-dataset-1')
# def fixture_test_dataset_1():
#     test_dataset_1 = json.load(open("../tests/data/_ecommerce-6.json"))
    

@pytest.fixture(name='dataset_args', 
params =[ 
        { 
        "dataset_id" : "test-dataset",
        "vector_field": "product_name_imagetext_vector_",
        "number_of_points_to_render" : 100,
        "random_state" : 0,
        "vector_label" : "product_name",
        "vector_label_char_length"  : 12,
        "hover_label": ["category"],
        },
        {  ## Testing colour label
            "vector_field": "sample_2_vector_",
            "colour_label": "sample_2_label",
            "colour_label_char_length": 20,
            "number_of_points_to_render": 100,
            "random_state": 42,
        },
        {  ## Testing vector label, colour label and hover label
            "vector_field": "sample_3_vector_",
            "colour_label": "sample_3_label",
            "colour_label_char_length": 20,
            "hover_label": ["sample_1_label", "sample_2_label", "sample_3_label"],
            "number_of_points_to_render": None,
            "random_state": 42,
        },
    ],
)
def fixture_dataset_args(request):
    return request.param


@pytest.fixture(
    name="dr_args",
    params=[
        {"dr": dr, "dr_args": {**DIM_REDUCTION_DEFAULT_ARGS[dr]}}
        for dr in get_args(DIM_REDUCTION)
    ],
)
def fixture_dr_args(request):
    return request.param


@pytest.fixture(
    name="cluster_args",
    params=[
        {"cluster": c, "cluster_args": {**CLUSTER_DEFAULT_ARGS[c]}}
        for c in get_args(CLUSTER)
        if c
    ],
)
def fixture_cluster_args(request):
    return request.param


def test_projector_plot(test_client, dataset_args, dr_args, cluster_args):
    """Testing vector label with cluster"""
    test_client.projector.plot(**dataset_args, **dr_args, **cluster_args)
    assert True
