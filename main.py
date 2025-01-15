import streamlit as st
import os
from custom_tool import documentsearchtool
from crew import AgenticCrew
import time
from dotenv import load_dotenv
st.title("Multi-Agent Rag System")
load_dotenv()

CURRENT_DIRECTORY = os.path.dirname(__file__)
ALL_FILE_PATH = os.path.join(CURRENT_DIRECTORY, 'Files')

# files path
PDF_FILE_PATH = os.path.join(ALL_FILE_PATH, "PDF")
TXT_FILE_PATH = os.path.join(ALL_FILE_PATH, "TXT")
CSV_FILE_PATH = os.path.join(ALL_FILE_PATH, "CSV")
XL_FILE_PATH = os.path.join(ALL_FILE_PATH, "XL")
DOC_FILE_PATH = os.path.join(ALL_FILE_PATH, "DOC")

# Files count
PDF_FILE_COUNT = len(os.listdir(PDF_FILE_PATH))
TXT_FILE_COUNT = len(os.listdir(TXT_FILE_PATH))
CSV_FILE_COUNT = len(os.listdir(CSV_FILE_PATH))
XL_FILE_COUNT = len(os.listdir(XL_FILE_PATH))
DOC_FILE_COUNT = len(os.listdir(DOC_FILE_PATH))


if "crew" not in st.session_state:
    st.session_state.crew = None
    
if "document_tool" not in st.session_state:
    st.session_state.document_tool = None
    
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
    
