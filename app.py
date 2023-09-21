import streamlit as st
import sqlite3
import pandas as pd
from Curr_User_Fun import Current_User as CU
from GetTableSchema import get_table_schema as gts

st.title('CM DataChat App')
#curr_user=st.write(st.experimental_user['email'])
curr_user=st.experimental_user['email']
st.write(CU(curr_user))


# Open Ai Test To SQL Generate
openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

input="Create a Snowflake query for top 5 customers by maximum total invoice."

dialect="SQL"

few_shot_examples="""Select col1,col2
from tabl t1 join tabl2 t2 on t1.col1=t2.col2
Where t1.col
Group By t1.Col1
Order By t2.Col1;"""

TableSchema = gts()

Prompt = f"""Given an input question, first create a syntactically correct {dialect} query to run, then look at the results of the query and return the answer.
Use the following format:

SQLQuery: "SQL Query to run"

Only use the following tables:

{TableSchema}.

Some examples of SQL queries that corrsespond to questions are:

{few_shot_examples}

Question: {input}"""

# response = openai.ChatCompletion.create(
#   model="gpt-3.5-turbo",
#   messages = [{"role": "user", "content": Prompt}],
#   temperature=0,
#   max_tokens=300
# )

def generate_response(input_text):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    st.info(llm(input_text))

with st.form('my_form'):
    text = st.text_area('Enter text:', ' ')
    submitted = st.form_submit_button('Submit')
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(Prompt)
