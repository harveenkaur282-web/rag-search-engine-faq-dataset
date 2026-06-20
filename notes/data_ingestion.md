![alt text](image.png)
knowledge base is the common element here


#elasticsearch
Elasticsearch is the industry standard for text search.

It supports:

Full-text search with BM25
Filtering, aggregations, and faceting
Vector search (dense and sparse)
Distributed scaling
Real-time indexing


#prob of version 1.0- only rag(not agentic)

Often, though, the search returns nothing useful.

Maybe the user made a typo.
Maybe they asked the question in an unusual way.
Maybe they need information from two different searches.

Instead of routing the user question straight to search, we can hand control to the LLM and let it drive.

The LLM is in charge now, and it can:

fix typos
search again with different terms
ask the user a clarifying question



In Part 2 of this module, we'll cover:

Function calling, so we can give the LLM tools it can use
The agentic loop, where the LLM decides when to call a tool, when to call another one, and when to stop and answer
Frameworks, the libraries that run this loop for you