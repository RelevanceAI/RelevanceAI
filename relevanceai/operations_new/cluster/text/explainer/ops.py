"""

"""
from tqdm.auto import tqdm
from typing import Optional
from relevanceai.operations_new.cluster.text.explainer.base import BaseExplainer
from relevanceai.operations_new.apibase import OperationAPIBase
from relevanceai.utils.doc_utils.doc_utils import DocumentList


class TextClusterExplainerOps(BaseExplainer, OperationAPIBase):  # type: ignore
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def explain_clusters(
        self,
        dataset_id: str,
        vector_fields: list,
        alias: str,
        text_field,
        encode_fn,
        n_closest: int = 5,
        highlight_output_field: str = "_explain_",
        cluster_properties_filters: Optional[dict] = None,
    ):

        """
        For each cluster, we explain the closest documents to the centroid, and then highlight the most
        important words in the centroid and then for the centroid, we analyse what makes it similar to the second most similar document

        Parameters
        ----------
        text_field
            The field that contains the text to explain
        encode_fn
            The function that encodes the text. This is the same function that you used to encode the text in
        the dataset.
        n_closest : int, optional
            The number of closest documents to the centroid to explain
        highlight_output_field, optional
            The field that will be added to the document with the highlighted text.

        .. code-block::

            from relevanceai import Client
            client = Client()


        """
        # TODO:
        # Make this supported with cluster_ops.explain_text_clusters()

        # For each centroid, explains the closest n_closest to the centroids
        # Then highlights why the centroid is similar to the second most similar one
        # List the closest
        cluster_properties_filters = (
            {} if cluster_properties_filters is None else cluster_properties_filters
        )

        from relevanceai.operations_new.cluster.ops import ClusterOps

        cluster_ops = ClusterOps(
            credentials=self.credentials,
            vector_fields=vector_fields,
            alias=alias,
            dataset_id=dataset_id,
        )
        closest = cluster_ops.list_closest(
            page_size=n_closest,
            select_fields=[text_field],
            verbose=False,
            cluster_properties_filters=cluster_properties_filters,
        )
        # For the results in closest, we explain a text field
        # Flatten the closest
        for cluster, results in tqdm(closest["results"].items()):
            if len(results["results"]) < 2:
                continue
            query_text = self.get_field(text_field, results["results"][0])
            result_texts = self.get_field_across_documents(
                text_field, results["results"][1:]
            )
            # Explain the first one
            explained_answer = self.explain(
                encode_fn, query_text=result_texts[0], answer_text=query_text
            )
            results["results"][0][highlight_output_field] = {
                text_field: explained_answer
            }
            for i, r in enumerate(result_texts):
                explained_answer = self.explain(
                    encode_fn, query_text=query_text, answer_text=r
                )
                results["results"][i + 1][highlight_output_field] = {
                    text_field: explained_answer
                }

            # Update explained results
            updated = self._update_documents(
                dataset_id=cluster_ops.dataset_id, documents=results["results"]
            )

        print(
            f"Make sure to set the highlight field `{text_field}` with substring `{highlight_output_field + '.' + text_field}` at: "
        )
        print(
            f"https://cloud.relevance.ai/dataset/{cluster_ops.dataset_id}/dashboard/settings"
        )
        return closest

    def run(self, documents: DocumentList):
        # Not useful but having just for sake of abstractmethod - potentially can just take a list of documents to do something in the future
        raise NotImplementedError

    @property
    def name(self):
        return "textclusterexplainer"
