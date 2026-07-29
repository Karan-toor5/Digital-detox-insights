import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st
from PTL import Image
#icon_image=Image.open("1785324228193.png")
st.set_page_config(
    page_title="Digital Detox",
    page_icon="./1785324228193.png",
    layout="wide",
)
st.title("Digital Detox: Intelligent Insights for Digital Well-being")   
st.markdown("---")
st.header("Executive Summary")
st.markdown("---")
st.markdown("This project, Digital Detox: Intelligent Insights for Digital Well-being, is a Data Analytics and Visualization Project focuses on analyzing digital wellness data to understand users' technology usage patterns and their impact on daily life.The project emphasizes data cleaning, exploratory data analysis (EDA), and visual representation of the dataset.\n " \
+"\nThe interactive dashboard allows users to explore key digital wellness indicators such as screen time, social media usage, gaming hours, sleep duration, stress level, productivity, notifications, and digital addiction through dynamic charts and filters. These visualizations help identify trends, compare user behaviour across different categories, and generate meaningful insights for promoting healthier digital habits.")
st.subheader("Key Objectives")
st.markdown(
    """
    - Analyze daily screen time and digital device usage patterns.
    - Study the relationship between screen time, sleep duration, and stress levels.
    - Compare digital behaviour across different age groups and genders.
    - Identify trends in social media usage, gaming hours, and productivity.
    - Provide actionable insights for promoting digital well-being and healthier technology habits.
    - Generate meaningful insights to support digital well-being awareness.""")
st.subheader("Expected Deliverables")
st.markdown(
    """
    - Cleaned and preprocessed digital wellness dataset.
    - Interactive dashboard with visualizations for key digital wellness indicators.
    - Insights and recommendations for promoting healthier digital habits.
    - Summary report highlighting trends, correlations, and actionable insights.
    - User-friendly interface for exploring digital wellness data and generating insights.
    - Documentation of the project methodology, analysis, and findings.""")
st.divider()
st.header("Project Description")
st.subheader("Problem Statement")
st.markdown("The increasing use of smartphones, social media, gaming, and digital devices has significantly impacted people's daily lives. Excessive screen time and digital dependency can lead to poor sleep quality, increased stress levels, reduced productivity, and unhealthy digital habits. There is a need to analyze digital wellness data to identify behavioural patterns and promote healthier technology usage.\n"\
+"\nThis project analyzes a digital wellness dataset to generate data-driven insights that can help:")
st.markdown("""
    - **Students and Professionals:** Understand their screen time habits and improve productivity.
    - **Researchers:** Study the relationship between digital device usage, sleep, stress, and addiction.
    - **Healthcare and Wellness Professionals:** Promote awareness of healthy digital behaviour.
    - **Individuals:** Make informed decisions to achieve a better balance between technology usage and personal well-being.""")
st.subheader("Dataset Overview")
st.markdown("The Digital Wellness dataset contains information related to users' digital device usage, lifestyle habits, and behavioural patterns. The dataset is used to analyze how screen time and digital activities influence physical and mental well-being.")
st.markdown("##### Core User Information")
st.markdown(""" 
    - User ID and demographic details
    - Age and Gender
    - Daily Screen Time
    - Weekend Screen Time
    - Social Media Usage
    - Gaming Hours
    - Work/Study Hours
""")
st.markdown("##### Lifestyle and Behaviour Information")
st.markdown("""
    - Sleep Duration
    - Stress Level
    - Academic/Work Impact
    - Notifications per Day
    - App Opens per Day
    - Digital Addiction Level
    - Addiction Label (Addicted / Not Addicted)
""")
st.markdown("##### Purpose of the Dataset")
st.markdown("""
    - Analyze digital usage patterns across different users.
    - Study the relationship between screen time, sleep, and stress.
    - Compare digital behaviour based on age and gender.
    - Visualize trends using interactive charts and dashboards.
    - Generate meaningful insights to encourage healthier digital habits.
 """)
