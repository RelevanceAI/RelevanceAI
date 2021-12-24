"""Testing code for batch inserting
"""
import numpy as np
import random
import pytest


class TestInsert:
    """Testing the insert functionalities"""

    def test_batch_insert(self, simple_doc, test_dataset_id, test_client):
        """Batch insert"""
        simple_documents = simple_doc * 100
        results = test_client.insert_documents(test_dataset_id, simple_documents)
        assert len(results["failed_documents"]) == 0


# Mock a callable For pull update push
def do_nothing(documents):
    return documents


def cause_error(documents):
    for d in documents:
        d["value"] = np.nan
    return documents


def cause_some_error(documents):
    MAX_ERRORS = 5
    ERROR_COUNT = 0
    for d in documents:
        if ERROR_COUNT < MAX_ERRORS:
            d["value"] = np.nan
            ERROR_COUNT += 1
    return documents


class TestPullUpdatePush:
    """Testing Pull Update Push"""

    def test_pull_update_push_simple(self, test_client, test_sample_dataset):
        """Simple test for pull update push"""
        results = test_client.pull_update_push(test_sample_dataset, do_nothing)
        assert len(results["failed_documents"]) == 0

    def test_pull_update_push_with_errors(self, test_client, test_sample_dataset):
        """Simple test for pull update push with an errored update function"""
        with pytest.raises(Exception) as execinfo:
            results = test_client.pull_update_push(test_sample_dataset, cause_error)

    def test_with_some_errors(self, test_client, test_sample_dataset):
        """Test with some errors"""
        import requests

        with pytest.raises(requests.exceptions.InvalidJSONError) as execinfo:
            results = test_client.pull_update_push(
                test_sample_dataset, cause_some_error
            )

    @pytest.mark.slow
    def test_pull_update_push_loaded(self, test_sample_dataset, test_client):
        """Stress testing pull update push."""

        def do_nothing(documents):
            return documents

        response = test_client.pull_update_push(test_sample_dataset, do_nothing)
        assert len(response["failed_documents"]) == 0, "Failed to insert documents"


# class TestCleanUp:
#     def test_clean_up(self, test_client, test_dataset_id):
#         assert test_client.datasets.delete(test_dataset_id)
