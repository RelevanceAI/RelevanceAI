Changelog
=================

Here you will find a list of changes for each package update related to the Relevance AI
Python library.

v1.2.4
-----------

- Add `nltk-rake` support for keyphrases
- Add more documentation around cluster reporting
- Enable `Dataset` and `Series` access `pandas` `DataFrame` and `Series` methods, respectively
- Change `Dataset.health` from a property to a method and add `pandas` `DataFrame` output

v1.2.3
-----------

- Add Cluster Report endpoints

Developer changes:

- Fix bug with analytics and change to an env variable tracker for outermost function


v1.2.2
----------

Developer changes:

**BREAKING CHANGES**

- All list and dict default arguments are changed to `None`.

**Other Changes**
- Introduced `corr`, a method to plot the correlation between two fields, in `Dataset`
- Export to Pandas DataFrame

v1.2.1
----------

**BREAKING CHANGES**

- When upserting, you will no longer be returned confusing inserting/write statements.

**Other Changes**:

- Add option to `create_id` when inserting

Developer changes:

- Reduced number of documents in testing
- Make tracking only occur at the uppermost level and not the bottom level

v1.2.0
----------

**BREAKING CHANGES**

- When inserting/writing, you will now no longer be returned confusing insertion/write statements
but if it errors, it will return the JSON object with the necessary details.

- Add image tooling around processing (currently an alpha feature to be tested)
- Add `vectorize` method for text and images

v1.1.5
----------

- Feature/add beta decorator by @boba-and-beer in https://github.com/RelevanceAI/RelevanceAI/pull/461
- feature/pro-1267-remove-verbose-logs-from-output by @ofrighil in https://github.com/RelevanceAI/RelevanceAI/pull/457
- feature/pro-1299-add-a-insert_images_folder by @ofrighil in https://github.com/RelevanceAI/RelevanceAI/pull/456
- Add filters to clustering  by @boba-and-beer in https://github.com/RelevanceAI/RelevanceAI/pull/464
- silence dataset retrieval by @boba-and-beer in https://github.com/RelevanceAI/RelevanceAI/pull/465


v1.1.4
----------

- Add grading to auto_clustering
- Bug fix for cluster report
- Add DBSCAN centroids
- Fix HDBSCAN
- Add support for BIRCH, OPTICS and all native sklearn algorithms

v1.1.2
-------

- Added new DR methods to auto_reduce_dimensions
- Fixed documentation on clustering

v1.1.1
--------

- Change data structure of report structure

v1.1.0
--------

- Add low-touch way to label with a given model
- Add `label_from_dataset`, `label_from_list`, `label_from_common_words`

v1.0.8
---------

- Fix document-utils for clustering on DR

v1.0.7
-------

- Add grading for cluster report

v1.0.6
-------

- Fix http client and regionalisation issues and remove need for firebase

v1.0.5
--------

**Breaking changes**

- `get_cluster_internal_report` has now been renamed to `internal_report`

Non-breaking changes:

- Remove repetitive print statements
- Add outlier support for cluster report
- Support for centroids and medoids in typing
- Add pretty printing for cluster overall reporting

v1.0.4
---------

- add launch_search_app for dataset functionality
- remove saving .creds.json to avoid file caching

v1.0.3
---------

- Fix print error message with segment
- Separate out JSON Encoder

v1.0.2
--------

- Fix pandas serialization for UTF-encoding errors
- Move search app
- Change print search dashboard app URL
- Fix regionalisation error when authenticating client.

v1.0.1
--------
- Make pandas dataframe serializable with vectors

v1.0.0
---------

- Clustering report functionality
- Add fix and test for new cluster aggregate
- Add document mocking utility
- Add integration for cluster reporting
- Fix bug for sklearn clustering
- Add segment tracking with option to turn off
- Add print statement after inserting

v0.33.6
---------

- Fix warning missing parameter
- Remove `dataset_id` from `get_documents`
- Fix URL bug if you are logging in from `old-australia-east`

v0.33.5
--------

