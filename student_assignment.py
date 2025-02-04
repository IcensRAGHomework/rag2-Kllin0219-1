from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (CharacterTextSplitter,
                                      RecursiveCharacterTextSplitter)

q1_pdf = "OpenSourceLicenses.pdf"
q2_pdf = "勞動基準法.pdf"


def hw02_1(q1_pdf):
    loader = PyPDFLoader(q1_pdf)
    docs = loader.load()

    text_splitter = CharacterTextSplitter(chunk_overlap=0)
    chunks = text_splitter.split_documents(docs)
    
    return chunks[-1]

def hw02_2(q2_pdf):
    loader = PyPDFLoader(q2_pdf)
    docs = loader.load()
    
    whole_text = "\n".join(doc.page_content for doc in docs)
    
    regex_separator = r'(?=\n\s*第\s.*(?:條|章).*)'

    recursive_splitter = RecursiveCharacterTextSplitter(
        chunk_overlap=0,
        chunk_size=30,
        separators=[regex_separator],
        is_separator_regex=True
    )
    
    chunks = recursive_splitter.split_text(whole_text)
    # for chunk in chunks:
    #     print("===")
    #     print(chunk)
    # print(chunks[0])
    return len(chunks)


if __name__ == '__main__':
    chunk = hw02_1(q1_pdf)
    # print(chunk)
    
    chunk_count = hw02_2(q2_pdf)
    print(chunk_count)