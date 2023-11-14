import streamlit as st

# Placeholder for the chatbot model
chatbot = None

# Streamlit app title
st.title('PRM Chatbot')

# Function to interact with the chatbot
def chat(message):
    if chatbot is None:
        return "Please wait, the model is still loading..."
    else:
        # Pass user input to the chatbot model and get the response
        # Example: response = chatbot.generate_response(message)
        # Replace `generate_response` with your chatbot's response method
        response = "Response from the chatbot goes here."
        return response

# Define a form to capture user input
form = st.form(key='my_form')
user_input = form.text_input('Enter your message here:')
submit_button = form.form_submit_button('Send')

# Execute JavaScript to trigger 'click' on the form submit on Enter key press
st.markdown(
    """
    <script>
    const input = document.querySelector("input");
    input.addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
            document.querySelector("[data-baseweb='button']").click();
        }
    });
    </script>
    """,
    unsafe_allow_html=True,
)

# Handle form submission
if submit_button:
    user_message = user_input
    if user_message:
        # Display user input
        st.text("You: " + user_message)
        # Get chatbot response
        bot_response = chat(user_message)
        # Display chatbot response
        st.text("Chatbot: " + bot_response)

# Add a footer or any additional content as needed
st.markdown('---')
st.write('This Chatbot will help you get an idea about you Project Risk')
