# importing the packages
import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")
import seaborn as sns
import pandas as pd
import numpy as np

DATA_URL = ("movies_data.csv")

st.markdown("# Self Exploratory Visualization on movies data")
st.markdown("Explore the dataset to know more about movies")
img=Image.open('images/movie_Camera.jpg')
st.image(img,width=100)



st.markdown(" **MOVIE** is also called a film, motion picture or moving picture, is a work of visual art used to simulate experiences that communicate ideas, stories, perceptions, feelings, beauty, or atmosphere through the use of moving images. These images are generally accompanied by sound, and more rarely, other sensory stimulations. The word **cinema**, short for cinematography, is often used to refer to filmmaking and the film industry, and to the art form that is the result of it.")

st.markdown("The data presented here are of 3 different genres of movie - **SC-FI, Action, Thriller**")
 

if st.button("see the Movie genre's"):
    # Movie # 1
    img=Image.open('images/sc-fi.jpg')
    st.image(img,width=700, caption="SC-FI")
    # Movie # 2
    img=Image.open('images/action.jpg')
    st.image(img,width=700, caption="Action")
    # Movie # 3
    img=Image.open('images/thriller.png')
    st.image(img,width=700, caption="Thriller")
    
    # info 
    img=Image.open('images/all_movies.png')
    st.image(img,width=700, caption="info")
    # Ballons
    st.balloons() 


st.info("The dataset contains different aspects like Genre, Rank, Votes, Budget, Profit, IMDB-Rating etc.")
img=Image.open('images/all_movies_2.png')
st.image(img,width=700)


st.sidebar.markdown("## Side Panel")
st.sidebar.markdown("Use this panel to explore the dataset")

@st.cache(persist=True, show_spinner=True)
# Load the Data
def load_data(nrows):
	# Parse date and Time
    df = pd.read_csv(DATA_URL, nrows = nrows)
    lowercase = lambda x:str(x).lower()
    df.rename(lowercase, axis='columns',inplace=True)
    return df


st.markdown("### Click the button below to explore the dataset through my visualization")
if st.button("Visualization created by Author"):
    img=Image.open('images/visualization.png')
    st.image(img,width=700, caption="Viz. created by sunil kumar valmiki")
st.markdown("### **Takeaway:** SCI-FI is the most voted & highest rated genre of all 3")

st.markdown("-----")

# Loading data
# df = load_data(100000)
# original_data = df
st.header("Now, Explore Yourself the Movies")
# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading the Movie dataset....')
    # Load 10,000 rows of data into the dataframe.
df = load_data(100)
    # Notify the reader that the data was successfully loaded.
data_load_state.text('Loading Movie dataset....Completed!')

images=Image.open('images/all_movies.png')
st.image(images,width=600)

# Showing the original raw data
if st.checkbox("Show Raw Data", False):
    st.subheader('Raw data')
    st.write(df)


st.title('Quick Explore')
st.sidebar.subheader(' Quick Explore')
st.markdown("Tick the box on the side panel to explore the dataset.")
if st.sidebar.checkbox('Basic info'):
    if st.sidebar.checkbox('Dataset Quick Look'):
        st.subheader('Dataset Quick Look:')
        st.write(df.head())
    if st.sidebar.checkbox("Show Columns"):
        st.subheader('Show Columns List')
        all_columns = df.columns.to_list()
        st.write(all_columns)
    # if st.sidebar.checkbox('Column Names'):
    #     st.subheader('Column Names')
    #     st.write(df.columns())
    if st.sidebar.checkbox('Statistical Description'):
        st.subheader('Statistical Data Descripition')
        st.write(df.describe())
    if st.sidebar.checkbox('Missing Values?'):
        st.subheader('Missing values')
        st.write(df.isnull().sum())

st.title('Create Own Visualization')
st.markdown("Tick the box on the side panel to create your own Visualization.")
st.sidebar.subheader('Create Own Visualization')
if st.sidebar.checkbox('Graphics'):
    if st.sidebar.checkbox('Count Plot'):
        st.subheader('Count Plot')
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.info("If error, please adjust column name on side panel.")
        column_count_plot = st.sidebar.selectbox("Choose a column to plot count. Try Selecting attributes ",df.columns)
        hue_opt = st.sidebar.selectbox("Optional categorical variables. Try Selecting attributes ",df.columns.insert(0,None))
        # if st.checkbox('Plot Countplot'):
        fig = sns.countplot(x=column_count_plot,data=df,hue=hue_opt)
        st.pyplot()
              
    # if st.sidebar.checkbox('Heatmap'):
    #     st.subheader('HeatMap')
    #     fig = sns.heatmap(df.corr(),annot=True, annot_kws={"size": 9}, linewidths=1.5)
    #     st.pyplot()
        
        
    if st.sidebar.checkbox('Boxplot'):
        st.subheader('Boxplot')
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.info("If error, please adjust column name on side panel.")
        column_box_plot_X = st.sidebar.selectbox("X (Choose a column). Try Selecting island:",df.columns.insert(0,None))
        column_box_plot_Y = st.sidebar.selectbox("Y (Choose a column - only numerical). Try Selecting Body Mass",df.columns)
        hue_box_opt = st.sidebar.selectbox("Optional categorical variables (boxplot hue)",df.columns.insert(0,None))
        # if st.checkbox('Plot Boxplot'):
        fig = sns.boxplot(x=column_box_plot_X, y=column_box_plot_Y,data=df,palette="Set3")
        st.pyplot(fig)
    # if st.sidebar.checkbox('Pairplot'):
    #     st.subheader('Pairplot')
    #     hue_pp_opt = st.sidebar.selectbox("Optional categorical variables (pairplot hue)",df.columns.insert(0,None))
    #     st.info("This action may take a while.")
    #     fig = sns.pairplot(df,palette="coolwarm")
    #     st.pyplot()

st.markdown(" > Thank you for exploring Movie datasets. This is my first Streamlit work. Feedbacks are highly welcomed.")

st.sidebar.info(" [Source Article](https://github.com/sunilkumarvalmiki/data-visualization-web-app-using-streamlit) | [Twitter  Tags](https://twitter.com/SunilkumarValm1/status/1405965400211296257)")
st.sidebar.info("Project is done by [sunil kumar](https://twitter.com/SunilkumarValm1)")
st.sidebar.info("Self Exploratory Visualization on Movies - Brought To you By [Sunil Kumar](https://github.com/sunilkumarvalmiki)")
st.sidebar.text("Built with ❤️ Streamlit")