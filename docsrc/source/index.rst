.. Relevance AI documentation master file, created by
   sphinx-quickstart on Mon Nov  8 16:54:12 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Relevance AI's documentation!
========================================

In the vector workflow to solve search and relevance problems, we decided to focus heavily on the foundation of all good solutions - the experimentation stage. Our experimentation-first approach help users experiment, tune and prototype various vector weightings, configurations, data structures and vector search methods to improve their vectors. For a more in-depth exploration and comparison take a look at our article on experimentation-first vector database.

You own any data you upload to Relevance AI.

Everything you upload to Relevance AI is yours, including any vectors, code, configuration, metadata, output metrics, search results, visualisations and model weights. You can choose to log, export, publish, or delete any of these. We collect aggregate statistics across our users to improve our product— we might do a database query to count how many users have used a specific endpoint to help decide if we want to improve our support for that endpoint. We treat your private data, source code, or trade secrets as confidential and private, as consistent with our Terms of Service and Privacy Policy.‌



.. toctree::
   :maxdepth: 4
   :caption: Core

   client
   dataset

.. toctree::
   :maxdepth: 4
   :caption: Clustering

   auto_clustering
   clusterer
   cluster_base
   reloading_clusterers
   relevanceai.report.cluster
   subclustering

.. toctree::
   :maxdepth: 4
   :caption: Dimensionality Reduction

   auto_reduce_dimensions
   relevanceai.dim_reduction_ops.rst

.. toctree::
   :maxdepth: 4
   :caption: Integrations

   sklearn_clustering_integration
   faiss_clustering_integration 
   hdbscan_integration

.. toctree::
   :maxdepth: 4
   :caption: Tools

   relevanceai.report.vector

.. toctree::
   :maxdepth: 4
   :caption: Data Importers

   mongodb

.. toctree::
   :maxdepth: 4
   :caption: Available Datasets

   available_datasets

.. toctree::
   :maxdepth: 4
   :caption: Appendix

   changelog

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
