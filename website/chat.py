import os
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms import OpenAI
os.environ["OPENAI_API_KEY"] = "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" 
os.environ["SERPAPI_API_KEY"] = "a18893add3d966c28c9fd51597b51ade792515e030981f557e3cdf6ea13c3f35"

llm = OpenAI(temperature=0)
tools = load_tools(["serpapi"])
agent = initialize_agent(tools, llm, agent="zero-shot-react-description")

# from langchain.embeddings.openai import OpenAIEmbeddings
# from langchain.vectorstores import Chroma
# from langchain.text_splitter import CharacterTextSplitter
# from langchain import OpenAI, VectorDBQA
# from langchain.document_loaders import DirectoryLoader
# import magic
# import os
# import nltk 
# os.environ["OPENAI_API_KEY"] = "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"
# loader = DirectoryLoader('C:\\Users\\nikhi\\Downloads\\newfolder4',glob='**/*.csv')
# docs = loader.load()
# char_text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
# doc_texts = char_text_splitter.split_documents(docs)
# openAI_embeddings = OpenAIEmbeddings(openai_api_key=os.environ['OPENAI_API_KEY'])
# vStore = Chroma.from_documents(doc_texts, openAI_embeddings)
# model = VectorDBQA.from_chain_type(llm=OpenAI(), chain_type="stuff", vectorstore=vStore)