@st.cache_data
def load_data():

    try:

        df = pd.read_csv("dataset/digital_detox.csv")

        return df

    except Exception as e:

        st.error(f"Error loading dataset: {e}")

        return None


df = load_data()

if df is None:

    st.stop()
st.markdown("---")
# Create Basic Dataset Information table
dataset_info = pd.DataFrame({
    "Attribute": [
        "Dataset Name",
        "Domain",
        "Data Type",
        "Number of Records",
        "Number of Features",
        "File Format",
        "Analysis Tool",
        "Dashboard Tool",
        "Visualization Libraries"
    ],
    
    "Details": [
        "Digital Wellness Dataset",
        "Data Analytics / Digital Well-being",
        "Structured (CSV)",
        df.shape[0],                 # Number of rows
        df.shape[1],                 # Number of columns (features)
        "CSV",
        "Python, Jupyter Notebook",
        "Streamlit",
        "Plotly Express, Matplotlib, Seaborn"
    ]
})

# Display the table
st.subheader("📊 Basic Dataset Information")
st.dataframe(dataset_info, use_container_width=True)
col1,col2,col3,col4=st.columns(4)

with col1:
  st.metric(
            "Total Records",
            df.shape[0]
  )

with col2:
  st.metric(
            "Total Columns",
            df.shape[1]
  )

with col3:
  st.metric(
            "Missing Values",
            df.isnull().sum().sum()
  )

with col4:
  memory=df.memory_usage(deep=True).sum()/(1024**2)
  st.metric(
            "Memory Usage",
            f"{memory:.2f} MB"
  )
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📋 Column Information",
    "❗ Missing Values",
    "📝 Sample Data",
    "📊 Statistical Summary",
    "📂 Categorical Data"
])
with tab1:

    st.subheader("Column Information")

    column_info = pd.DataFrame({

        "Column Name": df.columns,

        "Data Type": df.dtypes,

        "Non-Null Values": df.count().values,

        "Null Values": df.isnull().sum().values,

        "Unique Values": df.nunique().values

    })

    st.dataframe(column_info, use_container_width=True)
with tab2:

    st.subheader("Missing Value Analysis")

    missing_values = pd.DataFrame({

        "Column": df.columns,

        "Missing Values": df.isnull().sum().values,

        "Missing %":
        ((df.isnull().sum()/len(df))*100).round(2)

    })

    st.dataframe(missing_values,
                 use_container_width=True)

    if df.isnull().sum().sum()==0:

        st.success("✅ No Missing Values Found")

    else:

        st.warning("⚠ Missing Values Found")
with tab3:

    st.subheader("Dataset Preview")

    option = st.radio(

        "Select Data",

        ["First 10 Rows",
         "Last 10 Rows",
         "Random 10 Rows"]

    )

    if option=="First 10 Rows":

        st.dataframe(df.head(10),
                     use_container_width=True)

    elif option=="Last 10 Rows":

        st.dataframe(df.tail(10),
                     use_container_width=True)

    else:

        st.dataframe(df.sample(10),
                     use_container_width=True)
with tab4:

    st.subheader("Statistical Summary")

    numerical = df.select_dtypes(include=np.number)

    st.markdown("### Numerical Statistics")

    st.dataframe(

        numerical.describe(),

        use_container_width=True

    )

    st.markdown("### Categorical Statistics")

    categorical = df.select_dtypes(include="object")

    st.dataframe(

        categorical.describe(),

        use_container_width=True

    )
with tab5:
    st.subheader("📂 Categorical Columns Summary")
    categorical_cols=df.select_dtypes(include=["object"]).columns
    for col in categorical_cols:
        st.markdown(f"### Column: {col}")
        st.write(f"Unique Values: {df[col].nunique()}")        
        value_counts = df[col].value_counts().reset_index()
        value_counts.columns = [col, "Count"]
        st.dataframe(value_counts, use_container_width=True)
        st.divider()
