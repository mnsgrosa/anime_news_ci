import tiktoken
from haystack.components.preprocessors import DocumentSplitter


def prepare_synopsis(synopsis: str, genre: str, name: str, date: str) -> str:
    text_to_split = name + " " + genre + " " + synopsis

    splitter = DocumentSplitter(split_by="word", split_length=400, split_threshold=100)

    return splitter.run(documents=[text_to_split])
