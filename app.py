import pandas as pd
import streamlit as st
import pickle
import re
import os

# -------- PAGE CONFIG -------- #
st.set_page_config(
    page_title="Phishing Detection App",
    page_icon="🛡️",
    layout="centered"
)


# -------- LOAD MODEL -------- #
with open("model/phishing_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("model/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)


# -------- TEXT CLEANING FUNCTION -------- #
def clean_text(text):
    text = text.lower()
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


# -------- CLEAN PROFESSIONAL STYLE -------- #
st.markdown("""
    <style>
        html, body, [class*="css"]  {
            font-family: 'Times New Roman', serif;
        }

        .stApp {
            background-color: #f8f0f6;
            color: black;
        }

        .main {
            background-color: white;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0px 4px 20px rgba(0,0,0,0.05);
            color: black;
        }

        h1, h2, h3, h4, h5, h6 {
            color: #d63384;
            font-weight: bold;
        }

        p, label, div {
            color: black !important;
            font-weight: 500;
        }

        .stButton>button {
            background-color: #d63384;
            color: white;
            font-weight: bold;
            border-radius: 10px;
        }

        .stSidebar {
            background-color: #f3d9e5;
        }

        footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)
st.markdown("""
    <style>
        /* Hide the three-dot main menu */
        #MainMenu {
            visibility: hidden;
        }

        /* Keep deploy button visible */
        button[title="Share"] {
            visibility: visible !important;
        }
             <style>
        /* Make Deploy (Share) button bold and larger */
        button[title="Share"] {
            font-weight: bold !important;
            font-size: 16px !important;
            color: white !important;
            background-color: #d63384 !important;
            border-radius: 8px !important;
        }
    </style>
    </style>
""", unsafe_allow_html=True)

# -------- SIDEBAR -------- #
st.sidebar.title("🌸 Navigation")

section = st.sidebar.radio(
    "Go to:",
    ["🔐 Email Detector", "👩‍💻 About Developer", "📌 About Project"]
    
)

# -------- MAIN CONTENT -------- #
if section == "🔐 Email Detector":

    st.markdown("""
<h1 style='text-align:center; font-family:"Times New Roman", serif; font-weight:bold; margin-bottom:0.2rem;'>🛡️ Phishing Email Detection System</h1>
<p style='text-align:center; font-family:"Times New Roman", serif; font-size:18px; color:black; margin-top:0;'>Smart AI system to detect phishing emails using Machine Learning</p>
""", unsafe_allow_html=True)

    email_input = st.text_area("📧 Paste Email Content Below:", height=200)

    if st.button("🔍 Analyze Email"):
        if email_input.strip() == "":
            st.warning("Please enter email content.")
        else:
            cleaned = clean_text(email_input)
            vectorized = vectorizer.transform([cleaned])
            prediction = model.predict(vectorized)[0]

            if prediction == 1:
                st.error("⚠️ This email is PHISHING email.")
            else:
                st.success("✅ This is a SAFE email..")


elif section == "👩‍💻 About Developer":

    st.title("👩‍💻 About The Developer Shravani")

    st.write("""
    AI Instructor | Cybersecurity Enthusiast |  

I’m passionate about **building intelligent systems** that enhance digital security and help people protect themselves from cyber threats.  
             
Some things about me as a developer:  
             
- 💻 Experienced in **Python, Machine Learning, and Data Analysis**  
- 🛡️ Strong interest in **cybersecurity, phishing detection, and ethical hacking**  
- 🎓 Love teaching and guiding students in understanding **AI and security concepts**  
- 📈 Constantly exploring **new tools, frameworks, and best practices** in the tech world  
- 🎨 Enjoy combining **technical skills with creativity** to make projects both functional and attractive  
- 🚀 Believe in **hands-on learning** — every project I build is meant to **solve real problems** 
              
I enjoy turning **ideas into practical applications**, building small AI/ML tools, and sharing knowledge with the community.
             
    """)

    st.markdown("### 🔗 Connect with me:")
    st.markdown("[LinkedIn](https://www.linkedin.com/in/shravani-khanvilkar/)")
    st.markdown("[GitHub](https://github.com/Shravani924)")


elif section == "📌 About Project":

    st.title("📌 About This Project")

    st.write("""
The **Phishing Email Detection System** is a machine learning-powered application designed to **protect users from phishing attacks**.  

This phishing detection system uses:
    
- Text preprocessing & cleaning
- TF-IDF vectorization for text representation
- Logistic Regression classifier
- Evaluation using accuracy, precision, recall, and F1-score
- Achieves very high classification accuracy on the test set
**Purpose:**  
To provide a practical demonstration of how **ML can enhance cybersecurity**, detect suspicious emails, and raise awareness about phishing.  
**Tech Stack:** Python, Pandas, Scikit-Learn, Streamlit, Git/GitHub for version control, pickle for model serialization.
    
    The model analyzes textual patterns and predicts whether
    an email is safe or phishing.
    """)
 # ------------------- Feedback Box BELOW About Project -------------------
    st.subheader("💌 Feedback / Suggestions")
    import pandas as pd
    import os

    feedback_text = st.text_area("Share your thoughts, suggestions, or report any issues here:")

    if st.button("Submit Feedback"):
        if feedback_text.strip() == "":
            st.warning("Please write something before submitting.")
        else:
            feedback_file = "feedback.csv"
            write_header = not os.path.exists(feedback_file)
            df = pd.DataFrame([[feedback_text]], columns=["Feedback"])
            df.to_csv(feedback_file, mode="a", index=False, header=write_header)
            st.success("Thank you! Your feedback has been saved 😊")

# -------- FOOTER -------- #
st.markdown("---")
st.markdown(
    "<center>© 2026 | Made with ❤️ using Streamlit by Shravani</center>",
    unsafe_allow_html=True
)