- Fix UX flow
- Make US-East-1 the default
- Add force refresh
- Rework Login UX
- Mention region when connecting
- Make the authentication message super cool
- Fix centroids to Node endpoint
- Update the delete request

v0.33.4
---------

- Make asynchronous dashboard request

v0.33.3
--------

- Fix cluster aggregate
- Fix for login
- Make adding firebase UID not breaking

v0.33.2
--------

- Update References for data imports
- Add :code-block:`auto_reduce_dimensions` with projector links

v0.33.1
---------

*BREAKING CHANGES*
- :code-block:`predict_dataset` has been corrected to :code-block:`predict_update`
- :code-block:`fit_dataset_by_partial` has been corrected to :code-block:`partial_fit_dataset`
- :code-block:`fit_partial` instances have been corrected to :code-block:`partial_fit`

- Hotfix auto_cluster when having more clusters than batch size
- Add dashboard link after clustering
- Fix references when listing closest and furthest

v0.33.0
---------

The most important part of this change is adding more modularity to the clustering functions.
This is important because previous functions tried to abstract away too much.
Now, users


*BREAKING CHANGES*

- Clustering :code:`fit_transform` is not a :code:`fit_predict` to align with SKLearn's methods
- Rename :code:`Clusterer` to :code:`ClusterOps`
- :code:`fit` has now been broken down into :code:`fit_predict_update`
- Removed KMeansClusterer

Non-breaking changes:

- Create a CentroidClusterBase and update it to ClusterBase and a CentroidBase
- Added a `fit_update`
- Added support for batch clustering using MiniBatchKMeans
- Added functional Insert_centroid_documents to the `ClusterOps` object
- Introduced fit_partial to the clusterer
- Introduced fit_partial_documents
- Introduced `fit_dataset_by_partial` to allow users to be able to fit on a dataset if they want to use
partial_fit
- Introduced `fit_update_dataset`
- Introduced `fit_update_dataset_by_partial` which will fit the dataset, predict the dataset
and insert the centroids if there are expected centroids in the dataset
- Introduced `fit_partial_predict_update` to allow for fitting, predicting and updating the dataset
in 1 go
- Fixed arguments in the `clusterer` object to now take an optional vector_fields and dataset
- Feature/fix clustering transform by @boba-and-beer in https://github.com/RelevanceAI/RelevanceAI/pull/372
- add fix for dim reduction by @boba-and-beer in https://github.com/RelevanceAI/RelevanceAI/pull/374
- removed python manta on startup by @jtwinrelevanceai in https://github.com/RelevanceAI/RelevanceAI/pull/376
- Feature/add support for batch by @boba-and-beer in https://github.com/RelevanceAI/RelevanceAI/pull/375
- Hotfix/pull update filter error by @boba-and-beer in https://github.com/RelevanceAI/RelevanceAI/pull/379
- auto_cluster function by @jtwinrelevanceai in https://github.com/RelevanceAI/RelevanceAI/pull/373
- Feature/try fix cluster references by @boba-and-beer in https://github.com/RelevanceAI/RelevanceAI/pull/380


**Full Changelog**: https://github.com/RelevanceAI/RelevanceAI/compare/v0.32.0...v0.33.0

v0.32.1
---------

- Apply hotfix to pull_update_push

v0.32.0
---------

*BREAKING CHANGES*

- Move search to inside operations to keep consistency

New Features:

- Added Dimensionality Reduction
- Added Labelling

Non-breaking changes:

