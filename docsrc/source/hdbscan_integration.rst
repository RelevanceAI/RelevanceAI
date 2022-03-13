.. _hdbscan_integration:


HDBSCAN Integration
============================

Relevance AI integrates nicely with HDBScan thanks to its Scikit-Learn interface! Below are a few examples of such
integrations. It is also relatively easy to build your own!

Clustering Algorithms
-----------------------------

HDBSCAN Example
################

.. code-block::

    import hdbscan
    from relevanceai import Client

    # instantiate the client
    client = Client()

    # Retrieve the relevant dataset
    ds = client.Dataset("sample_dataset_id")

    from relevanceai.datasets import mock_documents
    ds.upsert_documents(mock_documents(100))

    model = hdbscan.HDBSCAN()

    clusterer = client.ClusterOps(alias="hdbscan", model=model)
    clusterer.fit_predict_update(
        ds, vector_fields=["sample_1_vector_"]
    )

    # check that cluster is now in schema
    ds.schema

    # List closest to center
    clusterer.list_closest_to_center()