@st.cache_data
def cleaned_data():
    try:
        cleaned_df=df.copy()
        #replace missing value symbols
        cleaned_df.replace(["??","###","N/A","NaN"],np.nan,inplace=True)
        #remove duplicate rows
        cleaned_df.drop_duplicates(inplace=True, ignore_index=True)

        #fill missing values 
        for col in cleaned_df.columns:
            if cleaned_df[col].dtype in [np.float64, np.int64]:
                cleaned_df[col].fillna(cleaned_df[col].mean(), inplace=True)
            else:
                cleaned_df[col].fillna(cleaned_df[col].mode()[0], inplace=True)
        return cleaned_df
    except Exception as e:
        st.error(f"Error cleaning dataset: {e}")
        return None
cleaned_df = cleaned_data()

# Initialize Session State

if "selected_gender" not in st.session_state:
    st.session_state.selected_gender = sorted(cleaned_df["gender"].unique())

if "selected_age" not in st.session_state:
    st.session_state.selected_age = (
        int(cleaned_df["age"].min()),
        int(cleaned_df["age"].max())
    )

if "selected_addiction" not in st.session_state:
    st.session_state.selected_addiction = sorted(cleaned_df["addiction_level"].unique())

if "selected_stress" not in st.session_state:
    st.session_state.selected_stress = sorted(cleaned_df["stress_level"].unique())

if "selected_label" not in st.session_state:
    st.session_state.selected_label = sorted(cleaned_df["addicted_label"].unique())

# Sidebar Filters
with st.sidebar:

    st.header("🎯 Filters")

    gender = st.multiselect(
        "👤 Gender",
        options=sorted(cleaned_df["gender"].unique())
    )

    addiction = st.multiselect(
        "📱 Addiction Level",
        options=sorted(cleaned_df["addiction_level"].unique())
    )

    stress = st.multiselect(
        "😣 Stress Level",
        options=sorted(cleaned_df["stress_level"].unique())
    )

    label = st.multiselect(
        "⚠️ Addiction Status",
        options=sorted(cleaned_df["addicted_label"].unique())
    )

    age = st.slider(
        "💠 Age",
        min_value=int(cleaned_df["age"].min()),
        max_value=int(cleaned_df["age"].max()),
        value=st.session_state.selected_age
    )

    col1, col2 = st.columns(2)

    with col1:
        apply = st.button(
            "✅ Apply",
            use_container_width=True,
            type="primary"
        )

    with col2:
        reset = st.button(
            "🔄 Reset",
            use_container_width=True
    )
#Apply Filters
if apply:

    st.session_state.selected_gender = gender

    st.session_state.selected_addiction = addiction

    st.session_state.selected_stress = stress

    st.session_state.selected_label = label

    st.session_state.selected_age = age
#Reset Filters   
if reset:

    st.session_state.selected_gender = sorted(cleaned_df["gender"].unique())

    st.session_state.selected_addiction = sorted(cleaned_df["addiction_level"].unique())

    st.session_state.selected_stress = sorted(cleaned_df["stress_level"].unique())

    st.session_state.selected_label = sorted(cleaned_df["addicted_label"].unique())

    st.session_state.selected_age = (
        int(cleaned_df["age"].min()),
        int(cleaned_df["age"].max())
    )

    st.rerun()
#Filtered Dataframe
filtered_df = cleaned_df.copy()

# Gender
if st.session_state.selected_gender:
    filtered_df = filtered_df[
        filtered_df["gender"].isin(st.session_state.selected_gender)
    ]

# Addiction Level
if st.session_state.selected_addiction:
    filtered_df = filtered_df[
        filtered_df["addiction_level"].isin(st.session_state.selected_addiction)
    ]

# Stress Level
if st.session_state.selected_stress:
    filtered_df = filtered_df[
        filtered_df["stress_level"].isin(st.session_state.selected_stress)
    ]

