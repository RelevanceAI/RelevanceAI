Cluster
---------

Basic
---------

The easiest way to cluster a dataset is to use the `cluster` method from a `Dataset` object (an example is shown below).

.. code-block::

    from relevanceai import Client
    client= Client()

    from relevanceai import mock_documents
    docs = mock_documents()
    ds = client.Dataset("sample")
    ds.upsert_documents(docs)

    cluster_ops = ds.cluster(
        vector_fields=["sample_1_vector_"],
        model="kmeans"
    )

Native Scikit-learn Integration
---------------------------------

You can easily cluster with the model if your cluster model has a `fit_predict` method.

.. code-block::

    from sklearn.cluster import KMeans
    model = KMeans(n_clusters=100)
    cluster_ops = ds.cluster(
        vector_fields=["sample_1_vector_"],
        model=model.
        alias="native-sklearn" # alias is anything you want
    )


Once clustered, you can access all of the useful Scikit-learn integrations.

.. code-block::

    # List the closest to each centroid in a cluster
    cluster_ops.list_closest()

    # Launch a cluster app
    ds.launch_cluster_app()

Reloading ClusterOps
------------------------

Often you may have clustered but want to just re-load
your clusterops object without having to re-fit the model.
You can do that in 2 ways.

.. code-block::

    # State the vector fields and alias in the ClusterOps object
    ds = client.Dataset("sample_dataset_id")
    cluster_ops = ds.ClusterOps(
        alias="kmeans-16",
        vector_fields=['sample_vector_'])
    )

    cluster_ops.list_closest()

    # State the vector fields and alias in the operational call
    cluster_ops = client.ClusterOps(alias="kmeans-16")
    cluster_ops.list_closest(dataset="sample_dataset_id",
        vector_fields=["documentation_vector_])

API Reference
----------------

.. automodule:: relevanceai.operations.cluster.cluster
   :members:
   :exclude-members: __init__

.. automethod:: relevanceai.operations.cluster.cluster.ClusterOps.aggregate

.. automethod:: relevanceai.operations.cluster.cluster.Clusterops.run

.. automethod:: relevanceai.operations.cluster.cluster.ClusterOps.list_closest

.. automethod:: relevanceai.operations.cluster.cluster.ClusterOps.list_furthest

.. automethod:: relevanceai.operations.cluster.cluster.ClusterOps.centroids

.. automethod:: relevanceai.operations.cluster.cluster.ClusterOps.insert_centroids

.. automethod:: relevanceai.operations.cluster.cluster.ClusterOps.create_centroids

.. automethod:: relevanceai.operations.cluster.cluster.ClusterOps.merge
