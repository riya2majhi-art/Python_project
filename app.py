import pandas as pd
import streamlit as st

Tab1,Tab2 = st.tabs(["col1","col2"])
with Tab1:
    df = pd.read_csv("riya.csv")

    st.sidebar.subheader("Menu")
    y = st.sidebar.multiselect("You can choose a value from here", df["City"].unique())
    z = st.sidebar.multiselect("You can choose a value from here", df["Has_Online_delivery"].unique())

    a = df["City"].isin(y)
    b = df["Has_Online_delivery"].isin(z)

    d = df[a & b]

    c = df.loc[a].groupby("Cuisines").agg(mean=("Average_Cost_for_two", "mean")).reset_index()
    e = df.loc[a].groupby("City").agg(mean=("Rating", "mean")).reset_index()

    st.dataframe(df.loc[a & b])
    st.dataframe(c)

    st.bar_chart(c, x="Cuisines", color="blue")
    st.bar_chart(e, x="City", color="red")
with Tab2:
    st.file_uploader("Upload a csv file")
    x = st.chat_input()
    st.chat_message("Users",)
    if st.button("Predict"):
        st.write("Hello")