# Addiction Label
if st.session_state.selected_label:
    filtered_df = filtered_df[
        filtered_df["addicted_label"].isin(st.session_state.selected_label)
    ]

# Age
filtered_df = filtered_df[
    filtered_df["age"].between(
        st.session_state.selected_age[0],
        st.session_state.selected_age[1]
    )
]
# 📊 DIGITAL WELLNESS VISUALIZATIONS

st.header("📊 Visualization and Insights")
st.markdown("---")
st.subheader("1️⃣ Average Daily Screen Time by Gender")
bar_df=filtered_df.groupby("gender",as_index=False)["daily_screen_time_hours"].mean()
fig=px.bar(bar_df,
        x="gender",
        y="daily_screen_time_hours",
        text_auto=".2f",
        title="Average Daily Screen Time by Gender",
        labels={
            "gender": "Gender",
            "daily_screen_time_hours": "Average Daily Screen Time (Hours)"
        }
)
fig.update_layout(title_x=0.5, title_font=dict(size=20), xaxis_title_font=dict(size=14), yaxis_title_font=dict(size=14),
    xaxis_title="Gender", yaxis_title="Average Daily Screen Time (Hours)"
)
st.plotly_chart(fig, use_container_width=True)
st.markdown("#### Key Insights:")
st.markdown("""
    - Compares the average daily screen time of different genders.
    - Helps identify which gender spends more time on digital devices.
    - Useful for understanding gender-based screen time behavior.
""")


# 2️⃣ Screen Time Trend by Age
st.subheader("2️⃣ Screen Time Trend Across Different Age Groups")

line_df = filtered_df.groupby(["age","gender"], as_index=False)["daily_screen_time_hours"].mean()

fig = px.line(
    line_df,
    x="age",
    y="daily_screen_time_hours",
    color="gender",
    markers=True,
    title="Average Screen Time by Age and Gender"
)

fig.update_layout(
    template="plotly_white",
    title_x=0.5
)

st.plotly_chart(fig, use_container_width=True)
st.markdown("#### Key Insights:")
st.markdown("""
    - Shows how average daily screen time varies across different age groups.
    - Highlights increasing or decreasing screen time trends with age.
    - Identifies age groups with higher digital engagement.
""")

# 3️⃣ Screen Time vs Sleep Duration
st.subheader("3️⃣ Relationship Between Daily Screen Time and Sleep Duration")
sample_df = filtered_df.sample(n=250, random_state=42)  # Sample 250 records for better visualization
fig = px.scatter(
    sample_df,
    x="daily_screen_time_hours",
    y="sleep_hours",
    color="addicted_label",
    hover_data=["age","gender"],
    title="Daily Screen Time vs Sleep Hours"
)

fig.update_layout(
    template="plotly_white",
    title_x=0.5
    
)

st.plotly_chart(fig, use_container_width=True)
st.markdown("""#### Key Insights:
    - Explores the relationship between screen time and sleep duration.
""")
# 4️⃣ Screen Time Distribution by Addiction Level
st.subheader("4️⃣ Daily Screen Time Distribution Across Addiction Levels")

fig = px.box(
    filtered_df,
    x="addiction_level",
    y="daily_screen_time_hours",
    color="gender",
    title="Screen Time Distribution by Addiction Level"
)

fig.update_layout(
    template="plotly_white",
    title_x=0.5
)

st.plotly_chart(fig, use_container_width=True)

# 5️⃣ Social Media Usage by Stress Level
st.subheader("5️⃣ Social Media Usage Across Different Stress Levels")

fig = px.violin(
    filtered_df,
    x="stress_level",
    y="social_media_hours",
    color="gender",
    box=True,
    title="Social Media Usage across Stress Levels"
)

fig.update_layout(
    template="plotly_white",
    title_x=0.5
)

st.plotly_chart(fig, use_container_width=True)

