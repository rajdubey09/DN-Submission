
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

print("Loading 2nd Approach")
model_name = 'sentence-transformers/bert-base-nli-mean-tokens'
model = SentenceTransformer(model_name)


def approach(s1,s2):
    sentences_a1 = [
        s1,s2
    ]

    #Encoding:
    sentences_embeddings_a1 = model.encode(sentences_a1)

    #let's calculate cosine similarity for sentence 0:
    similar_value_a1 = cosine_similarity(
        [sentences_embeddings_a1[0]],
        sentences_embeddings_a1[1:]
    )
    print("Similarity found")
    return similar_value_a1[0][0]*100
