Cluster
---------

Basic
---------

The easiest way to cluster is to run the following.

.. automethod:: relevanceai.operations.operations.Operations.cluster

Custom Cluster Models
-------------------------

The ClusterBase class is intended to be inherited so that users can add their own clustering algorithms
and models. A cluster base has the following abstractmethods (methods to be overwritten):

- :code:`fit_transform`
- :code:`metadata` (optional if you want to store cluster metadata)
- :code:`get_centers` (optional if you want to store cluster centroid documents)

:code:`CentroidBase` is the most basic class to inherit. Use this class if you have an
in-memory fitting algorithm.

If your clusters return centroids, you will want to inherit
:code:`CentroidClusterBase`.

If your clusters can fit on batches, you will want to inherit
:code:`BatchClusterBase`.

If you have both Batches and Centroids, you will want to inherit both.

.. code-block::

    import numpy as np
    from faiss import Kmeans
    from relevanceai import Client, CentroidClusterBase

    client = Client()
    df = client.Dataset("_github_repo_vectorai")

    class FaissKMeans(CentroidClusterBase):
        def __init__(self, model):
            self.model = model

        def fit_predict(self, vectors):
            vectors = np.array(vectors).astype("float32")
            self.model.train(vectors)
            cluster_labels = self.model.assign(vectors)[1]
            return cluster_labels

        def metadata(self):
            return self.model.__dict__

        def get_centers(self):
            return self.model.centroids

    n_clusters = 10
    d = 512
    alias = f"faiss-kmeans-{n_clusters}"
    vector_fields = ["documentation_vector_"]

    model = FaissKMeans(model=Kmeans(d=d, k=n_clusters))
    clusterer = client.ClusterOps(model=model, alias=alias)
    clusterer.fit_predict_update(dataset=df, vector_fields=vector_fields)

.. automodule:: relevanceai.workflows.cluster_ops.clusterbase
   :members:

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
