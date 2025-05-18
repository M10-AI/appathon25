import streamlit as st

st.set_page_config(layout="wide")

left, center, right = st.columns([2,4,2])

with center:
    # Banner with centered text and larger font
    st.image("banner.png")
    st.markdown("")

    registration, about = st.tabs(["Registration", "About us"])

    with registration:
        # Centered heading with custom color and size
        
        # Larger font for paragraph
        st.markdown("<div style='text-align: center; font-size: 20px;'>Gothenburg APPathon -25 is an event where teams get to build an application around a certain theme in groups of 1-5. Participation is limited to students, up to master's levels. <br> Programming language is free of choice.</div>", unsafe_allow_html=True)
        st.divider()

        # Rules with increased font size
        st.markdown("<h3 style='text-align: center; color: red; font-size: 28px;'>Rules</h3>", unsafe_allow_html=True)
        st.markdown("""
        <div style='text-align: center; font-size: 20px;'>
            - Time limit: 24 hours<br>
            - Participants must be registered students for spring -25 with valid credentials<br>
            - Team size: 1-5 participants<br>
            - Inauguration at Chalmers campus Johanneberg<br>
            - Remote work allowed afterwards<br>
            - Teams may work overnight but cannot sleep over
        </div>
        """, unsafe_allow_html=True)
        st.divider()

        # Registration steps with larger font
        st.markdown("<h3 style='text-align: center; color: blue; font-size: 28px;'>How to register</h3>", unsafe_allow_html=True)
        st.markdown("<div style='text-align: center; font-size: 20px;'>1. Reserve your spot through <a href='https://forms.gle/gzxN48refAxTdQNQ7'>this form</a></div>", unsafe_allow_html=True)
        st.markdown("<div style='text-align: center; font-size: 20px;'>2. Await email on June 7th with location details</div>", unsafe_allow_html=True)
        st.markdown("<div style='text-align: center; font-size: 20px;'>3. Register your team in person on June 14th - all team members must be present!</div>", unsafe_allow_html=True)
        st.divider()

        st.markdown("<h3 style='text-align: center; color: green; font-size: 28px; '> Prize </h3>", unsafe_allow_html=True)
        st.markdown("<div style='text-align: center; font-size: 20px;'>- Gold: 3000 SEK</div>", unsafe_allow_html=True)
        st.markdown("<div style='text-align: center; font-size: 20px;'>- Silver: 1500 SEK</div>", unsafe_allow_html=True)
        st.markdown("<div style='text-align: center; font-size: 20px;'>- Bronze: 500 SEK</div>", unsafe_allow_html=True)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

    with about:
        # Centered image and title with larger fonts
        st.image('aktlogo.png', width=300)
        st.markdown("<h1 style='text-align: center; font-size: 36px;'>Akash Network</h1>", unsafe_allow_html=True)
        
        # Content with larger font
        st.markdown("""
        <div style='text-align: center; font-size: 20px;'>
            Akash Network, also known as the Airbnb of cloud computing, is a decentralized marketplace for cloud resources.    
            Powered by blockchain, it provides access to GPUs, cloud storage, and hosting via the <a href='https://console.akash.network/'>Akash Console</a>.<br><br>
            <a href='https://akash.network/pricing/gpus/'>GPU Calculator</a> | 
            <a href='https://chat.akash.network/'>Akash Chat</a> | 
            <a href='https://akash.network/'>Official Site</a> | 
            <a href='https://discord.gg/VBXH6GXH'>Discord</a>
        </div>
        """, unsafe_allow_html=True)
        st.divider()

        # Centered image and title for M10 AI
        st.image('noback.png', width=300)
        st.markdown("<h1 style='text-align: center; font-size: 32px;'>M10 AI</h1>", unsafe_allow_html=True)
        
        # Larger font for M10 AI description
        st.markdown("""
        <div style='text-align: center; font-size: 20px;'>
            M10 AI is a Chalmers-based AI association formed by computer science students.  
            Activities include workshops, collective studies, and networking.<br><br>
            <a href='https://www.linkedin.com/company/m10-ai'>LinkedIn</a> | 
            <a href='https://discord.gg/9zEz9Crfn3'>Discord</a>
        </div>
        """, unsafe_allow_html=True)
        st.divider()