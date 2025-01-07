import streamlit as st
import pandas as pd


# Load your datasets
def load_datasets():
    # Replace with the paths to your actual datasets

    original_df = pd.read_csv(r"C:\Users\HP\Data-Analysis-Medical-Health-In-Tech\survey.csv")
    cleaned_df = pd.read_csv(r"C:\Users\HP\Data-Analysis-Medical-Health-In-Tech\data.csv")
    return original_df, cleaned_df

# Display the dataset
def show_dataset(df, title):
    st.write(f"### {title}")
    st.dataframe(df)

# App Navigation
def main():
    st.set_page_config(page_title="Mental Health in Tech EDA", layout="wide")

    # Sidebar navigation
    st.sidebar.title("Navigation")
    menu = ["Original Dataset", "Cleaned Dataset"]
    choice = st.sidebar.radio("Go to", menu)




    # Load datasets
    original_df, cleaned_df = load_datasets()
    if choice == "Original Dataset":
        st.title("Original Dataset")
        st.write("""
        The dataset before any cleaning or preprocessing. 
        """)
        show_dataset(original_df, "Original Dataset")
    elif choice == "Cleaned Dataset":
        st.title("Cleaned Dataset")
        st.write("""
        The dataset after cleaning and preprocessing to remove missing values, handle outliers, and standardize data.
        """)
        show_dataset(cleaned_df, "Cleaned Dataset")


# Run the app
if __name__ == "__main__":
    main()
