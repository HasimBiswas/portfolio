#Name:- Hasim Biswas, Class:- XII-A, Roll No.:-19

import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Self Portfolio | Hasim BIswas',page_icon=':slightly_smiling_face:')
with st.sidebar:
    selected=option_menu(
        menu_title='Main Menu',
        options=['Home', 'About Me', 'Contact Me'],
        icons=['house', 'person', 'envelope'],
        menu_icon='cast',
        default_index=0,
    )

if selected=='Home':
    st.title('Welcome to My Portfolio')
    st.image('photo.jpg',width=300)
    st.header('Hasim Biswas')
    st.subheader('XII-A')
    st.subheader('Pure Science')
    st.write("Enthusiastic computer science student with a deep passion for coding and problem-solving. Dedicated to continuous learning and exploring innovative technologies. I like tackling complex challenges that require a lot of brain power which is precisely why I like CS so much. I am always eager to expand my knowledge and contribute to exciting CS projects.")

if selected=='About Me':
    st.title('About Me')
    st.write("I live in Kampa,Nagdaha,Kanchrapara,743193. Here is a map showing my location.")
    coordinates = {"lat":{0:22.9236012}, "lon":{0:88.4739397}}
    st.map(coordinates)
    st.subheader('My Family')
    st.write('There are 4 people in my family including me')
    st.write('Kabatulla Biswas, my father')
    st.write('Sahanara Biswas, my mother')
    st.write('Samim Biswas, my brother')

if selected=='Contact Me':
    st.title('Contact Me')
    contact_form="""
    <form action="https://formsubmit.co/hasimbiswas999@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your Email Address" required>
        <textarea name="message" placeholder="Your Message Here"></textarea>
        <button type="submit">Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    local_css("style/style.css")
