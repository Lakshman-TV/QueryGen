import streamlit as st
import google.generativeai as genai

# Configure Google API Key
GOOGLE_API_KEY = "AIzaSyAU2j7K1c30QPbhCawAJrFtTBegBhb8uTk"
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize Generative Model
model = genai.GenerativeModel('gemini-pro')

# Main function to define UI
def main():
    # Set page configuration
    st.set_page_config(page_title="AI Query Generator", page_icon=":robot:")

    # Title and Description with emoji
    st.markdown(
        """
        <div style="text-align:center;">
            <h1>SQL Query Generator 🤖</h1>
            <h3>Generate SQL for your database 💡</h3>
            <p>This tool allows you to generate SQL queries based on your prompts. 🚀</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Text input area for user query
    text_input = st.text_area("Enter your query in plain English:")

    # Button to trigger query generation
    submit = st.button('Generate SQL Query')

    if submit:
        with st.spinner("Generating SQL Query..."):
            # Template for query generation
            template = """
                create a SQL query snippet using the below text:

                {text_input}

                I just want a SQL Query.
            """
            formatted_template = template.format(text_input=text_input)

            # Generate SQL query
            response = model.generate_content(formatted_template)
            sql_query = response.text.strip()

            # Display SQL query
            with st.expander("Generated SQL Query 💻", expanded=True):
                st.code(sql_query, language="sql")

            # Expected output template
            expected_output = """
                What would be the expected response of this SQL Query snippet:

                {sql_query}

                Provide sample tabular response with no explanation:
            """
            expected_output_formatted = expected_output.format(sql_query=sql_query)

            # Generate expected output
            eoutput = model.generate_content(expected_output_formatted).text

            # Display expected output
            with st.expander("Expected Output 📊", expanded=True):
                st.markdown(eoutput, unsafe_allow_html=True)

            # Explanation template
            explanation = """
                Explain this SQL Query:

                {sql_query}

                Please provide simplest of explanation.
            """
            explanation_formatted = explanation.format(sql_query=sql_query)

            # Generate explanation
            explanation_text = model.generate_content(explanation_formatted).text

            # Display explanation
            with st.expander("Explanation ℹ️", expanded=True):
                st.markdown(explanation_text, unsafe_allow_html=True)

# Run main function
if __name__ == "__main__":
    main()
