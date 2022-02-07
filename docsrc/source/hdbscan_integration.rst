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
    df = client.Dataset("sample_dataset")

    model = hdbscan.HDBSCAN()

    clusterer = client.ClusterOps(model, alias="hdbscan")
    clusterer.fit_predict_update(df, vector_fields=["sample_vector_"])

    # check that cluster is now in schema
    df.schema

    # List closest to center 
    clusterer.list_closest_to_center()
