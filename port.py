import streamlit as st
from streamlit_lottie import st_lottie
import json, os
from PIL import Image
from streamlit_option_menu import option_menu


st.set_page_config(page_title="My portfolio", page_icon=':tada:', layout='wide')

def lottie_file(filepath):
    with open(filepath, 'r',encoding='utf-8') as file:
        return json.load(file)
    
selected = option_menu(
    menu_title="",
    options= ["Home","Projects","Publications", "Blogs" ],
    icons= ["house", "briefcase", "book", "file-text"],
    default_index=0,
    orientation="horizontal"
) 
lottie_filepath= os.path.join('static', 'lottie.json')
ln_filepath=os.path.join('static','ln.json')
research_filepath= os.path.join('static','research.json')


lottie_json= lottie_file(lottie_filepath)
resarch_json= lottie_file(research_filepath)
ln=lottie_file(ln_filepath)
buddymate= Image.open('images/buddymate.jpg')
ats=Image.open('images/ats.jpg')
worlds4= Image.open('images/worlds4.jpg')
cert=Image.open('images/cert.jpg')
medium = Image.open('images/medium.jpg')
RAG=Image.open('images/rag.jpg')


if selected=='Home':
    with st.container():
        st.subheader("Hi I am Pavan sai :wave:")
        st.title('About Me :)')
        st.write("""  I’m Pavan Sai Bolliboina, passionate tech nerd about building cool tech that makes a difference. 
                 I love diving into Python, Django, and AI/ML to turn complex problems into elegant, practical solutions.
                  My journey in tech is driven by curiosity and a constant desire to learn and grow. 
                 Whether I’m developing backend systems, deploying machine learning models, or exploring new AI innovations, 
                 I’m always excited for the next challenge.""")
    
#007DC5
#----what i do----

    with st.container():
        st.write('---')
        leftcolumn, rightcolum = st.columns(2)
        with leftcolumn:
            st.header('Professional Experience')
            st.markdown("""<h2><span style ="color:#007DC5;">TATA CONSULTANCY SERVICES</span></h2> """, unsafe_allow_html=True)
            st.markdown(''' <h6> <em>August 2020 - September 2022</em></h6>''',unsafe_allow_html=True)
            st.markdown("""<h3><span style="color: #C0C0C0;">Client :</span> 
                        <span style="color: #94ffeb;">Mars Inc.</span></h3>""",unsafe_allow_html=True)
            st.markdown(
                '''  
                - Collaborated with Mars Incorporated to establish and maintain Dynamics 365 infrastructure in Azure cloud, leveraging Azure fundamentals.
                - Developed and configured automated scripts in Azure, utilizing Infrastructure as Code (IaC) principles, which resulted in a 20 percent reduction in operational expenses.
                -  Monitored Azure cloud infrastructure for over 20 countries in 3 global regions (EU-AMER-APAC) using Splunk and CheckMk, ensuring high levels of scalability, reliability, and performance.
                -  Conducted over 30 Disaster Recovery drills in Azure, ensuring robust resilience and secure production environment provisioning.
                - Implemented agile and DevOps methodologies, significantly enhancing project development efficiency and reducing deployment times through Continuous integration and continuous Delivery (CI/CD) pipelines.
                - Worked with various teams to troubleshoot incidents, issues,  identify root causes, and implement preventive measures, fostering a collaborative DevOps culture.'''
            )
            st.markdown("""<h2><span style ="color:#d1190d;">MONTCLAIR STATE UNIVERSITY</span></h2> """, unsafe_allow_html=True)
            st.markdown(''' <h6> <em>october 2022 - May 2024</em></h6>''',unsafe_allow_html=True)
            st.markdown("""<h3><span style="color: #94ffeb;">Research Assistant</span></h3>""",unsafe_allow_html=True)
    
        
        with rightcolum:
            st_lottie(lottie_json, speed=1, width=800, height=400, key="lottie_animation")

          
    with st.container():
        leftcolumn, rightcolum = st.columns(2)
        with leftcolumn:
            st.markdown(
                '''  
                - Developed a Retrieval-Augmented Generation (RAG) chatbot utilizing Llama2 and Sentence Transformers for efficient document querying and retrieval.
                - Utilized FAISS for vector storage, ensuring accurate retrieval of document embeddings and improving query response times.
                -  Designed a robust backend using Python and Flask, facilitating seamless integration with document processing logic.
                -  Conducted research on the performance comparison of OpenAI API and private API of chatbots, presented at the WORLDS4 conference in London, UK.
                - Developed an ATS compatibility tool that parses PDF resumes and compares them against job descriptions using Streamlit and Python.
                - Integrated Google’s generative AI to evaluate resumes, providing detailed suggestions to enhance match rates with targeted job roles.
                - Implemented features for identifying critical keywords for ATS optimization, guiding users on effective incorporation into their resumes.
                - Created an automated resume rewriting option, improving users' chances of landing interviews by ensuring alignment with job description criteria.
                - Developed a task management web application using Django and Python for efficient team collaboration.
                - Utilized PostgreSQL as the primary database for reliable and scalable task data management.
                - Implemented user authentication and role-based access control, ensuring secure access to application features.
                - Designed an intuitive user interface using Django templates and Bootstrap for a seamless user experience.
                - Deployed the application on a cloud platform, demonstrating skills in maintaining web applications in production environments.
                '''
                )
            with rightcolum:
                st_lottie(resarch_json, speed=1, width=800, height=400, key="research_animation")

