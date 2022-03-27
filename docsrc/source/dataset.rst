..
   Manually maintained. Relevant functions are copied from docsrc/source/autoapi/relevanceai/dataset_api/dataset/index.rst

Dataset
=============================

Dataset is the class that Relevance AI uses to resolve a lot of complexity.

It is instantiated like this:

.. code-block::

    from relevanceai import Client
    client = Client()
    ds = client.Dataset("sample_dataset_id")
    ds.head()

You can also easily access metadata using the following: 

.. code-block::

    import time
    ds = client.Dataset("_mock_dataset_")
    ds.metadata['value'] = 3
    ds.metadata['strong_values'] = 10
    time.sleep(1)
    ds.metadata

.. automodule:: relevanceai.dataset.read.read
    :members:
    :exclude-members: __init__

.. automodule:: relevanceai.dataset.write.write
    :members:
    :exclude-members: __init__

.. autoclass:: relevanceai.dataset.io.export.Export
    :members: to_csv, to_dict, to_pandas_dataframe
    :exclude-members: __init__

.. automodule:: relevanceai.dataset.read.metadata
    :members:
    :exclude-members: __init__

.. autoclass:: relevanceai.dataset.read.statistics.Statistics
    :exclude-members: __init__
    :members:
