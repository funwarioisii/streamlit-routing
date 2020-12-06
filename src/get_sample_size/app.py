import streamlit as st
from get_sample_size import sample_size

p = st.number_input("prob of distribute of a (ex. 0.6) >>> ")  # 分布a の 確率
diff = st.number_input(
    "prob diff between distribute a and b (ex. 0.05) >>> "
)  # 分布a と 分布b の差分
alpha = st.number_input(
    "Determine the accuracy (1-α), set α (ex. 0.05) >>> "
)  # 確度 = (1 - α)

st.text(sample_size(float(p), float(diff), float(alpha)))
