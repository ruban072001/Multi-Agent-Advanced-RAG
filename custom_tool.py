from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field, ConfigDict
from chonkie import SemanticChunker
from qdrant_client import QdrantClient
from markitdown import MarkItDown

class documentsearchtoolinput(BaseModel):
    """Input schema for MyCustomTool."""
    questions: str = Field(..., description="Mandatory query you want to use to search the PDF's content")

class documentsearchtool(BaseTool):
    name: str = "documentsearchtool"
    description: str = (
        "A tool that can be used to semantic search a query from a PDF's content"
    )
    args_schema: Type[BaseModel] = documentsearchtoolinput

    model_config = ConfigDict(extra="allow")
    def __init__(self, file_path, db_path, collection_name, method):
        super().__init__()
        self.file_path = file_path
        self.db_path = db_path
        self.collection_name = collection_name
        self.client = None
        if method == "store":
            self.setup_client()
            self.load_text_DB()
        else:
            self.setup_client()


    def setup_client(self):
        if self.client is None:
            self.client = QdrantClient(path=self.db_path)
            
    def text_loading(self):
        print(f"Text extraction in progress...")
        md = MarkItDown()
        load_text = md.convert(self.file_path)
        texts = load_text.text_content

        return texts
        

    def text_splitting(self):
        texts = self.text_loading()
        print(f"Text splitting in Progress...")
        chunker = SemanticChunker(
            min_characters_per_sentence=50,
            min_chunk_size=512,
            min_sentences=5,
            chunk_size=1024,
        )
        chunks = chunker.chunk(texts)
        return chunks 
        

    def load_text_DB(self):
        chunks = self.text_splitting()
        print(f"Updating Database...")
        value = 0

        if self.client.collection_exists(collection_name=self.collection_name):
            old_db = self.client.get_collection(collection_name=self.collection_name)
            value = old_db.points_count
            print(value)
 
        chunks = [chunk.text for chunk in chunks]
        ids = [i+value for i in range(len(chunks))]
        metadatas = [{'metadata': self.file_path} for _ in range(len(chunks))]
    
        self.client.add(
            collection_name = self.collection_name,
            documents=chunks,
            metadata=metadatas,
            ids=ids
        )

        
    def _run(self, questions: str) -> str:
        
        print("retriving content...")
        result = self.client.query(
            collection_name=self.collection_name,
            query_text=questions
        )
        
        relevant_content = [i.document for i in result]
        return "\n\n".join(relevant_content)
    
if __name__ == "__main__":
    tool = documentsearchtool(
        file_path= r"C:\Users\KIRUBA\Desktop\Ruban_resume.pdf",
        db_path= r"C:\Users\KIRUBA\Documents\crewai_new_workflow\agentic_crew\VECTOR DB",
        collection_name= "ruban-resume",
        method="retrieve"
    )
    questions = "who is ruban?"
    result = tool._run(questions=questions)
    print(result)
