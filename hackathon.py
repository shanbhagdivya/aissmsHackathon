import streamlit as st
import pandas as pd

df = pd.read_csv('booksData.csv')

def filter_data(subjects, price_min, price_max, rating_min, rating_max, top_n=None):
    filtered_df = pd.DataFrame()  # Initialize as an empty DataFrame
    for subject in subjects:
        subject_df = df[df["class"] == subject]
        subject_df = subject_df[(subject_df["price"] >= price_min) & (subject_df["price"] <= price_max)]
        subject_df = subject_df[(subject_df["ratings"] >= rating_min) & (subject_df["ratings"] <= rating_max)]
        if top_n:
            subject_df = subject_df.head(top_n)
        filtered_df = pd.concat([filtered_df, subject_df], ignore_index=True)
    return filtered_df

# Streamlit app
def main():
    # User input
    st.header("Study Material Recommender")
    
    with st.sidebar:
        subjects = st.multiselect("Select Subjects:", df["class"].unique())
        st.write("\n\n\n")
        price_min, price_max = st.slider("Price Range (₹):", min_value=df["price"].min(), max_value=df["price"].max(), value=(df["price"].min(), df["price"].max()))
        st.write("\n\n\n")
        rating_min, rating_max = st.slider("Rating Range:", min_value=df["ratings"].min(), max_value=df["ratings"].max(), value=(df["ratings"].min(), df["ratings"].max()))
        st.write("\n\n\n")
        sort_by = st.radio("Sort by:", ["None", "Alphabetical (A-Z)", "Alphabetical (Z-A)", "Price (Low to High)", "Price (High to Low)", "Rating (Low to High)", "Rating (High to Low)"])

    # Filter data
    filtered_df = filter_data(subjects, price_min, price_max, rating_min, rating_max, top_n=5)

    # Display recommendations
    if filtered_df.empty:
        st.text("No books found matching your criteria.")
    else:
        for subject in subjects:
            class_df = filtered_df[filtered_df["class"] == subject]
            if not class_df.empty:
                st.subheader(f"Subject: {subject}")  # Print class as heading
                if sort_by == "Alphabetical (A-Z)":
                    class_df = class_df.sort_values(by="bookName")
                elif sort_by == "Alphabetical (Z-A)":
                    class_df = class_df.sort_values(by="bookName", ascending=False)
                elif sort_by == "Price (Low to High)":
                    class_df = class_df.sort_values(by="price")
                elif sort_by == "Price (High to Low)":
                    class_df = class_df.sort_values(by="price", ascending=False)
                elif sort_by == "Rating (Low to High)":
                    class_df = class_df.sort_values(by="ratings")
                elif sort_by == "Rating (High to Low)":
                    class_df = class_df.sort_values(by="ratings", ascending=False)  
                for index, row in class_df.iterrows():
                    st.text(f"- Title: {row['bookName']}")
                    st.text(f"  Publisher: {row['authorPublisher']}")
                    st.text(f"  Price: ₹{row['price']}")
                    st.text(f"  Rating: {row['ratings']}")    

#if __name__ == "__main__":
    #main()
