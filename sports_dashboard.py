import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

# Simulated data (replacing with your generated dataset)
num_matches = 20
data = {
    "Match": [f"Match {i+1}" for i in range(num_matches)],
    "Goals": [np.random.randint(0, 5) for _ in range(num_matches)],
    "Assists": [np.random.randint(0, 4) for _ in range(num_matches)],
    "Stamina": [np.random.randint(50, 100) for _ in range(num_matches)],
    "Ball Possession (%)": [np.random.randint(40, 70) for _ in range(num_matches)],
    "Pass Success Rate (%)": [np.random.randint(60, 90) for _ in range(num_matches)],
    "Injury Risk (%)": [np.random.randint(10, 50) for _ in range(num_matches)],
}
simulated_data = pd.DataFrame(data)

# Streamlit app
st.title("Sports Analytics Dashboard")
st.sidebar.header("Filters")

# Filter for Match Range
match_range = st.sidebar.slider(
    "Select Match Range",
    1, num_matches,
    (1, num_matches)
)
filtered_data = simulated_data.iloc[match_range[0]-1:match_range[1]]

# Line Chart: Goals, Assists, and Stamina
st.header("Player Performance Trends")
line_fig = px.line(
    filtered_data,
    x="Match", y=["Goals", "Assists", "Stamina"],
    title="Player Performance Over Matches"
)
st.plotly_chart(line_fig)

# Bar Chart: Team Metrics
st.header("Team Metrics")
bar_fig = px.bar(
    filtered_data,
    x="Match",
    y=["Ball Possession (%)", "Pass Success Rate (%)"],
    title="Team Performance Metrics"
)
st.plotly_chart(bar_fig)

# Pie Chart: Injury Risk
st.header("Injury Risk Distribution")
injury_categories = ['Low', 'Moderate', 'High']
injury_counts = [
    len(filtered_data[filtered_data['Injury Risk (%)'] < 20]),
    len(filtered_data[(filtered_data['Injury Risk (%)'] >= 20) & (filtered_data['Injury Risk (%)'] < 35)]),
    len(filtered_data[filtered_data['Injury Risk (%)'] >= 35])
]
pie_fig = px.pie(values=injury_counts, names=injury_categories, title="Injury Risk Categories")
st.plotly_chart(pie_fig)

st.write("Filtered Data:", filtered_data)
