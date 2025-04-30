from collections import defaultdict, Counter

def build_index(docs):
    index = []
    for doc in docs:
        word_count = Counter(doc.split())
        index.append(word_count)
    return index

def search(index, query):
    query_words = set(query.split())
    relevance = []
    for i, doc in enumerate(index):
        score = sum(doc[word] for word in query_words if word in doc)
        if score > 0:
            relevance.append((score, -i))
    relevance.sort(reverse=True)
    return [-idx for _, idx in relevance[:5]]

def main():
    n = int(input())
    docs = [input().strip() for _ in range(n)]
    index = build_index(docs)
    
    q = int(input())
    for _ in range(q):
        query = input().strip()
        result = search(index, query)
        print(" ".join(str(r + 1) for r in result))

if __name__ == '__main__':
    main()
