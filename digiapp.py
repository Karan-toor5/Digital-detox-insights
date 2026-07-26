import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.set_page_config(
    page_title="Digital Detox",
    page_icon="⚕️",
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
        df=pd.read_csv("/dataset/digital_detox.csv")
        return df
    except Exception as e:
        st.error(e)
        return None
df=load_data()
st.header("Data Overview")
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
tab1, tab2, tab3, tab4 = st.tabs([
    "📋 Column Information",
    "❗ Missing Values",
    "📝 Sample Data",
    "📊 Statistical Summary"
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
  
