import streamlit as st

st.set_page_config(
    page_title="Mental Health in Tech - EDA App",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Conclusions")

st.markdown("""
This section provides an overview of the app and its purpose.
""")


# Convert markdown points into bullet points
conclusions = [
    "**Mental health concerns are prevalent in the tech industry.** A significant portion of survey respondents reported mental health challenges and sought treatment.",
    "**Gender and age play a role in mental health treatment.** Women and individuals in specific age groups were more likely to seek help compared to their counterparts.",
    "**Family history of mental health conditions appears to correlate with seeking treatment.** This suggests a potential genetic or environmental influence on help-seeking behaviors.",
    "**Company size and location may impact mental health treatment rates.** Certain company sizes and countries exhibited higher or lower rates of treatment compared to others.",
    "**The ease of taking leave for mental health issues can influence the likelihood of seeking treatment.** Supportive workplace policies are crucial for encouraging help-seeking behaviors.",
    "**Mental health interviews during the hiring process may deter individuals from disclosing their mental health conditions.** This could potentially impact their willingness to seek help in the future.",
    "**Supervisor support and positive workplace culture are crucial for promoting mental health and well-being in the tech industry.** These factors are associated with treatment-seeking behaviors.",
    "**The correlation between mental and physical health consequences underscores the importance of a holistic approach to employee well-being.** Addressing both physical and mental health concerns is essential for overall well-being.",
]

for conclusion in conclusions:
    st.markdown(f"- {conclusion}")