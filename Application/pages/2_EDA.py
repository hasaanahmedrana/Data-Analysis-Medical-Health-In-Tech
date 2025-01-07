import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.set_page_config(
    page_title="Mental Health in Tech - EDA App",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)


# Load the data
data_path = r"C:\\Users\\HP\\Data-Analysis-Medical-Health-In-Tech\\data.csv"  # Adjust the path as needed
df = pd.read_csv(data_path)

# Sidebar options
st.sidebar.title("EDA Options")
visualization_choice = st.sidebar.selectbox(
    "Choose a Visualization:",
    [
        "Age Distribution",
        "Gender Distribution",
        "Top Countries",
        "Mental Health Treatment by Gender",
        "Age Distribution by Treatment and Gender",
        "Treatment vs. Family History",
        "Work Interfere Distribution",
        "Seek Help Distribution",
        "Ease of Leave vs Treatment",
    ]
)

# Age Distribution
if visualization_choice == "Age Distribution":
    bins = list(range(20, 71, 5)) + [float("inf")]
    labels = [f"{i}-{i+4}" for i in range(20, 70, 5)] + ["70+"]
    df["Age Group"] = pd.cut(df["Age"], bins=bins, labels=labels, right=False)
    fig = px.histogram(df, x="Age Group", title="Age Distribution in 5-Year Intervals")
    fig.update_layout(xaxis_title="Age Group", yaxis_title="Count")
    st.plotly_chart(fig)

# Gender Distribution
elif visualization_choice == "Gender Distribution":
    gender_counts = df["Gender"].value_counts().reset_index()
    gender_counts.columns = ["Gender", "Count"]
    fig = px.pie(
        gender_counts,
        names="Gender",
        values="Count",
        title="Gender Distribution",
        color_discrete_sequence=["Blue", "#FC0FC0", "Yellow"],
    )
    fig.update_traces(textposition="inside", textinfo="percent+label")
    st.plotly_chart(fig)

# Top Countries
elif visualization_choice == "Top Countries":
    country_count = df["Country"].value_counts().head(15).reset_index()
    country_count.columns = ["Country", "Count"]
    fig = px.bar(
        country_count,
        x="Country",
        y="Count",
        text="Count",
        title="Top 15 Countries",
        color="Count",
        color_continuous_scale="Blues",
    )
    fig.update_traces(texttemplate="%{text:.1f}", textposition="outside")
    fig.update_layout(xaxis_title="Country", yaxis_title="Count", template="simple_white")
    st.plotly_chart(fig)

# Mental Health Treatment by Gender
elif visualization_choice == "Mental Health Treatment by Gender":
    fig = px.histogram(
        df,
        x="Gender",
        color="Treatment",
        barmode="group",
        title="Mental Health Treatment by Gender",
    )
    fig.update_layout(
        xaxis_title="Gender",
        yaxis_title="Count",
        legend_title="Treatment",
        template="simple_white",
    )
    st.plotly_chart(fig)

# Age Distribution by Treatment and Gender
elif visualization_choice == "Age Distribution by Treatment and Gender":
    fig = px.violin(
        df,
        y="Age",
        x="Treatment",
        color="Gender",
        box=True,
        points="all",
        title="Age Distribution by Treatment and Gender",
        labels={"Age": "Age", "Treatment": "Treatment", "Gender": "Gender"},
    )
    fig.update_layout(
        title_font_size=20,
        xaxis_title="Treatment",
        yaxis_title="Age",
        legend_title="Gender",
        template="simple_white",
    )
    st.plotly_chart(fig)

# Treatment vs. Family History
elif visualization_choice == "Treatment vs. Family History":
    treatment_family = df.groupby("Family History")["Treatment"].mean().reset_index()
    fig = px.bar(
        treatment_family,
        x="Family History",
        y="Treatment",
        title="Treatment vs. Family History",
        labels={"Treatment": "Proportion Receiving Treatment"},
        color="Treatment",
        color_continuous_scale="Blues",
    )
    st.plotly_chart(fig)

# Work Interfere Distribution
elif visualization_choice == "Work Interfere Distribution":
    work_interfere_counts = df["Work Interfere"].value_counts().reset_index()
    work_interfere_counts.columns = ["Work Interfere", "Count"]
    fig = px.bar(
        work_interfere_counts,
        x="Work Interfere",
        y="Count",
        title="Work Interfere Distribution",
        labels={"Work Interfere": "Work Interfere", "Count": "Count"},
    )
    st.plotly_chart(fig)

# Seek Help Distribution
elif visualization_choice == "Seek Help Distribution":
    seek_help_counts = df["Seek Help"].value_counts().reset_index()
    seek_help_counts.columns = ["Seek Help", "Count"]
    fig = px.bar(
        seek_help_counts,
        x="Seek Help",
        y="Count",
        title="Seek Help Distribution",
        labels={"Seek Help": "Seek Help", "Count": "Count"},
    )
    st.plotly_chart(fig)

# Ease of Leave vs Treatment
elif visualization_choice == "Ease of Leave vs Treatment":
    contingency_table = pd.crosstab(df["Leave"], df["Treatment"])
    contingency_table.plot(
        kind="bar",
        stacked=True,
        figsize=(8, 6),
        color=["skyblue", "orange"],
    )
    plt.title("Ease of Taking Leave vs Seeking Treatment", fontsize=14)
    plt.xlabel("Ease of Taking Leave", fontsize=12)
    plt.ylabel("Count", fontsize=12)
    plt.xticks(rotation=45)
    plt.legend(title="Treatment", labels=["No", "Yes"])
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    st.pyplot(plt.gcf())