- Fix bug with clusterer using `fit_predict` now
* Feature/pro 1107 bug with clusterer by @boba-and-beer in https://github.com/RelevanceAI/RelevanceAI/pull/360
* Added Cluster Metrics to ClusterOps by @jtwinrelevanceai in https://github.com/RelevanceAI/RelevanceAI/pull/347
* Feature/fix auth by @boba-and-beer in https://github.com/RelevanceAI/RelevanceAI/pull/361
* removing dataset_id as a required parameter by @ChakavehSaedi in https://github.com/RelevanceAI/RelevanceAI/pull/366
* add dimensionality reduction by @boba-and-beer in https://github.com/RelevanceAI/RelevanceAI/pull/362
* added faiss kmeans integrations example by @jtwinrelevanceai in https://github.com/RelevanceAI/RelevanceAI/pull/364
* adding pretty html for df by @ofrighil in https://github.com/RelevanceAI/RelevanceAI/pull/337
* Feature/add df label by @boba-and-beer in https://github.com/RelevanceAI/RelevanceAI/pull/365
* Fix conflicts by @boba-and-beer in https://github.com/RelevanceAI/RelevanceAI/pull/369
* Nice code blocks for datatsets by @jtwinrelevanceai in https://github.com/RelevanceAI/RelevanceAI/pull/368
* black files by @boba-and-beer in https://github.com/RelevanceAI/RelevanceAI/pull/370


**Full Changelog**: https://github.com/RelevanceAI/RelevanceAI/compare/v0.31.0...v0.32.0


v0.31.0
---------

- Include more native sklearn integration. KMeans and MiniBatchKMeans now supported natively.
- Fix to `vectorize` and `sample` in Series
- Fixes to cluster aggregation for the clusterer class and cluster metrics for the clusterer class
- `groupby` and `agg` now supported
- Added warnings to `vectorize` method
- Bug Fix to list_closest_to_center to now return results
- Add `send_dataset`
- Add `clone_dataset`
- Add references to available example datasets
- Added `vector_search`, `chunk_search` , `multistep_chunk_search`, `hybrid_search`
as part of the search endpoints

Developer changes:

- Added warnings module (boba-and-beer)
- Folder factor for datasets API (boba-and-beer)
- 2x Test speed up by introducing pytest-xdist with file distribution strategy (boba-and-beer)

Tests are now run modularly. In other words, if you want tests to run together, keep
them in the same file. If you want them to run in parallel, keep them in separate files.

v0.30.1
--------

Non-breaking changes:

- Fixed incorrect reference in `update_documents`
- Fixed bulk getting the wrong document in `df.get()` and added subsequent unit test
- Fixed references with apply
- Added health endpoints
- Added `insert_pandas_dataframe` endpoints
- Test folder refactor and clean up

Developer changes:
- Forced precommits
- Added minimum pytest coverage

Auto Generated Release Notes:

* Fixing _get_all_documents by @charyeezy in https://github.com/RelevanceAI/RelevanceAI/pull/338
* Updating df.filter docstring by @charyeezy in https://github.com/RelevanceAI/RelevanceAI/pull/341
* Fix test for inserting csv by @boba-and-beer in https://github.com/RelevanceAI/RelevanceAI/pull/339
* Feature/add precommit and force pytest by @boba-and-beer in https://github.com/RelevanceAI/RelevanceAI/pull/344
* Feature/add tests by @boba-and-beer in https://github.com/RelevanceAI/RelevanceAI/pull/346
* specify pandas dataframe by @boba-and-beer in https://github.com/RelevanceAI/RelevanceAI/pull/349
* Accelerate testing  by @boba-and-beer in https://github.com/RelevanceAI/RelevanceAI/pull/348
* typo and example by @ChakavehSaedi in https://github.com/RelevanceAI/RelevanceAI/pull/351

v0.30.0
---------

**BREAKING CHANGES**

- Renamed all `docs` references to `documents`
- Renamed all `cluster_alias` references to `alias`
- Changed functionality in CentroidClusterBase
- Renamed chunk_size to chunskize in get_all_documents
- Renamed `retrieve_chunk_size` to `retrieve_chunksize` in `df.apply` and `df.bulk_apply`
- Schema is now a property and not a method!
- `get_centroid_documents` now no longer takes a field
- Removal of any mention of `centroid_vector_` as those should now be replaced with the
actual vector field name the centroids are derived from

Non-breaking changes:

