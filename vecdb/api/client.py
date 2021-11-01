# -*- coding: utf-8 -*-
"""API Client
"""
from vecdb.config import CONFIG, Config
from vecdb.api.datasets import Datasets
from vecdb.api.services import Services


class APIClient:
    """API Client"""

    config: Config = CONFIG

    def __init__(self, project: str, api_key: str, base_url: str):
        self.project = project
        self.api_key = api_key
        self.base_url = base_url
        self.datasets = Datasets(project=project, api_key=api_key, base_url=base_url)
        self.services = Services(project=project, api_key=api_key, base_url=base_url)
