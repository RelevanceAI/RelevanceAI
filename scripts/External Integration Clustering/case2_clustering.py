"""
This script demonstrates a class based approach for clustering with KMeans Using the new Pandas-Like Dataset API for RelevanceAI Python Package
"""

import argparse

from relevanceai import Client
from relevanceai.clusterer import Clusterer
from relevanceai.clusterer.kmeans_clusterer import KMeansModel


def main(args):
    client = Client()

    df = client.Dataset(args.dataset_id)
    vector_field = args.vector_field
    n_clusters = int(args.n_clusters)

    model = KMeansModel(k=3)

    clusterer = Clusterer(model=model, alias=f"kmeans-{n_clusters}")

    clusterer.fit(dataset=df, vector_fields=[vector_field])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="class based clustering")

    parser.add_argument("dataset_id", help="The dataset_id of the dataset to cluster")
    parser.add_argument("vector_field", help="The vector field over which to cluster")
    parser.add_argument("n_clusters", help="The number of clusters to find")

    args = parser.parse_args()
    main(args)
