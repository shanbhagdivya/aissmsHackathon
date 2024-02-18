import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="BookHub", page_icon="&#128213;", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
#img_contact_form = Image.open("images/yt_contact_form.png")
#img_lottie_animation = Image.open("images/yt_lottie_animation.png")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hello, we are Team Girl Code :wave:")
    st.title("Book Recommendation System")
    st.write(
        "Welcome to our Machine Learning Project which recommends books on the basis of the selections you make. We are 2nd year students from Symbiosis Institute of Technology."
    )
    st.write("College Website: [Link >](https://www.sitpune.edu.in/)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What we're doing")
        st.write("##")
        st.write(
            """
            This project aims to develop a machine learning model that predicts the popularity of books based on two key factors: purchase count and price. The model will be trained to rank books in order of either their purchase count (most popular to least popular) or their price (most expensive to least expensive). This information can be valuable for various stakeholders in the book industry, such as:

Recommender systems: Recommending books to users based on their preferences for price or popularity.
Inventory management: Optimizing stock levels based on predicted demand.
Pricing strategies: Determining optimal pricing based on predicted popularity.
Project Objectives:

Primary objective: 
Build a machine learning model that can accurately predict the order of books based on either purchase count or price.
Secondary objectives:
Compare the performance of models trained on both price and purchase count.
Analyze the factors influencing book popularity beyond price and purchase count.
            """
        )
        #st.write("[YouTube Channel >](https://youtube.com/c/CodingIsFun)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    
    st.write("Looking for a particular book? Find personalized recommendations below:")

    with open("D:/aiml/s4/hackathon/hackathon.py") as f: 
        exec(f.read())

    st.markdown("[Click me...](hackathon.main())")
# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Feedback")
    st.write("##")

    contact_form = """
    <form action="mailto:nandita.singh.btech2022@sitpune.edu.in" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """

    # Display the contact form
    st.markdown(contact_form, unsafe_allow_html=True)

    # Divide the space between the form and an empty column
    left_column, _ = st.columns([3, 1])

    # Display an empty column on the right for spacing
    with left_column:
        st.empty()

