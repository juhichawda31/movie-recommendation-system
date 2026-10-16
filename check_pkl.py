import pickle

with open("tfidf.pkl", "rb") as file:
    tfidf = pickle.load(file)

with open("tfidf_matrix.pkl", "rb") as file:
    tfidf_matrix = pickle.load(file)

print("TF-IDF object:")
print(type(tfidf))

print("\nTF-IDF Matrix:")
print(type(tfidf_matrix))

print("\nMatrix shape:")
print(tfidf_matrix.shape)