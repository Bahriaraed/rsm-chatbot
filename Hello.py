import streamlit as st
import pandas as pd
from fuzzywuzzy import process


file_path = "output_df_final.csv"
data = pd.read_csv(file_path)


# Function to extract sections based on the concept
def get_section(user_input):
    # Use fuzzy matching to find similar concepts
    concepts = data['Content'].tolist()
    similar_concepts = process.extract(user_input, concepts, limit=5)  # Adjust limit as needed

    # Retrieve information for the most similar concept found
    if similar_concepts:
        most_similar_concept = similar_concepts[0][0]
        matching_row = data[data['Content'] == most_similar_concept]
        if not matching_row.empty:
            Chapter_Name = matching_row['Chapter_Name'].iloc[0]
            Sub_chapter_Name = matching_row['Sub_chapter_Name'].iloc[0]
            Sub_sub_chapter_Name = matching_row['Sub_sub_chapter_Name'].iloc[0]
            synonyms = matching_row['synonyms'].iloc[0]
            concept = matching_row['concepts'].iloc[0]
            definition = matching_row['Content'].iloc[0]
            type_val = matching_row['type'].iloc[0]
            synonyms = matching_row['synonyms'].iloc[0]
            keywords = matching_row['Keywords_Only'].iloc[0]
            response = f"Concept: {concept}\nDefinition: {definition}\nType: {type_val}\nSynonyms: {synonyms}\nKeywords: {keywords}"
        else:
            response = f"No information found for the most similar concept '{most_similar_concept}'."
    else:
        response = f"No similar concepts found for '{user_input}'."
    
    return response

# Define a form to capture user input
form = st.form(key='my_form')
user_input = form.text_input('Enter your message here:')
submit_button = form.form_submit_button('Send')

# Handle form submission
if submit_button:
    user_message = user_input.strip().lower()  # Convert input to lowercase and remove leading/trailing spaces
    if user_message:
        # Display user input
        st.text("You: " + user_input)
        # Get response based on user input compared to the 'concept' column
        bot_response = get_section(user_message)
        # Display chatbot response
        st.text("Chatbot: " + bot_response)

# Add a footer or any additional content as needed
st.markdown('---')
st.write('This Chatbot will help you get an idea about your Project Risk management')
