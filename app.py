import streamlit as st

# Title
st.set_page_config(page_title="College Assistant", page_icon="🎓")

st.title("🎓Loyola College AI Assistant ")
st.write("Ask anything about your college 👇")

# Study data (ALL KEYS IN lowercase)
study_notes = {
    "hello": "Hello! I am your college assistant bot. How can I help you today?",
    "hi": "Hi there! What college info are you looking for?",
    "admission": "Admission processes usually start in May.",
    "courses": "We offer B.Sc, B.A, B.Com, and B.Tech courses.",
    "exam": "Final exams are in the third week of November.",
    "fees": "Fees depend on the course.",
    "library": "Library is open from 8 AM to 8 PM.",
    "hostel": "Hostel is available on a first-come basis.",
    "faculty": """ 
Mr. S. Samual – Computer Lecturer & NCC CTO.

Mr. B. Sujith Kumar – Programming expert, choreographer, social media admin.

Mr. L. Karthik – Friendly teaching style, social media admin.

Mrs. D. Himaja – Teaching programming, DB, OS since 2017,SASA.
""",
"fee structure": """
B.Sc computer science – 15,000 only.

B.Sc data science – 15,000 only.

B.Sc quantum technology – 15,000 only.

Students are eligible for scholarships.
""",
# Study data (ALL KEYS IN lowercase)
    # Your Questions
    "what activities are available in your college": "Our college offers real-time project-based learning with an advanced computing lab. Students also participate in sports, NCC, NSS, and cultural activities.",

    "what type of learning environment does your college provide": "The college provides a real-time project-based learning environment with advanced computing labs.",

    "who is the hod of your department": "Mr. M. Ramana Reddy is the HOD of Computational Sciences.",

    "since when has the hod been serving": "He has been serving since 2012.",

    "who is mrs d himaja": "Mrs. D. Himaja is a Computer Lecturer serving since 2017.",

    "what are the timings of the library": "The library is open from 8 AM to 8 PM.",

}

# Function
def get_answer(user_input):
    return study_notes.get(user_input.lower().strip(), "❌ Sorry! I don't know that yet.")

# Input box
user_input = st.text_input("💬 Enter your question:")

# Button
if st.button("Ask"):
    if user_input:
        answer = get_answer(user_input)
        st.success(answer)
    else:
        st.warning("Please enter a question!")

# Sidebar
st.sidebar.title("📌 Available Topics")
for topic in study_notes.keys():
    st.sidebar.write("•", topic)