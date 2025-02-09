*****AgenticCrew: Intelligent Document Retrieval and Response System*****

      AgenticCrew is a modular and extensible framework built using the CrewAI library for intelligent document retrieval and response generation. 

      This system integrates multiple agents and tasks to efficiently retrieve, process, and update relevant content from documents while leveraging external tools like Google Search for enhanced context.

**Features**

    **Agent-Based Architecture:** Four specialized agents for retrieving, updating, and responding to document queries.
    
    **retriever_agent:** Extracts relevant content from documents.
    
    **update_retriever_agent:** Refines and updates the retrieved content.
    
    **response_agent:** Generates meaningful responses from the content.
    
    **update_response_agent:** Updates the generated responses as needed.
    
    **Task Management:** Each agent has a dedicated task for modular functionality.

**Tool Integration:** Leverages tools like:

    1 Custom document_tool for document processing.
    2.SerperDevTool for Google Search integration.

**Flexible Workflow:** Supports sequential and hierarchical processing for complex pipelines.

**Configurable Design:** Easy configuration using agents.yaml and tasks.yaml files.


***Workflow***

    **Retrieve:** Relevant content is extracted from documents using retriever_agent.
    
    **Update:** Content is refined using update_retriever_agent.
    
    **Respond:** Responses are generated based on the retrieved content.
    
    **Refine:** Responses are updated for accuracy and relevance.


**Clone the repository:**
git clone https://github.com/your-username/AgenticCrew.git


**Install dependencies:**
    pip install -r requirements.txt
    
    Set up environment variables by creating a .env file.
    
    Configure the agents.yaml and tasks.yaml files in the config directory.

***USE this comment to run main.py file** : 
python -m streamlit run main.py

Contributing
Contributions are welcome! Feel free to fork the repo and submit a pull request.