# 6️⃣ Distribution of Daily Screen Time
st.subheader("6️⃣ Distribution of Daily Screen Time Among Users")

fig = px.histogram(
    filtered_df,
    x="daily_screen_time_hours",
    color="addicted_label",
    nbins=20,
    title="Distribution of Daily Screen Time"
)

fig.update_layout(
    template="plotly_white",
    title_x=0.5,
    bargap=0.05
)

st.plotly_chart(fig, use_container_width=True)

# 7️⃣ Percentage of Users by Addiction Level
st.subheader("7️⃣ User Distribution Based on Addiction Level")

pie_df = filtered_df["addiction_level"].value_counts().reset_index()
pie_df.columns = ["addiction_level","Count"]

fig = px.pie(
    pie_df,
    names="addiction_level",
    values="Count",
    hole=0.45,
    title="Distribution of Addiction Levels"
)

fig.update_layout(
    template="plotly_white",
    title_x=0.5
)

st.plotly_chart(fig, use_container_width=True)

# 8️⃣ Gender-wise Addiction Level Composition
st.subheader("8️⃣ Gender-wise Distribution of Digital Addiction Levels")

tree_df = filtered_df.groupby(
    ["gender","addiction_level"]
).size().reset_index(name="Count")

fig = px.treemap(
    tree_df,
    path=["gender","addiction_level"],
    values="Count",
    color="addiction_level",
    title="Treemap of Gender and Addiction Level"
)

fig.update_layout(title_x=0.5)

st.plotly_chart(fig, use_container_width=True)

# 9️⃣ Gender, Stress Level and Addiction Analysis
st.subheader("9️⃣ Hierarchical Analysis of Gender, Stress Level and Digital Addiction")

sun_df = filtered_df.groupby(
    ["gender","stress_level","addiction_level"]
).size().reset_index(name="Count")

fig = px.sunburst(
    sun_df,
    path=["gender","stress_level","addiction_level"],
    values="Count",
    title="Gender, Stress Level and Addiction Level"
)

fig.update_layout(title_x=0.5)

st.plotly_chart(fig, use_container_width=True)

# 🔟 Stress Level vs Addiction Level Heatmap
st.subheader("🔟 Relationship Between Stress Level and Digital Addiction")
heat_df = pd.crosstab(
    filtered_df["stress_level"],
    filtered_df["addiction_level"]
)

fig = px.imshow(
    heat_df,
    text_auto=True,
    aspect="auto",
    title="Stress Level vs Addiction Level"
)

fig.update_layout(
    title_x=0.5
)

st.plotly_chart(fig, use_container_width=True)

#st.subheader("🔥 Density Heatmap: Daily Screen Time vs Sleep Hours")

#fig = px.density_heatmap(
#    filtered_df,
#    x="daily_screen_time_hours",
#    y="sleep_hours",
#    nbinsx=10,
#    nbinsy=10,
#    color_continuous_scale="Viridis",
#    title="Density of Daily Screen Time and Sleep Hours"
#)

#fig.update_layout(
#    template="plotly_white",
#    title_x=0.5,
#    xaxis_title="Daily Screen Time (Hours)",
#    yaxis_title="Sleep Hours",
#    coloraxis_colorbar_title="User Count"
#)

#st.plotly_chart(fig, use_container_width=True)

# 1️⃣1️⃣ Digital Addiction Funnel Analysis
st.subheader("1️⃣1️⃣ User Progression Across Digital Addiction Levels")

funnel_df = filtered_df["addiction_level"].value_counts().reset_index()
funnel_df.columns = ["addiction_level","Count"]

fig = px.funnel(
    funnel_df,
    x="Count",
    y="addiction_level",
    title="Users across Addiction Levels"
)

fig.update_layout(
    template="plotly_white",
    title_x=0.5,
    height=800


)

st.plotly_chart(fig, use_container_width=True)



