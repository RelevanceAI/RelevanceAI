"""
Base class for operations.
"""
from typing import Any, List, Union, Optional
from relevanceai.client.helpers import (
    Credentials,
    process_token,
)


class BaseOps:
    """
    Base class for operations
    """

    def __init__(self, *args, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    @classmethod
    def init(self, *args, **kwargs):
        return self(*args, **kwargs)

    @classmethod
    def from_credentials(self, credentials: Credentials, *args, **kw):
        return self(credentials=credentials)

    @classmethod
    def from_token(self, token: str, *args, **kw):
        """
        If this is from a token, then we use this
        """
        credentials = process_token(token)
        return self(credentials=credentials, *args, **kw)

    @classmethod
    def from_client(self, client, *args, **kwargs):
        credentials = client.credentials
        return self(
            credentials=credentials,
            *args,
            **kwargs,
        )

    @classmethod
    def from_dataset(
        self,
        dataset,
        alias: Optional[str],
        vector_fields: Optional[List[str]],
        *args,
        **kwargs,
    ):
        credentials = dataset.credentials
        dataset_id = dataset.dataset_id
        return self(
            credentials=credentials,
            dataset_id=dataset_id,
            alias=alias,
            vector_fields=vector_fields,
            *args,
            **kwargs,
        )

    def _get_dataset_id(self, dataset: Union[str, Any]):
        from relevanceai.dataset import Dataset

        if isinstance(dataset, str):
            return dataset
        elif isinstance(dataset, Dataset):
            return dataset.dataset_id
