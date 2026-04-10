import streamlit as st
import math
# -------------------------------
# PAGE CONFIG
# -------------------------------
# -------------------------------
# CUSTOM UI
# -------------------------------
st.markdown("""
    <style>
    body {
        background-color: #fafafa;
    }
    .stChatMessage {
        border-radius: 15px;
        padding: 10px;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)
# -------------------------------
# LOGIN SYSTEM
# -------------------------------
users = {
    "loyola": "loyola123",
    "student": "loyola123"
}

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.header("Welcome to Loyola CS Digital Assistant")
    st.subheader("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in users and users[username] == password:
            st.session_state.logged_in = True
            st.success("Login successful!")
            st.rerun()
        else:
            st.error("Invalid username or password")

    st.stop()
# -------------------------------
# CUSTOM UI (ChatGPT style)
# -------------------------------
st.markdown("""
<style>
.main {
    background-color: #0e1117;
}
.stChatMessage {
    padding: 12px;
    border-radius: 10px;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# SIDEBAR (like ChatGPT)
# -------------------------------
with st.sidebar:

    st.markdown('<div class="sidebar-title">⚙️ Menu</div>', unsafe_allow_html=True)

    if st.button(" Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")

    st.markdown('<div class="sidebar-title">📌 Topics</div>', unsafe_allow_html=True)

    topics = [
        "Faculty", "Fees", "Courses",
        "Library", "Hostel", "Admission",
        "Principal", "HOD", "Scholarships"
    ]

    for t in topics:
        if st.button(t):
            st.session_state.quick_question = t.lower()

# -------------------------------
# DATA
# -------------------------------
study_notes = {
    "hello": "Hello! I am your college assistant bot. How can I help you today?",
    "hi": "Hi there! What college info are you looking for?",
    "creator":"""<span style='color:red; font-weight:bold;'>THIS APPLICATION WAS DEVELOPED BY ME</span> I’m a student currently studying in loyola college ysrr. I’m really interested in coding and technology, especially Python. I enjoy building projects like chatbots and AI-based apps. I like learning new things and improving my skills little by little.I developed an AI-powered college assistant application using Python and the Streamlit framework. The application provides information about various academic and administrative aspects such as faculty details, fee structure, admission guidelines, scholarships, and eligibility criteria.

The system features an interactive chat-based interface inspired by ChatGPT, allowing users to input queries and receive relevant responses instantly. Additionally, I enhanced the user experience by incorporating features like dynamic content display, highlighted text formatting, and image integration for faculty profiles.

This project demonstrates my skills in Python programming, UI design using Streamlit, and basic natural language processing techniques for handling user queries.
""",
    "admission": """
<h3>📌 Admission Guidelines</h3>

Loyola Degree College, affiliated to 
<b>Yogi Vemana University (YVU), Kadapa</b>, follows a 
<span style='color:#00ffcc; font-weight:bold;'>transparent, merit-based, and student-friendly</span> 
admission process.

<hr>

<h4>📋 General Guidelines</h4>

<ul>
<li><b>Eligibility:</b> Must meet YVU academic requirements</li>
<li><b>Application:</b> Online & Offline modes available</li>
<li><b>Selection:</b> Merit-based + Govt reservation policy</li>
<li><b>Documents:</b> Academic records, TC, certificates</li>
<li><b>Reservation:</b> As per Andhra Pradesh Govt norms</li>
<li><b>Code of Conduct:</b> Discipline & integrity required</li>
<li><b>Scholarships:</b> Financial support for deserving students</li>
<li><b>Jesuit Preference:</b> Support for underprivileged students</li>
</ul>

<hr>

<h4>🌟 Vision</h4>
To provide equitable and transparent admission opportunities aligned with YVU norms.

<h4>🎯 Mission</h4>
<ul>
<li>Ensure fair and merit-based admissions</li>
<li>Support marginalized communities</li>
<li>Guide students and parents clearly</li>
<li>Promote holistic student development</li>
<li>Follow university & government policies</li>
</ul>

<h4>💡 Taglines</h4>
<ul>
<li>“Admissions with Transparency, Education with Integrity”</li>
<li>“Equal Opportunities, Inclusive Education”</li>
<li>“Empowering Students, Enriching Futures”</li>
<li>“Fair Access to Quality Education”</li>
</ul>
""",
"eligibility": """
<h3>🎓 Eligibility Criteria</h3>

Loyola Degree College welcomes students who have successfully completed their 
<b>Intermediate (10+2)</b> education from a recognized board. Admissions follow 
<b>APSCHE guidelines</b> for web counselling and merit-based selection.

<h4>📘 Course-Wise Eligibility</h4>

<b>1. Computer Science:</b><br>
Students must have studied <span style='color:#00ffcc;'>Mathematics (MPC)</span>.<br><br>

<b>2. Life Sciences / B.Sc (Biology):</b><br>
Students should have completed <span style='color:#00ffcc;'>BiPC</span>.<br><br>

<b>3. Commerce Courses (B.Com):</b><br>
Students from <span style='color:#00ffcc;'>CEC or MEC</span> streams.<br><br>

<b>4. BBA:</b><br>
Open to <span style='color:#00ffcc;'>CEC or MEC</span> students.<br><br>

<b>5. Arts / Humanities:</b><br>
Students from <span style='color:#00ffcc;'>any stream</span> are eligible.<br><br>

<hr>

<h4>🌟 Vision</h4>
To provide equitable access to quality higher education and foster holistic learning.

<h4>🎯 Mission</h4>
<ul>
<li>Follow APSCHE & University guidelines</li>
<li>Provide clear course guidance</li>
<li>Ensure merit-based admissions</li>
<li>Help students choose right career path</li>
<li>Build confidence in higher education journey</li>
</ul>

<h4>💡 Taglines</h4>
<ul>
<li>“Eligibility Meets Opportunity at Loyola”</li>
<li>“Right Course, Bright Future”</li>
<li>“Your Stream, Your Strength, Your Success”</li>
<li>“Guiding You from Eligibility to Excellence”</li>
<li>“Merit-Based Access, Holistic Learning”</li>
</ul>
""",
"scholarships": """
<h3>🎓 Scholarship & Financial Support</h3>

Loyola Degree College is deeply committed to the <b>Jesuit tradition</b> of serving 
the poor and the marginalized.

In addition to <b>government scholarships</b>, the Management provides 
<span style='color:#00ffcc; font-weight:bold;'>financial aid and fee concessions</span> 
to ensure that <b>no deserving student is deprived of education</b> due to financial hardship.

This reflects Loyola vision of 
<b>inclusive and value-based education</b>, empowering students from underprivileged 
backgrounds to pursue their dreams with dignity.

<hr>

<h4>🌟 Vision</h4>
To ensure that every deserving student, regardless of financial background, 
has access to quality education and the opportunity to succeed.

<h4>🎯 Mission</h4>
<ul>
<li>Provide scholarships to deserving students</li>
<li>Bridge financial and academic gaps</li>
<li>Promote inclusivity in education</li>
<li>Support Jesuit value: <b>“option for the poor”</b></li>
<li>Build confident and responsible leaders</li>
</ul>

<h4>💡 Taglines</h4>
<ul>
<li>“Education for All, Support for the Needy”</li>
<li>“No Dream Too Distant, No Student Left Behind”</li>
<li>“Bridging Financial Gaps, Building Bright Futures”</li>
<li>“Compassion in Action, Education with Inclusion”</li>
</ul>
""",
 "courses": "We offer B.Sc, B.A and B.Com courses with single major.",
    "exam": "Final exams are in the third week of November.",
    "fees": "Fees depend on the course.",
    "library": "Library is open from 8 AM to 8 PM.",
    "hostel": "Hostel is available on a first-come basis.",
    # Faculty data (ALL KEYS IN lowercase)
    "faculty": """ 
<span style='color:red; font-weight:bold;'>SAMULURU SAMUEL</span>Mr. S. Samual – Computer Lecturer & NCC CTO.<br>
Technical skills:
• SQL
• C
• C++
• Java
• HTML,CSS
Strengths:
• Quick learner
• Good at communication
• Critical Thinking
• Versatility
Hobbies:
• Playing Sports
• Browsing social media
• Watching movies & Series
• Listening music
Personal details:
Name : S.Samuel
Father Name : S.Simon
Mother Name : S.Vimala
Marital status : Unmarried
Languages known : English and Telugu
Address : 2-2-257,
Christian line,
Pulivendula,
Y.S.R.Kadapa (dist), 516390(A.P).

<span style='color:red; font-weight:bold;'>Mr.B. SUJITH KUMAR</span> – Programming expert, choreographer, social media admin.<br>
Professional Experience :
 Worked as assistant professor in ANNAMACHARYA PG College of Computer
Studies, Rajampet
 Worked as XML developer in MRV IT SOLUTIONS.
Technical Profiency:
 WEB DEVELOPMENT
 MACHINE LEARNING PROJECTS
 C, JAVA, PYTHON PROGRAMMING LANGUAGES
 MS-OFFICE
Professional Activites:
 R&D incharge in APGCCs college-rajampet.
 Culture coordinator at the university level.
List of Publications:
 Paper titled “Detectiong fake identities on Instagram” at IJSRT in 2023.
 Paper titled “Emotion-based detection of mental health risk in social meia” at
IJIRSET in 2025.
Workshops/FPDS/Webinars Attended:
 Attended a faculty development program named “Enterprenuership management”
organized by Wadwani foundation held at JNTUA in march-2025.
Personal Profile
Name : B. SUJITH KUMAR
Date of Birth : 24-06-2001
Gender : MALE
Contact Address : 2-5-249/1, SIYONPURAM,
PULIVENDULA-516390
Languages Knows : ENGLISH, TELUGU

<span style='color:red; font-weight:bold;'>Mr. L. Karthik</span> – Friendly teaching style, social media admin.<br>
Professional Experience :
Technical Profiency:
 WEB DEVELOPMENT
 MACHINE LEARNING PROJECTS
 C, JAVA, PYTHON PROGRAMMING LANGUAGES
 MS-OFFICE
Professional Activites:
List of Publications:
 Paper titled “BINARY MULTILINGUAL MACHINE GENERATOR TEST
DETECCTION” at in 2025.
Workshops/FPDS/Webinars Attended:
Personal Profile
Name : L. KARTHIK
Date of Birth : 3-8-2002
Gender : MALE
Contact Address : 1-10-315, CHRISTIAN
LINE PULIVENDULA516390
Languages Knows : ENGLISH, TELUGU

<span style='color:red; font-weight:bold;'>Mrs. D. HIMAJA</span>– Teaching programming, DB, OS since 2017,SASA.<br>
Professional Experience:
I have been working as the Computer Science lecturer at Loyola Degree College
(YSRR), Pulivendula, from 2017 to the present.
Technical Profiency:
Languages : C, C++, JAVA, Python, Ms-Office
Operating systems : windows XP, 7, 8.1, 10,11
Database : Oracle
Professional Activities:
I have been working as the SASA Coordinator at Loyola Degree College since June
2025.
Workshops/FDPS/Webinars Attended\n
Data Analytics Using Power BI and Tableau Organized by Faculty of IT and CS -Parul
University - Gujarat, Atria Institute of Technology- Karnataka & Amity Pune – Maharashtra
in in Collaboration with ExcelR Edtech Pvt.Ltd. 11th to 15th March 2024
Business Analytics Organized by AISSMS College of Engineering, SJC Institute of Technology
and Matrusri Engineering College in Collaboration with ExcelR Edtech Pvt.Ltd. 5th to 9th Sep
2024
Block Chain Technology Organized by D Y Patil Deemed to be university 8
TH TO 12 Jan
024
Data Visualization using Tableau by MOHAN BABU UNIVERSITY &
EXCELR EDTTECH PVT LTD 16th to 20th Sep2024
Gen-AI and Prompt Engineering Using Microsoft Co-Pilot. By BNM Institute of
Technology Bangalore (BNMIT) – Karnataka,D.Y. Patil Agriculture and
Technical University Talsande – Maharashtra, and Marwadi University Rajkot -
Gujarat in Collaboration with ExcelR Edtech Pvt. Ltd. 15th to B.  19 Nov 2024
Cloud Architect By Vardhaman Engineering College, Shamshabad - Hyderabad,
AVS Engineering College, Salem – Tamil Nadu, 18th-22nd Nov 2024.
Data Visualization Using Tableau By Department of Computer Science and
Engineering, Mohan Babu University, Tirupati, Andhra Pradesh & EXCELR
EDTECH PVT. LTD.1st to 5th April 2024\n
Personal Profile
Name : D. Himaja
Date of Birth : 10-06-1994
Gender : Fe- Male
Contact Address : Peddakondappa Colony -2
pulivendula, YSR Kadapa
Languages Knows : English, Telugu,

""",
"fee structure": """
B.Sc computer science – 15,000 only.

B.Sc data science – 15,000 only.

B.Sc quantum technology – 15,000 only.

Students are eligible for scholarships.
""",
"hod": """
<span style='color:red; font-weight:bold;'>M. Ramana Reddy</span>– Teaching programming, DB, OS since 2017,SASA.<br>M. Ramana Reddy (MCA, MBA) – HOD & Assistant Professor<br>  
Department of Computer Science  
the Department of Computer Science at Loyola Degree College, established a few years ago, is dedicated to training students as techno-savvy professionals equipped with skills for the digital age. The department focuses on building strong foundations in computer systems, programming languages, databases, and emerging technologies that prepare students for higher studies, research, and industry careers.\n
Professional Experience:
I have been working as the Head of the Department of Computer Science at Loyola
Degree College (YSRR), Pulivendula, from August 2021 to the present.
I worked as a Lecturer in Computer Science at Loyola Degree College (YSRR),
Pulivendula, from July 2012 to July 2021.
I served as the Head of the Department of Computer Science at Vivekananda Degree
College, Vempalli, from August 2010 to May 2012.
I worked as an IT Associate at the Institute for Electronic Governance from August
2008 to July 2010.
""",
"principal": """
<span style='color:red; font-weight:bold;'>Prof . Fr. Dr. L. Joji Reddy, S.J. M.Sc., M.B.A., M.Phil., Ph.D., Postdoc.(USA)</span> – Principal, Loyola Degree College.<br>
Loyola Degree College is more than an institution—it is a global centre of learning with world-class facilities and a commitment to excellence in every sphere of life. Our vision goes beyond academics, embracing the all-round development of every student and nurturing in them a lifelong thirst for knowledge. Here, education is not confined to classrooms; it is value-driven, activity-based, and respect-centered, preparing our students to adapt, excel, and lead in any environment. Loyola imparts not only knowledge but also values—by teaching, by example, and by inspiring students to serve the poorest of the poor with compassion and patriotism. In this way, we cultivate visionary leaders who dream fearlessly, live purposefully, and leave behind a legacy for generations to come. As Principal, I am proud to be a Loyolite and to lead our student community as they unravel their true potential and move confidently toward their aspiring, futuristic goals.
""",
# Study data (ALL KEYS IN lowercase)
    # Your Questions
    "what activities are available in your college": "Our college offers real-time project-based learning with an advanced computing lab. Students also participate in sports, NCC, NSS, and cultural activities.",

    "what type of learning environment does your college provi de": "The college provides a real-time project-based learning environment with advanced computing labs.",

    "who is the hod of your department": "Mr. M. Ramana Reddy is the HOD of Computational Sciences.",

    "since when has the hod been serving": "He has been serving since 2012.",

    "who is mrs d himaja": "Mrs. D. Himaja is a Computer Lecturer serving since 2017.",

    "what are the timings of the library": "The library is open from 8 AM to 8 PM.",

}

# -------------------------------
# SMART RESPONSE
# -------------------------------
def get_answer(user_input):
    user_input = user_input.lower()

    # -------------------------------
    # MATH CALCULATIONS
    # -------------------------------
    try:
        # Power support
        user_input = user_input.replace("^", "**")

        # Square root
        if "sqrt" in user_input:
            num = float(user_input.split("sqrt")[-1])
            return f"🧮 Answer: {math.sqrt(num)}"

        # Basic operations
        if any(op in user_input for op in ["+", "-", "*", "/"]):
            result = eval(user_input)
            return f"🧮 Answer: {result}"

    except:
        pass

    # -------------------------------
    # YOUR EXISTING LOGIC
    # -------------------------------
    if "fee" in user_input:
        return study_notes["fee structure"]

    if "scholarship" in user_input:
        return study_notes["scholarships"]

    # Default
    for key in study_notes:
        if key in user_input:
            return study_notes[key]
        
    return "🤖 I’m still learning. Try asking about fees, faculty, or courses."

# -------------------------------
# CHAT MEMORY
# -------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -------------------------------
# TITLE
# -------------------------------
st.markdown("<h2 style='color:#9ca3af;'>Loyola CS Digital Assistant</h2>",
             unsafe_allow_html=True)

# -------------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):

        # show images if exist
        if "images" in msg:
            for img in msg["images"]:
                st.image(img, width=120)

        # show text
        st.markdown(msg["content"], unsafe_allow_html=True)
# -------------------------------
# INPUT (ChatGPT style)
# -------------------------------
user_input = st.chat_input("Ask anything about your college...")

# Handle quick button click
if "quick_question" in st.session_state:
    user_input = st.session_state.quick_question
    del st.session_state.quick_question

# -------------------------------
# RESPONSE FLOW
# -------------------------------
if user_input:
    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    st.chat_message("user").write(user_input)

    # Get answer
    answer = get_answer(user_input)

    # 👉 Decide images
    images = []

    if "hod" in user_input.lower():
        images = ["ramana.jpg"]

    elif "faculty" in user_input.lower():
        images = ["samuel.jpg", "sujith.jpg", "karthik.jpg", "himaja.jpg"]

    elif "principal" in user_input.lower():
        images = ["joji.jpg"]
    
    elif "creator" in user_input.lower():
        images = ["suhel.jpg"] 

    # Save assistant message WITH images
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer,
        "images": images
    })

    # Show immediately
    with st.chat_message("assistant"):
        for img in images:
            st.image(img, width=120)

        st.markdown(answer, unsafe_allow_html=True)