- Added `head` to Series object
- Add CentroidClustererbase and CentroidClusterBase classes to inherit from
- Deprecated KMeansClusterer in documentation and functionality
- Add fix for clusterer for missing vectors in documents by forcing filters
- Support for multi-region base URL based on frontend parsing
- Added AutoAPI to gitignore as we no longer want to measure that
- Add tighter sklearn integration
- Add CentroidClusterBase
- Clean up references around Clusterbase, ClusterOps, Dataset
- Add reference to Client object
- Hotfix .sample()
- Update the Base Ingest URL to gateway and set to appropriate default
- Added support for base url token
- Removed QC from references
- Add integration reference
- Fixed centroid insertion for Dataset
- Refactor of tests based
- Add clustering test around clustering
- Separation of references to clean up clustering and sidebar menu navigation
- Fix reference examples

AUTO-GENERATED RELEASE NOTES:

- Update README.md by @JackyKoh in https://github.com/RelevanceAI/RelevanceAI/pull/314
- Feature/refactor docsrc by @boba-and-beer in https://github.com/RelevanceAI/RelevanceAI/pull/315
- hotfix sample by @boba-and-beer in https://github.com/RelevanceAI/RelevanceAI/pull/316
- add installation suggestion by @boba-and-beer in https://github.com/RelevanceAI/RelevanceAI/pull/317
- Renaming docs to documents and cluster_alis to alias by @charyeezy in https://github.com/RelevanceAI/RelevanceAI/pull/308
- added column value to df.info by @jtwinrelevanceai in https://github.com/RelevanceAI/RelevanceAI/pull/321
- update ingest to gateway by @boba-and-beer in https://github.com/RelevanceAI/RelevanceAI/pull/318
- Feature/remove qc by @boba-and-beer in https://github.com/RelevanceAI/RelevanceAI/pull/322
- Feature/separate centroid cluster bases by @boba-and-beer in https://github.com/RelevanceAI/RelevanceAI/pull/323
- Feature/fix series object by @boba-and-beer in https://github.com/RelevanceAI/RelevanceAI/pull/324
- Renaming datasets by @charyeezy in https://github.com/RelevanceAI/RelevanceAI/pull/320
- add integration RST and code improvements by @boba-and-beer in https://github.com/RelevanceAI/RelevanceAI/pull/326
- added df.filter to dataset api by @jtwinrelevanceai in https://github.com/RelevanceAI/RelevanceAI/pull/319
- Reference Quality check by @jtwinrelevanceai in https://github.com/RelevanceAI/RelevanceAI/pull/325
- Feature/fix docsrc 2 by @boba-and-beer in https://github.com/RelevanceAI/RelevanceAI/pull/328
- Fixing notebook test by @charyeezy in https://github.com/RelevanceAI/RelevanceAI/pull/327
- Feature/fix example custom cluster model by @boba-and-beer in https://github.com/RelevanceAI/RelevanceAI/pull/329
- fixed centroids by @jtwinrelevanceai in https://github.com/RelevanceAI/RelevanceAI/pull/330
- add core by @boba-and-beer in https://github.com/RelevanceAI/RelevanceAI/pull/331
- Update documentation on kmeans cluster model  by @boba-and-beer in https://github.com/RelevanceAI/RelevanceAI/pull/332
- Feature/fix references 3 by @boba-and-beer in https://github.com/RelevanceAI/RelevanceAI/pull/334
- added kmeans integration by @jtwinrelevanceai in https://github.com/RelevanceAI/RelevanceAI/pull/333


v0.29.1
---------

- Moved get_all_documents in BatchAPIClient to _get_all_documents to resolve typing error
- Include Client, Fix ClusterOps, ClusterBase, update Cluster References
- Add Write Documentation by @boba-and-beer in https://github.com/RelevanceAI/RelevanceAI/pull/311
- update clustering documentation and client documentation by @boba-and-beer in https://github.com/RelevanceAI/RelevanceAI/pull/312


v0.29.0
--------

- Added value_counts method to Dataset API by @jtwinrelevanceai in https://github.com/RelevanceAI/RelevanceAI/pull/272
- Added to_dict for pandas dataset api by @jtwinrelevanceai in https://github.com/RelevanceAI/RelevanceAI/pull/293
- Feature/add clusterer object by @boba-and-beer in https://github.com/RelevanceAI/RelevanceAI/pull/306
- Feature/fix references docs by @boba-and-beer in https://github.com/RelevanceAI/RelevanceAI/pull/302
- Feature/edit docs by @boba-and-beer in https://github.com/RelevanceAI/RelevanceAI/pull/309

