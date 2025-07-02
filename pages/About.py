import streamlit as st

st.markdown("""
### About this platform  

+ **Digital Teaching & Learning Archive:** This web platform is designed to archive and share classroom materials by semester for English Education majors. It hosts a variety of applications created to support both class instruction and student learning, tailored to the learning process and individual learner levels.

+ **Beyond accessing materials, this platform also reflects a broader goal:** encouraging future English teachers to explore how basic Python coding and web-based tools like Streamlit can be used to design customized, learner-centered applications. Through hands-on experience, students gain digital literacy skills essential for innovative and effective teaching in today’s classrooms.
""")

# Custom CSS for the styled button
st.markdown("""
    <style>
    .orange-button {
        display: inline-block;
        padding: 0.5em 1em;
        border: 2px solid orange;
        background-color: white;
        color: orange;
        font-weight: bold;
        text-align: center;
        text-decoration: none;
        border-radius: 5px;
        cursor: pointer;
        transition: 0.3s;
    }
    .orange-button:hover {
        background-color: orange;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Define the target URL
target_url = "https://englishedu.gnu.ac.kr"  # Replace with your desired link

# Create the button with link
st.markdown(f"""
    <a href="{target_url}" target="_blank">
        <div class="orange-button">Go to GNU English Education Website</div>
    </a>
""", unsafe_allow_html=True)
