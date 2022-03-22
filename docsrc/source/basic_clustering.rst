Basic Clustering
================

Auto clustering is the easiest way to cluster.

.. code-block::

    from relevanceai import Client
    client = Client()
    dataset_id = "sample_dataset_id"
    ds = client.Dataset(dataset_id)

    # Modelling with Sklearn
    from sklearn.cluster import KMeans
    cluster_model = KMeans()
    cluster_ops = ds.auto_cluster(
        alias="kmeans", # this will be used to re-instantiate the model
                        # we encourage naming it something useful!
        vector_fields=[vector_field], # vector fields
        model=KMeans() # sklearn model you want to use
    )
    cluster_ops.list_closest_to_center()

    # Run mini-batch K means clustering with 8 clusters
    from sklearn.cluster import MiniBatchKMeans
    cluster_model = MiniBatchKMeans()

    cluster_ops = ds.auto_cluster(
        "minibatchkmeans_8",
        vector_fields=[vector_field],
        model=cluster_model
    )

    # Automated modelling
    # If you want to run KMeans with 8 clusters automatically
    cluster_ops = ds.auto_cluster(
        "kmeans_8",
        vector_fields=[vector_field]
    )

    # Run minibatch k means clustering with 8 clusters
    cluster_ops = ds.auto_cluster(
        "minibatchkmeans_8", vector_fields=[vector_field]
    )

    # Run minibatch k means clustering with 20 clusters
    cluster_ops = ds.auto_cluster(
        "minibatchkmeans_20",
        vector_fields=[vector_field]
    )

You can read more about how to cluster using the `auto_cluster` below!

.. automethod:: relevanceai.dataset_ops.dataset_operations.Operations.auto_cluster

For more advanced clustering methods and to use your own custom clustering
method, read the other sections under `ClusterOps`.
