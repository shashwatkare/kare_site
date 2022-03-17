import os
import requests
from PIL import Image
from streamlit_lottie import st_lottie
import streamlit as st
from streamlit_timeline import timeline

# Refer to this for emoji https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Shashwat Kare", page_icon=":bowtie:", layout="wide")

def lottie_loader(url):
    res = requests.get(url)
    if res.status_code != 200:
        return None
    return res.json()

def file_reader(file_name):
    with open(file_name, "r") as f:
        data = f.read()
        return data


# lottie_ani = lottie_loader("https://assets10.lottiefiles.com/packages/lf20_wfsunjgd.json")  # loader circle
lottie_ani = lottie_loader("https://assets6.lottiefiles.com/packages/lf20_g3dzz0wz.json")  # 3d social

style_path = os.path.abspath("src")+"/style/style.css"
print(style_path)
style_obj = file_reader(style_path)
st.markdown(f"<style>{style_obj}</style>", unsafe_allow_html=True)


def printer_sr(input_text):
    if input_text:
        return st.write(f'this is SR you entered: {input_text}')
    else:
        st.empty()

# Header Section
with st.container():
    left_col, right_col = st.columns(2)
    with left_col:
        st.subheader(":wave: Hi there, I'm")
        st.title("Shashwat Kare")
        st.subheader("Tech Lead | Python Developer | AI/ML Engineer | Cloud Expert | DevOps ")
        st.write("I help customer skyrocket :rocket: their profits ")
        st.write("by creating AI/ML products, Python Automation and Webservices ")
        st.write("providing data insights")
    with right_col:
        st_lottie(lottie_ani, height=250, key="loader")

timeline_path = os.path.abspath("src")+"/json/timeline.json"
print(style_path)
timeline_obj = file_reader(timeline_path)
timeline(timeline_obj, height=400)

with st.container():
    st.write("---")
    # left_col, right_col = st.columns((2,3))
    # with left_col:
    st.header("Instructions")
    # st.write("##")
    st.write(
        """
        - Use the text space given below to input valid SR (incident number)
        - Press on Submit to start the engine
        - :tada: You will see list of similar SRs
        """
    )


with st.container():
    # st.write("---")
    # st.header("Please Input Your SR")
    # st.write("##")
    with st.form(key='sr_form', clear_on_submit=True):
        text_input = st.text_input(label='SR Input', key="incident_number", placeholder="69xxxxxxx")
        submit_button = st.form_submit_button(label='Submit', on_click=printer_sr(text_input))
        # print(text_input)
