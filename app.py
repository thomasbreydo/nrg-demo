import streamlit as st
from img import img_to_html
import pandas as pd
from model import load_model


st.beta_set_page_config(
    page_title="NRG Demonstration",
    page_icon="logo.png",  # doesn't yet work
)
st.image("logo.png", width=400)

age = st.number_input("Age", min_value=1)
race = st.selectbox("Race", ("Asian", "Black", "White", "Other"))
diet = st.selectbox("Diet", ("Keto", "Fasting", "Other"))
insulin_resistant = st.checkbox("Patient has insulin resistance.")

personrow = pd.DataFrame(
    columns=(
        "Race_Black",
        "Race_Multi",
        "Race_White",
        "Diet_Fast",
        "Diet_GLC_2",
        "Age",
        "InsulinResistant",
    ),
    index=[0],
)
personrow.loc[0, "Race_Black"] = race == "Black"
personrow.loc[0, "Race_Multi"] = race == "Other"
personrow.loc[0, "Race_White"] = race == "White"
personrow.loc[0, "Diet_Fast"] = diet == "Fasting"
personrow.loc[0, "Diet_GLC_2"] = diet == "Other"
personrow.loc[0, "Age"] = age
personrow.loc[0, "InsulinResistant"] = insulin_resistant

model = load_model()

st.write(
    f"""NRG predicts that this patient's mean brain instability is
    {model.predict(personrow)[0]:.4f}.
    """
)