#minsearch
minsearch is a lexical search engine, not a vector database
it does not understand words like a verctor databse does in the form of embeddings
instead it searches based on the words/tokens appearing in the document

Uses the inverted index approach,
words --> documents

lexical search strong when docs are short, vocab is specific, queries use the same terminology

#replacing minsearch with another library- sqlitesearch
1) minsearch builds the index at startup, in-memory search library
sqlitesearch - persistent sqlite-backend counterpart
Minsearch requires re-indexing at every startup, rebuilds it everytime a python process starts
sqlite- stores data on disk using sqllite, allowing the index to persist across sessions, suitable for larger datasets, or slower ingestion processes. (for when index needs to survive process restarts)

2) Both libraries share the same API, including methods like search, boost_dict, filter_dict, and num_results, making it easy to switch between them without changing application code

3) Minsearch is single-process and in-memory.
SQLitesearch supports a two-process architecture: one process for ingestion and another for querying, which is more suitable for production environments with larger or continuously updated datasets

4) SQLitesearch leverages SQLite's FTS5 for text ranking and additional vector search optimizations 
5) minsearch - just a bit of python dictionaries..