if selected=='Projects':
    with st.container():
        st.header("My Projects")
        st.write('---') 
        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image(RAG, width=300)
        with text_column:
            st.header("Project name : Docuquery-RAG-Bot")
            st.subheader("Overview")
            st.write("""Docuquery-RAG-Bot is a powerful tool designed to provide answers to user queries by 
                     leveraging state-of-the-art language models and vector databases. """)
            st.markdown(
                """
                <a href="https://github.com/Bolliboinapavansai/Docuquery-RAG-Bot" target="_blank">
                    <button style="padding:10px 20px; background-color: #007bff; border: none; border-radius: 5px;font-size:16px; cursor:pointer;">Click Here To Know More</button>
                </a>
                """,
                unsafe_allow_html=True)
            
    with st.container():
        
        st.write('---')

        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image(ats, width=300)
        with text_column:
            st.header("Project name : ATS RESUME TRACKER USING GOOGLE GENERATIVE AI")
            st.subheader("Overview")
            st.write("""ATS Resume Tracker is an advanced Applicant Tracking System (ATS) that leverages Google Generative AI 
                     to evaluate resumes against job descriptions. It provides detailed insights into resume fit, skill enhancement
                      recommendations, and match percentages to streamline the recruitment process.""")
            st.markdown(
                """
                <a href="https://github.com/Bolliboinapavansai/ATS_Resume-Tracker" target="_blank">
                    <button style="padding:10px 20px; background-color: #007bff; border: none; border-radius: 5px;font-size:16px; cursor:pointer;">Click Here To Know More</button>
                </a>
                """,
                unsafe_allow_html=True)


        
    with st.container():
        st.write('---')
        
        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image(buddymate, width=300)
        with text_column:
            st.header("Project name : BUDDY TASK A TASKMANAGER APP")
            st.subheader("Overview")
            st.write("""Buddytask is a robust task manager web application built with the powerful Django Framework. 
                     This project delves deep into Django's MVT (Model-View-Template) architecture, 
                     showcasing seamless integration and functionality of various features and libraries.""")
            st.markdown(
                """
                <a href="https://github.com/Bolliboinapavansai/django_buddytask" target="_blank">
                    <button style="padding:10px 20px; background-color: #007bff; border: none; border-radius: 5px;font-size:16px; cursor:pointer;">Click Here To Know More</button>
                </a>
                """,
                unsafe_allow_html=True)
            
    
            
