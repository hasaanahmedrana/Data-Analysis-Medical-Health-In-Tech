import streamlit as st

st.set_page_config(
    page_title="Mental Health in Tech - EDA App",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

import streamlit as st


def app_overview():
    st.title("Overview")

    st.header("Welcome to the Exploratory Data Analysis (EDA) of Mental Health in Tech")
    st.write("""
    This application provides a comprehensive exploration of data related to mental health in the technology sector. 
    Mental health is a crucial topic, especially in the high-pressure environment of the tech industry, where long 
    hours, tight deadlines, and the rapid pace of innovation can take a significant toll on individuals' well-being. 
    This EDA aims to shed light on various aspects of mental health in tech, including factors influencing it, trends, 
    and actionable insights.
    The DataSet Used for the analysis is the [OSMI Mental Health in Tech Survey](https://www.kaggle.com/datasets/osmi/mental-health-in-tech-survey/data).
    """)

    st.subheader("Objectives")
    st.write("""
    - **Understand Patterns:** Analyze data to uncover trends and patterns related to mental health in the tech industry.
    - **Identify Key Factors:** Explore the impact of workplace culture, accessibility of mental health resources, 
      and societal attitudes on mental health.
    - **Enable Decision Making:** Provide insights that can guide employers, policymakers, and employees in improving 
      mental health support.
    """)

    # st.subheader("Key Features")
    # st.write("""
    # - **Basic Analysis:** Explore descriptive statistics to understand the overall distribution and nature of the data.
    # - **Trend Analysis:** Discover changes over time, highlighting emerging trends in mental health awareness and support.
    # - **Outlier and Missing Value Handling:** Ensure data quality by addressing anomalies and gaps.
    # - **Feature Engineering:** Create new metrics and features to enhance analysis and predictive capabilities.
    # - **Machine Learning Integration:** Use predictive models to identify individuals or groups at higher risk for
    #   mental health challenges.
    # - **Interactive Visualizations:** Engage with the data through dynamic charts, graphs, and filters.
    # """)
    #
    # st.subheader("Methodology")
    # st.write("""
    # 1. **Data Cleaning:** Initial processing to remove inconsistencies and prepare the dataset for analysis.
    # 2. **Exploratory Analysis:** Comprehensive exploration of data using visualizations and statistical methods.
    # 3. **Insights Generation:** Extract actionable insights based on findings from the analysis.
    # 4. **Modeling:** Apply machine learning techniques to predict outcomes and test hypotheses.
    # 5. **Presentation:** Use Streamlit to create an intuitive, interactive platform for presenting results and engaging users.
    # """)

    st.subheader("Why Mental Health in Tech?")
    st.write("""
    The tech industry is both unique and demanding. Employees often face challenges such as:
    - Intense work schedules.
    - Isolation due to remote work or non-collaborative environments.
    - Lack of access to mental health resources or stigmatization of seeking help.

    By focusing on this sector, we aim to address a critical area of concern and contribute to the growing conversation 
    around mental health in the workplace.
    """)

    st.subheader("Insights You Can Expect")
    st.write("""
    - Prevalence of mental health issues across demographics.
    - Workplace factors influencing mental well-being.
    - Trends in mental health awareness and support over time.
    - Recommendations for improving workplace mental health policies.
    """)


    st.subheader("Call to Action")
    st.write("""
    Mental health in the tech industry is a shared responsibility. Use the insights from this EDA to:
    - Advocate for better mental health policies.
    - Foster a more supportive workplace culture.
    - Encourage conversations about mental well-being in professional settings.

    Together, we can create a healthier, more inclusive tech industry for all.
    """)
app_overview()
