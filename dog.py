import streamlit as st

# Set page title
st.set_page_config(page_title="Dog Year Greeting", page_icon=":dog:", layout="wide")

# Define page layout
def page_layout():
    # Define header section
    st.write("<div style='background-color: #00bfff; padding: 1rem 2rem;'><h1 style='color: #ffffff; text-align: center;'>Dog Year Greeting</h1></div>", unsafe_allow_html=True)

    # Define main section
    st.write("<h2 style='text-align: center;'>Enter your name and age:</h2>", unsafe_allow_html=True)
    name = st.text_input("Name")
    age = st.slider("Age", min_value=0, max_value=100, value=18)

    # Calculate age in dog years
    dog_age = age * 7

    # Display greeting
    st.write(f"<h3 style='text-align: center;'>Hi {name}, you are {age} years old, which is {dog_age} in dog years!</h3>", unsafe_allow_html=True)

    # Add some styling
    st.markdown("---")
    st.write("<p style='text-align: center; color: #000000;'>© 2023 Dog Year Greeting</p>", unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    page_layout()
