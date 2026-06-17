# LLM vocabulary translation instead of vector database

The skill's primary users are Business Analysts who describe processes in plain English rather than COSMIC terminology. A vector database was considered to bridge this vocabulary gap at retrieval time. We rejected it in favour of an explicit LLM translation step: before grepping `manuals-indexed/`, Claude maps the user's natural language to COSMIC vocabulary (Entry, Exit, Read, Write, triggering event, persistent storage, etc.), then greps with those terms.

The corpus is ~208 KB of heading-chunked markdown — small enough that the translation step fully solves the retrieval problem without any new infrastructure. A vector database would add an embedding pipeline, a runtime dependency, and operational overhead over a fixed, rarely-updated corpus. Since the LLM is already in the loop extracting keyword phrases (Q&A oracle step 1), making the COSMIC translation explicit costs nothing incremental.

## Considered Options

- **Vector database (e.g. ChromaDB, pgvector)** — rejected because the corpus size does not justify the operational complexity, and the LLM translation step solves the same vocabulary-bridging problem at zero additional cost.
- **Synonym expansion in the skill prompt** — viable for developer users (query→Read, insert→Entry), but insufficient for BA natural language where there is no reliable lexical mapping.

## Consequences

The Q&A oracle workflow must make the translation step explicit: extract COSMIC terms from the user's phrasing before grepping, not after. If the corpus grows substantially (multiple additional manuals, translated editions) or the user population shifts to a context where LLM latency is unacceptable, revisit this decision.