v0.28.2
--------

- Update RELEASES.md by @jtwinrelevanceai in https://github.com/RelevanceAI/RelevanceAI/pull/287
- Feature/make conda installable by @boba-and-beer in https://github.com/RelevanceAI/RelevanceAI/pull/288
- Concatentate Numeric Features into Vector by @jtwinrelevanceai in https://github.com/RelevanceAI/RelevanceAI/pull/289
- from_csv and to_csv - Dataset API by @jtwinrelevanceai in https://github.com/RelevanceAI/RelevanceAI/pull/281
- Fixing hybrid search field by @charyeezy in https://github.com/RelevanceAI/RelevanceAI/pull/285
- created mean method for GroupBy and corresponding test by @ofrighil in https://github.com/RelevanceAI/RelevanceAI/pull/291
- Add link by @boba-and-beer in https://github.com/RelevanceAI/RelevanceAI/pull/299
- Feature/pinning notebook version to 0.27.0 in notebook tests by @charyeezy in https://github.com/RelevanceAI/RelevanceAI/pull/301
- Update centroid documents and restructure docs  by @boba-and-beer in https://github.com/RelevanceAI/RelevanceAI/pull/300
- make alias required by @boba-and-beer in https://github.com/RelevanceAI/RelevanceAI/pull/296
- @ofrighil made their first contribution in https://github.com/RelevanceAI/RelevanceAI/pull/291


v0.28.1
--------

- removed clustering results from get_realestate_dataset by @ChakavehSaedi in https://github.com/RelevanceAI/RelevanceAI/pull/277
- add option to print no dashboard by @boba-and-beer in https://github.com/RelevanceAI/RelevanceAI/pull/278
- move to node implementation for listing furthest by @boba-and-beer in https://github.com/RelevanceAI/RelevanceAI/pull/279
- add output field to apply by @boba-and-beer in https://github.com/RelevanceAI/RelevanceAI/pull/282
- Add releases workflow markdown and diagram
- Fix clustering tests

v0.28.0
--------

- *Breaking Change*️ Change pull_update_push to use dataset ID
- Added centroid distance evaluation
- Added JSONShower to df.head() so previewing images is now possible
- Refactor Pandas Dataset API to use BatchAPIClient
- Modularise testing infrastructure to use separate datasets
- Add aggregation, groupby pandas API support
- Added GroupBy, Series class for Datasets
- Added datasets.info()
- Added documentation testing
- Added df.apply()
- Added additional functionality for sampling etc.
- Fixed documentation for Datasets API
- Add new monitoring health test for chunk data structure
- Add fix for csv reading for _chunk_ to be parsed as actual Python objects
and not strings

v0.27.0
--------

- Fixed datasets.documents.update_where so it runs
- Added more tests around multivector search
- Added Pandas-like Dataset Class for interacting with SDK (Alpha)
- Added datasets.cluster.centroids.list_furthest_from_centers and datasets.cluster.centroids.list_closest_to_centers
- Folder Refactor

v0.26.6
--------

- Fix missing import in plotting since internalising plots
- Add support for vector labels
- Remove background axes from plot

v0.26.5
---------

- Fix incorrect URL being submitted to frontend

v0.26.4
---------

- Fix string parsing issue for endpoints and dashboards

v0.26.3
---------

- Cluster labels are now lower case
- Bug fix on centroids furthest from center
- Changed error message
- Fixed Dodgy string parsing
- Fixed bug with kmeans_cluster 1 liner by supporting getting multiple centers

v0.26.2
---------

- Add CSV insertion
- Make JSON encoder utility class for easier customisation
- Added smarter parsing of CSV

v0.26.1
---------

- Bug fixes

v0.26.0
---------

- Added JSON serialization and consequent test updates
- Bug fix to cluster metrics
- Minor fix to tests
