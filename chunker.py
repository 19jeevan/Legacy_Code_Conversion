import tiktoken

MAX_TOKENS = 3000
encoder = tiktoken.get_encoding("cl100k_base")


def chunk_code(code: str):
    tokens = encoder.encode(code)
    chunks = []

    for i in range(0, len(tokens), MAX_TOKENS):
        chunk = encoder.decode(tokens[i:i + MAX_TOKENS])
        chunks.append(chunk)

    return chunks