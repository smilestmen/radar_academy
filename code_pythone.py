import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Radar Academy", layout="centered")
st.title("📊 Radar Academy - نقاط الضعف والقوة")
st.write("دخل نقط التلميذ من 0 ل 10 وشوف الرسم ديالو")

#smya del timlid
nom = st.text_input("أحمد",":اسم التلميذ")
#no9at
st.subheader("دخل النقط:")
maths = st.slider(label="Maths", min_value=0, max_value=10, value=7)
physique = st.slider(label="Physique", min_value=0, max_value=10, value=5)
francais = st.slider(label="Francais", min_value=0, max_value=10, value=8)
anglais = st.slider(label="Anglais", min_value=0, max_value=10, value=6)
arabe = st.slider(label="Arabe", min_value=0, max_value=10, value=4)

#Données dyal rassm
categories = ['الرياضيات', 'الفيزياء', 'الفرنسية', 'الإنجليزية', 'العربية']
values = [maths,physique,francais,anglais,arabe]

#bach rassm ytssd
values += values[:1]
angles = np.linspace(0, 2*np.pi , len(categories) , endpoint=False).tolist()
angles += angles[:1]

#rassm
fig, ax =plt.subplots(figsize=(6,6), subplot_kw=dict(polar=True))
ax.plot(angles, values, color='#1f77b4', linewidth=2)
ax.fill(angles,values,color='#1f77b4',alpha=0.25)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories)
ax.set_ylim(0,10)
ax.set_title(f"Radar Chart de {nom}", size=16,pad=20)
st.pyplot(fig)

#ta7lil automatique
st.subheader("🧠 التحليل:")
plus_fort=categories[np.argmax(values[:-1])]
plus_faible=categories[np.argmin(values[:-1])]
st.success(f"✅ point fort de {nom} est: **{plus_fort}**")
st.error(f"⚠️ point faible de {nom} est: **{plus_faible}**")
st.info(f"lmo3adal l3am: **{sum(values[:-1])/5:.1f}/10**")