if selected == 'Publications':
    with st.container():
        st.write("#")
        leftcolumn, rightcolum = st.columns((3,1))
        with rightcolum:
            st.image(worlds4, width=300)
        with leftcolumn:
            st.markdown(''' 
                <h2><span style="color: white;">Publishing Platform: </span></h2><h5><span style ="color:#FFFF00;"><em> WorldS4 2024 in London, United Kingdom</em></span></h5> 
                ''', unsafe_allow_html=True)
        st.write("---")
        st.markdown(''' 
            <h4><span style="color: white;">PAPER TITLE: </span><span style ="color:#FFFF00;"><em>Performance Comparision of Private AI Chatbot and Public AI Chatbot</em></span></h4> 
            ''', unsafe_allow_html=True)
        st.write("#")
        text_column,image_column  = st.columns((2,1))
        with image_column:
            st.image(cert, width=300)
        with text_column:
            st.subheader("About the paper:")
            st.write("""In this paper, we develop an AI chatbot portal using Python Flask
                      server. LangChain was used for setting up the backend process. For phase one,
                      we load and process our PDF documents and use LangChain’s text splitter, RecursiveCharacterTextSplitter, to break up these documents into smaller chunks.
                       HuggingFaceEmbeddings is then used to create embeddings for each chunk and
                            we use Facebook AI Similarity Search (FAISS) to index the embeddings. For
                         phase two, the Question and Answer, FAISS is used to retrieve relevant chunks.
                            CTransformers is used for language model interactions and uses these chunks to
                       generate the answer. The answer is then displayed on the browser screen. For
                    comparison purposes, we develop three versions of this system. The first version
                   utilizes data and knowledge from a pdf on the local store. The second version
                   uses Google search engine AI APIs to send the query and receive the query result.
                  The third one is a hybrid form which uses the local bot to handle the query. If it
                 is unable to do so, it will then fall back to use the search engine AI bot. This paper
                      will only examine and compare the results of version 1 and version 2. We will
                     also briefly discuss the advantages and disadvantages of public and private AI
             bots, as well security concerns. According to our experimental results, the search
                   engine AI outperforms the private local AI bots.""")


if selected == 'Blogs':
    with st.container():
        st.write('#')
        text_column,image_column  = st.columns((2,1))
        with image_column:
            st.image(medium, width=300)
        with text_column:
            st.header("My Blogs")
            st.write("""
                    🚀 **Hey there, tech enthusiasts!** 🚀

                    Are you a self-proclaimed tech nerd with an insatiable curiosity for all things geeky? 🤓 Well, you’re in the right place! I’m a newbie blogger on Medium, and I’m here to sprinkle some nerdy magic into your feed.

                    If you’re into code, gadgets, and the occasional techie joke (Why do programmers prefer dark mode? Because light attracts bugs! 🦠), then hit that **Follow** button and join me on this epic tech adventure. Let’s dive into the geeky goodness together!

                     Catch you on the flip side of the code! 💻✨
                    """)
            st.markdown(f"""<style>.button {{
                            padding: 10px 20px;
                            background-color: #f0f0f0; /* Neutral button background color */
                            border: 2px solid #f0f0f0;
                            border-radius: 10px;
                            color: #39ff14;
                            font-size: 16px;
                            font-weight: bold;
                            cursor: pointer;
                            text-align: center;
                            text-decoration: none;
                            display: inline-block;
                        }}.button:hover {{
                            background-color: #ADD8E6;
                            text-decoration: none;
                                }}
                        </style><a href="https://pavansaibolliboina.medium.com/" target="_blank" class="button">Follow</a>""",unsafe_allow_html=True
                        )
        st.write('---')
        leftcolumn,rightcolum=st.columns(2)
        with leftcolumn:
            st.header("Social Media -Linkedin")
            st.write("""
        🌟 **Attention LinkedIn Professionals!** 🌟

        If you are passionate about technology and interested in connecting with industry peers, let's connect on LinkedIn. I am committed to sharing valuable insights and fostering professional relationships.

        Click the **Connect** button to join me in this professional network. I look forward to engaging with you and exploring opportunities for collaboration.

        See you on LinkedIn! 💼✨
    """)
            st.markdown(f"""<style>.button {{
                                padding: 10px 20px;
                                background-color: #f0f0f0; /* Neutral button background color */
                                border: 2px solid #f0f0f0;
                                border-radius: 10px;
                                color: #39ff14;
                                font-size: 16px;
                                font-weight: bold;
                                cursor: pointer;
                                text-align: center;
                                text-decoration: none;
                                display: inline-block;
                            }}.button:hover {{
                                background-color: #ADD8E6;
                                text-decoration: none;
                                    }}
                            </style><a href="https://www.linkedin.com/in/bolliboinapavansai/" target="_blank" class="button">Follow</a>""",unsafe_allow_html=True
                            )
        with rightcolum:
            st_lottie(ln, speed=1, width=800, height=400, key="ln_animation")
            




            
        
        
        
        