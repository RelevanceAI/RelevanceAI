from relevanceai.datasets import mock_documents
from relevanceai.http_client import Client


def test_dataset_vectorize(test_client: Client):
    dataset_id = "vectorhub-test"
    ds = test_client.Dataset("vectorhub-test")
    ds.insert_documents(mock_documents(number_of_documents=10))
    results = ds.vectorize(text_fields=["sample_1_description"])
    assert len(results["text"]["failed_documents"]) == 0
    ds.delete()