with st.sidebar:
    DB_NAME = st.text_input("Enter the DB name")
    COLLECTION_NAME = st.text_input("Enter collection name")
    METHOD = st.selectbox(label= "Select an Option", placeholder="Choose an option", options=['store', 'retrieve'])
    DB_PATH = os.path.join(CURRENT_DIRECTORY, 'VECTOR DB', DB_NAME)
    files = st.file_uploader(
            "Select your file..", 
            accept_multiple_files=True, 
            type= ['.txt', '.pdf', '.xlxs', '.csv', '.docx']
        )
    click = st.button("process files")
    
    if click:
        if len(files) > 0:
        
            for file in files:
                file_extension = file.name.split('.')[-1]

                if file_extension == "pdf":
                    
                    PDF_FILE_NAME = f"pdf_{PDF_FILE_COUNT + 1}.pdf"
                    UPDATED_PDF_FILE_PATH = os.path.join(PDF_FILE_PATH, PDF_FILE_NAME)

                    with open(UPDATED_PDF_FILE_PATH, 'wb') as f:
                        f.write(file.getvalue())
                        
                    if len(files) - 1 == files.index(file):
                        
                        with st.spinner(f"Processing Uploaded files...{files.index(file) + 1} / {len(files)}"):
                            st.session_state.document_tool = documentsearchtool(
                                file_path=UPDATED_PDF_FILE_PATH,
                                db_path=DB_PATH,
                                collection_name=COLLECTION_NAME,
                                method=METHOD
                            )
                        st.success(f"Processing completed...{files.index(file) + 1} / {len(files)}")
                    else:
                        with st.spinner(f"Processing Uploaded files...{files.index(file) + 1} / {len(files)}"):
                            documentsearchtool(
                                file_path=UPDATED_PDF_FILE_PATH,
                                db_path=DB_PATH,
                                collection_name=COLLECTION_NAME,
                                method=METHOD
                            )
                
                elif file_extension == "csv":
                    CSV_FILE_NAME = f"csv_{CSV_FILE_COUNT + 1}.txt"
                    UPDATED_CSV_FILE_PATH = os.path.join(CSV_FILE_PATH, CSV_FILE_NAME)

                    with open(UPDATED_CSV_FILE_PATH, 'wb') as f:
                        f.write(file.getvalue())
                        
                    if len(files) - 1 == files.index(file):
                        
                        with st.spinner(f"Processing Uploaded files...{files.index(file) + 1} / {len(files)}"):
                            st.session_state.document_tool = documentsearchtool(
                                file_path=UPDATED_CSV_FILE_PATH,
                                db_path=DB_PATH,
                                collection_name=COLLECTION_NAME,
                                method=METHOD
                            )
                        st.success(f"Processing completed...{files.index(file) + 1} / {len(files)}")
                    else:
                        with st.spinner(f"Processing Uploaded files...{files.index(file) + 1} / {len(files)}"):
                            documentsearchtool(
                                file_path=UPDATED_CSV_FILE_PATH,
                                db_path=DB_PATH,
                                collection_name=COLLECTION_NAME,
                                method=METHOD
                            )
                            
                elif file_extension == "txt":
                    TXT_FILE_NAME = f"txt_{TXT_FILE_COUNT + 1}.txt"
                    UPDATED_TXT_FILE_PATH = os.path.join(TXT_FILE_PATH, TXT_FILE_NAME)

                    with open(UPDATED_TXT_FILE_PATH, 'wb') as f:
                        f.write(file.getvalue())
                        
                    if len(files) - 1 == files.index(file):
                        
                        with st.spinner(f"Processing Uploaded files...{files.index(file) + 1} / {len(files)}"):
                            st.session_state.document_tool = documentsearchtool(
                                file_path=UPDATED_TXT_FILE_PATH,
                                db_path=DB_PATH,
                                collection_name=COLLECTION_NAME,
                                method=METHOD
                            )
                        st.success(f"Processing completed...{files.index(file) + 1} / {len(files)}")
                    else:
                        with st.spinner(f"Processing Uploaded files...{files.index(file) + 1} / {len(files)}"):
                            documentsearchtool(
                                file_path=UPDATED_TXT_FILE_PATH,
                                db_path=DB_PATH,
                                collection_name=COLLECTION_NAME,
                                method=METHOD
                            )
                
                
                elif file_extension == "xlxs":
                    XL_FILE_NAME = f"xlxs_{XL_FILE_COUNT + 1}.xlxs"
                    UPDATED_XL_FILE_PATH = os.path.join(XL_FILE_PATH, XL_FILE_NAME)

                    with open(UPDATED_XL_FILE_PATH, 'wb') as f:
                        f.write(file.getvalue())
                        
                    if len(files) - 1 == files.index(file):
                        
                        with st.spinner(f"Processing Uploaded files...{files.index(file) + 1} / {len(files)}"):
                            st.session_state.document_tool = documentsearchtool(
                                file_path=UPDATED_XL_FILE_PATH,
                                db_path=DB_PATH,
                                collection_name=COLLECTION_NAME,
                                method=METHOD
                            )
                        st.success(f"Processing completed...{files.index(file) + 1} / {len(files)}")
                    else:
                        with st.spinner(f"Processing Uploaded files...{files.index(file) + 1} / {len(files)}"):
                            documentsearchtool(
                                file_path=UPDATED_XL_FILE_PATH,
                                db_path=DB_PATH,
                                collection_name=COLLECTION_NAME,
                                method=METHOD
                            )
                
                
                elif file_extension == "docx":
                    DOC_FILE_NAME = f"docx_{DOC_FILE_COUNT + 1}.docx"
                    UPDATED_DOC_FILE_PATH = os.path.join(DOC_FILE_PATH, DOC_FILE_NAME)

                    with open(UPDATED_DOC_FILE_PATH, 'wb') as f:
                        f.write(file.getvalue())
                        
                    if len(files) - 1 == files.index(file):
                        
                        with st.spinner(f"Processing Uploaded files...{files.index(file) + 1} / {len(files)}"):
                            st.session_state.document_tool = documentsearchtool(
                                file_path=UPDATED_DOC_FILE_PATH,
                                db_path=DB_PATH,
                                collection_name=COLLECTION_NAME,
                                method=METHOD
                            )
                        st.success(f"Processing completed...{files.index(file) + 1} / {len(files)}")
                    else:
                        with st.spinner(f"Processing Uploaded files...{files.index(file) + 1} / {len(files)}"):
                            documentsearchtool(
                                file_path=UPDATED_DOC_FILE_PATH,
                                db_path=DB_PATH,
                                collection_name=COLLECTION_NAME,
                                method=METHOD
                            )
                            
                else:
                    st.warning("File extension is not valid...Kindly upload the Mentioned files...")
                            
                            
                            
for chat_history in st.session_state.chat_history:
    with st.chat_message(chat_history["role"]):
        st.markdown(chat_history["content"])
        
        
prompt = st.chat_input("Ask your Question...")
if prompt:

    st.session_state.chat_history.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
        
    if st.session_state.crew is None:
        crew = AgenticCrew(st.session_state.document_tool)
        
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        with st.spinner("Thinking..."):
            inputs = {"questions": prompt}
            
            result = crew.crew().kickoff(inputs=inputs).raw

        lines = result.split('\n')
        for i, line in enumerate(lines):
            full_response += line
            if i < len(lines) - 1:  
                full_response += '\n'
            message_placeholder.markdown(full_response + "▌")
            time.sleep(0.25) 
            
        message_placeholder.markdown(full_response)

    st.session_state.chat_history.append({"role": "assistant", "content": result})
