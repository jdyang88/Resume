from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | JD(Jungdae) Yang"
PAGE_ICON = ":wave:"
NAME = "JD(Jungdae) Yang"
DESCRIPTION = """
Senior Manager working for SK earthon, 100% owned by SK innovation
"""
EMAIL = "jdyang88@gmail.com"

# SOCIAL_MEDIA = {
#     "YouTube": "https://youtube.com/c/codingisfun",
#     "LinkedIn": "https://linkedin.com",
#     "GitHub": "https://github.com",
#     "Twitter": "https://twitter.com",
# }


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
# cols = st.columns(len(SOCIAL_MEDIA))
# for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
#     cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience")
st.write(
    """
- ✔️ 18 years in commercial, financial & strategic planning in E&P industry
- ✔️ 6 years as commercial manager in Lubricants industry
- ✔️ 5 years as chemical engineer in Petrochemical field in Aromatics plant
"""
)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History (1995-Present)")
st.write("---")

# --- JOB 1
st.write("🚧", "**Senior Manager  | SK earthon**")
st.write("10/2022 - Present")
st.write(
    """
- ► Responsible for Qatar LNG and Oman LNG projects
- ► Led projects in S.E. Asia, Middle East and M&A in N. America
- ► Led negotiation on PSC, JOA and related agreements etc. 
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Director | Korea LNG Ltd.**")
st.write("02/2019 - 10/2022")
st.write(
    """
- ► General Management for LNG Project in Oman
- ► Network with partners and Omanese goverment
- ► Business extension and control compliance issues
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Head of HCMC Office in Vietnam | SK innovation**")
st.write("02/2014 - 12/2018")
st.write(
    """
- ► Responsible for all S.E. Asia projects
- ► Build relationships with partners and Vienamese Gov.
- ► Develop New Ventures, contract negotiations, asset valuation
"""
)

st.write('\n')
st.write("---")

# --- SKILLS ---
st.write('\n')
st.subheader("IT Skills")
st.write(
    """
- 👩‍💻 Knowledge : Machine Leraning / Deep Learning for data science
- 📊 Coding Language : Python
- 📚 etc. : MS Office(MS word, PPT and Excel) / basic knowledge in HTML, CSS, JavaScript
"""
)

# --- PROJECTS SECTION ---
st.write('\n')
st.write("Some examples")
PROJECTS = {
    "🏆 Korea Annual Population Dashboard": "https://koreanpopulation-jdyang88.streamlit.app/",
    "🏆 Korea Lotto Prediciton by 5 Machine Learing Models": "https://korealotto-jdyangh88.streamlit.app/",
    "🏆 Korea Stocks Prediction by Deep Learning Models(LSTM and Prophet)": "https://stocks-jdyang88.streamlit.app/"
}
for project_name, project_url in PROJECTS.items():
    st.markdown(f"[{project_name}]({project_url})")

st.write('\n')
st.write("---")

#--- Other Career ---
st.write('\n')
st.write("🗄️ Other Career : Military Service (1989-1991)")
st.write(
"""
KATUSA in the US Army base in Korea for 3 years as Medium heavy truck(M915) driver and Driver Instroductor in DTA(Drivers Training Academy),
Partly performed mission for the 1st Gulf War in 1991 """)
st.write(
"""
Awards : Distinguished Graduate in Drivers Training Academy in 69th Transportation Battalion in 1989 / 
ARCOM(The army commendation medal) Award in 1991 by Commander of 20th support group 
""")

st.write("---")

# for project, link in PROJECTS.items():
#     st.write(f"[{project}]({link})")

