from relevanceai.interfaces import Dataset


def test_dataset_vectorize(test_dataset: Dataset):
    results = test_dataset.vectorize(image_fields=["image_url"], text_fields=["data"])
    # This means the results are good yay!
    assert "image_url_clip_vector_" in test_dataset.schema
    assert "data_use_vector_" in test_dataset.schema

    results = test_dataset.vectorize(image_fields=["image_url"])
    assert "image_url_clip_vector_" in results["skipped_vectors"]


def test_dataset_auto_text_cluster_dashboard(test_dataset: Dataset):
    alias = "kmeans_3"
    test_dataset.auto_text_cluster_dashboard(text_fields=["data"], alias=alias)

    vector = "data_use_vector_"
    assert vector in test_dataset.schema
    assert ".".join(["_cluster_", vector, alias]) in test_dataset.schema
