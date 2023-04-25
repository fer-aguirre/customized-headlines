import streamlit as st
import pandas as pd
import numpy as np
import openai
import pinecone
import configparser

# Create a parser object and disable interpolation
parser = configparser.ConfigParser(interpolation=None)

# Read data from 'config.ini' file
parser.read("./config.ini")

# Access sections from the configuration file
parser.sections()

# Get 'key' from openai section
openai_key = parser.get('openai', 'key')

# Set up OpenAI API key
openai.api_key = openai_key

# Get 'key' from pinecone section
pinecone_key = parser.get('pinecone', 'key')

index_name = 'semantic-search-openai'

# initialize connection to pinecone
pinecone.init(
    api_key=pinecone_key,
    environment="asia-southeast1-gcp"  # find next to api key in console
)

# connect to index
index = pinecone.Index(index_name)

# Title
st.title('Títulos Personalizados')

edad = st.selectbox(
    '¿Cuál es tu rango de edad?',
    ('10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80-89', '90-99'))

genero = st.selectbox(
    '¿Cómo te identificas?',
    ('Mujer', 'Mujer trans', 'Hombre', 'Hombre trans', 'No binarie', 'Otro'))

pais = st.text_input('¿En qué país resides?', '')

opciones_topicos = [
    'Entretenimiento', 
     'Deportes', 
     'Cultura', 
     'Política', 
     'Tecnología', 
     'Ciencia', 
     'Arte', 
     'Salud', 
     'Negocios', 
     'Medio Ambiente'
     ]

topicos = st.multiselect(
    'Elige los temas de tu interés:',
    opciones_topicos,
)

if st.button('Generar ejemplos'):
    embeddings = []
    for i in range(len(topicos)):
        emb = openai.Embedding.create(input=topicos[i], engine="text-embedding-ada-002")['data'][0]['embedding']
        embeddings.append(emb)

    user_model = np.mean(embeddings, axis=0).tolist()

    res = index.query([user_model], top_k=3, include_metadata=True)

    texts = []
    original_titles = []
    for match in res['matches']:
        texts.append(match['metadata']['content'][1])
        original_titles.append(match['metadata']['content'][0])
    st.write(original_titles)

    # suggestions = []
    # for text in texts:
    #     response = openai.Completion.create(
    #         model="text-davinci-003",
    #         prompt=f"""
    #                 Considera un usuario lector que se identifica como {genero} en un rango de edad de {edad} años, que reside en {pais} y le interesan {topicos}. 
    #                 Basado en estos datos, tu objetivo es generar un título de noticias breve y conciso que resulte atractivo para ese usuario con el contenido del siguiente texto. 
    #                 No añadas información del usuario en el título.

    #                 Input:{text}

    #                 Output:""",
    #         temperature=0.8,
    #         max_tokens=50,
    #         top_p=1,
    #         frequency_penalty=0,
    #         presence_penalty=0,
    #         stop=["\n"],
    #     )

    #     suggestions.extend(match['text'] for match in response['choices'])
    
    # for i in range(len(suggestions)):
    #     st.markdown(f"Título original: :red[{original_titles[i]}]\n Título generado: :green[{suggestions[i]}]\n")
