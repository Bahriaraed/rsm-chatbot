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
            concept = matching_row['concepts'].iloc[0]
            definition = matching_row['Content'].iloc[0]
            type_val = matching_row['type'].iloc[0]
            synonyms = matching_row['synonyms'].iloc[0]
            keywords = matching_row['Keywords_Only'].iloc[0]
            response = f"**Concept:** {concept}\n\n*Definition:* {definition}\n\n*Type:* {type_val}\n\n*Synonyms:* {synonyms}\n\n*Keywords:* {keywords}"
            
            # Add a line to indicate the relation between user input and result
            response += f"\n\n**Result based on user input: '{user_input}'**"
        else:
            response = f"No information found for the most similar concept '{most_similar_concept}'."
    else:
        response = f"No similar concepts found for '{user_input}'."
    
    return response

# Define a form to capture user input
def main():
    st.title('Project Risk Management Chatbot')
    st.write('This Chatbot will help you get an idea about your Project Risk management')

    form = st.form(key='my_form')
    user_input = form.text_input('Enter your message here:')
    submit_button = form.form_submit_button('Send')

    if submit_button:
        user_message = user_input.strip().lower()
        if user_message:
            st.text("You: " + user_input)
            bot_response = get_section(user_message)
            
            # Formatting the bot response for better readability
            bot_response = bot_response.replace('[', '').replace(']', '').replace("'", "").replace(",", ", ")
            bot_response = bot_response.replace('Concept:', '\nConcept:').replace('Definition:', '\nDefinition:')
            bot_response = bot_response.replace('Type:', '\nType:').replace('Synonyms:', '\nSynonyms:')
            bot_response = bot_response.replace('Keywords:', '\nKeywords:')
            st.text("Chatbot: ")
            st.write(bot_response)

if __name__ == "__main__":
    main()