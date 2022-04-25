import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from PIL import Image
import streamlit.components.v1 as components
import folium
from streamlit_folium import folium_static
import numpy as np
import os.path

my_path = os.path.abspath(os.path.dirname(__file__))
file1 = os.path.join(my_path, "Data Ekspor Impor/Perkembangan Ekspor NonMigas (Komoditi) Periode 2017 - 2022.xlsx")
file2 = os.path.join(my_path, "Data Ekspor Impor/Perkembangan Impor Non Migas - Komoditi Periode 2017 - 2022.xlsx")
flagimg = os.path.join(my_path, "Flag_map_of_Indonesia.jpg")
fileayam = os.path.join(my_path, "Produksi/Ayam.xlsx")
filesapi = os.path.join(my_path, "Produksi/Sapi.xlsx")
filekebun = os.path.join(my_path, "Produksi/Perkebunan.xlsx")
filepadi = os.path.join(my_path, "Produksi/Luas Panen, Produksi, dan Produktivitas Padi Menurut Provinsi.xlsx")
fileikan1 = os.path.join(my_path, "Produksi/Ikan Tangkap.xlsx")
fileikan2 = os.path.join(my_path, "Produksi/Ikan Budidaya.xls")
mapfile = os.path.join(my_path, "Data Ekspor Impor/indonesia-geojson-master/indonesia.geojson")
filekons = os.path.join(my_path, "Konsumsi/Konsumsi.xlsx")



st.set_page_config("Indonesia Economy Activity Infographic Web",layout="wide")

df = pd.read_excel (file1) 
df.columns = range(df.shape[1])
df1 = pd.read_excel (file2)
df1.columns = range(df.shape[1])

data_kopiteh = []
for i in range(0,len(df[2])):
    if df[2][i] == "KOPI, TEH, REMPAH-REMPAH": 
        for j in range(3,8):
            data_kopiteh.append(df[j][i])
for i in range(0,len(data_kopiteh)):
     data_kopiteh[i] = float(data_kopiteh[i].replace(',',''))

imp_kopiteh = []
for i in range(0,len(df1[2])):
    if df1[2][i] == "KOPI, TEH, REMPAH-REMPAH": 
        for j in range(3,8):
            imp_kopiteh.append(df1[j][i])

data_garambel = []
for i in range(0,len(df[2])):
    if df[2][i] == "GARAM, BELERANG, KAPUR": 
        for j in range(3,8):
            data_garambel.append(df[j][i])

imp_garambel = []
for i in range(0,len(df1[2])):
    if df1[2][i] == "GARAM, BELERANG, KAPUR": 
        for j in range(3,8):
            imp_garambel.append(df1[j][i])
            
imp_garambel = list(map(str,imp_garambel))
for i in range(0,len(imp_garambel)):
    if "," in  imp_garambel[i]:
        imp_garambel[i] = imp_garambel[i].replace(',','')
imp_garambel = list(map(float,imp_garambel))

data_gula = []
for i in range(0,len(df[2])):
    if df[2][i] == "GULA DAN KEMBANG GULA": 
        for j in range(3,8):
            data_gula.append(df[j][i])

imp_gula = []
for i in range(0,len(df1[2])):
    if df1[2][i] == "GULA DAN KEMBANG GULA": 
        for j in range(3,8):
            imp_gula.append(df1[j][i])
for i in range(0,len(imp_gula)):
     imp_gula[i] = float(imp_gula[i].replace(',',''))

data_kakao = []
for i in range(0,len(df[2])):
    if df[2][i] == "KAKAO/COKLAT": 
        for j in range(3,8):
            data_kakao.append(df[j][i])
for i in range(0,len(data_kakao)):
     data_kakao[i] = float(data_kakao[i].replace(',',''))


imp_kakao = []
for i in range(0,len(df1[2])):
    if df1[2][i] == "KAKAO/COKLAT": 
        for j in range(3,8):
            imp_kakao.append(df1[j][i])


data_temb = []
for i in range(0,len(df[2])):
    if df[2][i] == "TEMBAKAU": 
        for j in range(3,8):
            data_temb.append(df[j][i])
for i in range(0,len(data_temb)):
     data_temb[i] = float(data_temb[i].replace(',',''))

imp_temb = []
for i in range(0,len(df1[2])):
    if df1[2][i] == "TEMBAKAU": 
        for j in range(3,8):
            imp_temb.append(df1[j][i])

data_ikanudang = []
for i in range(0,len(df[2])):
    if df[2][i] == "IKAN DAN UDANG": 
        for j in range(3,8):
            data_ikanudang.append(df[j][i])
for i in range(0,len(data_ikanudang)):
    if "," in  data_ikanudang[i]:
        data_ikanudang[i] = float(data_ikanudang[i].replace(',',''))

imp_ikanudang = []
for i in range(0,len(df1[2])):
    if df1[2][i] == "IKAN DAN UDANG": 
        for j in range(3,8):
            imp_ikanudang.append(df1[j][i])

data_dgniknol = []
for i in range(0,len(df[2])):
    if df[2][i] == "DAGING DAN IKAN OLAHAN": 
        for j in range(3,8):
            data_dgniknol.append(df[j][i])
data_dgniknol = list(map(str,data_dgniknol))
for i in range(0,len(data_dgniknol)):
    if "," in  data_dgniknol[i]:
        data_dgniknol[i] = data_dgniknol[i].replace(',','')

imp_dgniknol = []
for i in range(0,len(df1[2])):
    if df1[2][i] == "DAGING DAN IKAN OLAHAN": 
        for j in range(3,8):
            imp_dgniknol.append(df1[j][i])

data_pupuk = []
for i in range(0,len(df[2])):
    if df[2][i] == "PUPUK": 
        for j in range(3,8):
            data_pupuk.append(df[j][i])

imp_pupuk = []
for i in range(0,len(df1[2])):
    if df1[2][i] == "PUPUK": 
        for j in range(3,8):
            imp_pupuk.append(df1[j][i])
for i in range(0,len(imp_pupuk)):
     imp_pupuk[i] = float(imp_pupuk[i].replace(',',''))

data_besi = []
for i in range(0,len(df[2])):
    if df[2][i] == "BESI DAN BAJA": 
        for j in range(3,8):
            data_besi.append(df[j][i])
for i in range(0,len(data_besi)):
     data_besi[i] = float(data_besi[i].replace(',',''))

imp_besi = []
for i in range(0,len(df1[2])):
    if df1[2][i] == "BESI DAN BAJA": 
        for j in range(3,8):
            imp_besi.append(df1[j][i])
for i in range(0,len(imp_besi)):
     imp_besi[i] = float(imp_besi[i].replace(',',''))


data_mesinlistrik = []
for i in range(0,len(df[2])):
    if df[2][i] == "MESIN/PERALATAN LISTRIK": 
        for j in range(3,8):
            data_mesinlistrik.append(df[j][i])
for i in range(0,len(data_mesinlistrik)):
     data_mesinlistrik[i] = float(data_mesinlistrik[i].replace(',',''))

imp_mesinlistrik = []
for i in range(0,len(df1[2])):
    if df1[2][i] == "MESIN/PERALATAN LISTRIK": 
        for j in range(3,8):
            imp_mesinlistrik.append(df1[j][i])
for i in range(0,len(imp_mesinlistrik)):
     imp_mesinlistrik[i] = float(imp_mesinlistrik[i].replace(',',''))


plt.tight_layout()


components.html(
    """
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    <h1 style="text-align:center;">Indonesia Economy Activity Infographic</h1>
    """,height=50,
)
image = Image.open(flagimg)
col1, col2, col3 = st.columns([1,6,1])

with col1:
    st.write("")

with col2:
    st.image(image, caption='Indonesia')

with col3:
    st.write("")

############## EXPORT
st.header("Indonesia Export Chart")

col1, col2 = st.columns([4,2])

with col1:
    optionA = st.selectbox(
     'Komoditas Export',
     ("Kopi dan Teh", "Garam dan Belerang", "Gula", "Kakao", 
     "Tembakau","Ikan dan Udang","Daging dan Ikan Olahan",
     "Pupuk","Besi","Mesin dan Peralatan Listrik"),
    key=1155)

if optionA == "Kopi dan Teh":
    optionAA = data_kopiteh
elif optionA == "Garam dan Belerang":
    optionAA = data_garambel
elif optionA == "Gula":
    optionAA = data_kopiteh
elif optionA == "Kakao":
    optionAA = data_kakao
elif optionA == "Tembakau":
    optionAA = data_temb
elif optionA == "Ikan dan Udang":
    optionAA = data_ikanudang
elif optionA == "Daging dan Ikan Olahan":
    optionAA = data_dgniknol
elif optionA == "Pupuk":
    optionAA = data_pupuk
elif optionA == "Besi":
    optionAA = data_besi
elif optionA == "Mesin dan Peralatan Listrik":
    optionAA = data_mesinlistrik
else:
    optionAA = None

fig2 = plt.figure(figsize=(20, 5), facecolor='#e8f4f0')
Year = [2017,2018,2019,2020,2021]
plt.plot(Year,optionAA)
locator = matplotlib.ticker.MultipleLocator()
plt.gca().xaxis.set_major_locator(locator)
formatter = matplotlib.ticker.StrMethodFormatter("{x:.0f}")
plt.gca().xaxis.set_major_formatter(formatter)
plt.title("{} (Juta US$)".format(optionA))
st.pyplot(fig2)

############## IMPORT
st.header("Indonesia Import Chart")
col1, col2 = st.columns([4,2])

with col1:
    optionB = st.selectbox(
     'Komoditas Import',
     ("Kopi dan Teh", "Garam dan Belerang", "Gula", "Kakao", 
     "Tembakau","Ikan dan Udang","Daging dan Ikan Olahan",
     "Pupuk","Besi","Mesin dan Peralatan Listrik"),
    key=1152)

if optionB == "Kopi dan Teh":
    optionBB = data_kopiteh
elif optionB == "Garam dan Belerang":
    optionBB = data_garambel
elif optionB == "Gula":
    optionBB = data_kopiteh
elif optionB == "Kakao":
    optionBB = data_kakao
elif optionB == "Tembakau":
    optionBB = data_temb
elif optionB == "Ikan dan Udang":
    optionBB = data_ikanudang
elif optionB == "Daging dan Ikan Olahan":
    optionBB = data_dgniknol
elif optionB == "Pupuk":
    optionBB = data_pupuk
elif optionB == "Besi":
    optionBB = data_besi
elif optionB == "Mesin dan Peralatan Listrik":
    optionBB = data_mesinlistrik
else:
    optionBB = None

fig2 = plt.figure(figsize=(20, 5), facecolor='#e8f4f0')
Year = [2017,2018,2019,2020,2021]
plt.plot(Year,optionBB)
locator = matplotlib.ticker.MultipleLocator()
plt.gca().xaxis.set_major_locator(locator)
formatter = matplotlib.ticker.StrMethodFormatter("{x:.0f}")
plt.gca().xaxis.set_major_formatter(formatter)
plt.title("{} (Juta US$)".format(optionB))
st.pyplot(fig2)


############## RATIO
 
st.write("")
col1, col2 = st.columns([2,4])

with col1:
    st.header("Indonesia Export - Import Ratio")

with col2:
    option1 = st.selectbox(
     'Tahun',
     (2017, 2018, 2019, 2020, 2021))

if option1 == 2017:
    option1 = 0
elif option1 == 2018:
    option1 = 1
elif option1 == 2019:
    option1 = 2
elif option1 == 2020:
    option1 = 3
else:
    option1 = 4

labels = 'Export', 'Import'
sizes = [data_kopiteh[option1], imp_kopiteh[option1]]
colors = ['#66b3ff','#ff9999']
explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')
fig1 = plt.figure(figsize=(20, 5), facecolor='#e8f4f0')
ax1 = plt.subplot2grid((2,5),(0,0))
plt.pie(sizes, wedgeprops=dict(width=.5), colors=colors ,autopct='%1.1f%%',
        shadow=True, startangle=30,)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("Kopi, Teh, Rempah-Rempah")

labels = 'Export', 'Import'
sizes = [data_garambel[option1], imp_garambel[option1]]
colors = ['#66b3ff','#ff9999']
explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')
ax2 = plt.subplot2grid((2,5),(0,1))
plt.pie(sizes,  wedgeprops=dict(width=.5), colors=colors ,autopct='%1.1f%%',
        shadow=True, startangle=30,)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("Garam & Belerang")

labels = 'Export', 'Import'
sizes = [data_gula[option1], imp_gula[option1]]
colors = ['#66b3ff','#ff9999']
explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')
ax3 = plt.subplot2grid((2,5),(0,2))
plt.pie(sizes, wedgeprops=dict(width=.5), colors=colors ,autopct='%1.1f%%',
        shadow=True, startangle=30,)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("Gula")

labels = 'Export', 'Import'
sizes = [data_kakao[option1], imp_kakao[option1]]
colors = ['#66b3ff','#ff9999']
explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')
ax4 = plt.subplot2grid((2,5),(0,3))
plt.pie(sizes, wedgeprops=dict(width=.5), colors=colors ,autopct='%1.1f%%',
        shadow=True, startangle=30,)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("Kakao")

labels = 'Export', 'Import'
sizes = [data_temb[option1], imp_temb[option1]]
colors = ['#66b3ff','#ff9999']
explode = (0, 0.1) 
ax5 = plt.subplot2grid((2,5),(0,4))
plt.pie(sizes, wedgeprops=dict(width=.5), colors=colors ,autopct='%1.1f%%',
        shadow=True, startangle=30,)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("Tembakau")


labels = 'Export', 'Import'
sizes = [data_ikanudang[option1], imp_ikanudang[option1]]
colors = ['#66b3ff','#ff9999']
explode = (0, 0.1) 
ax6 = plt.subplot2grid((2,5),(1,0))
plt.pie(sizes, wedgeprops=dict(width=.5), colors=colors ,autopct='%1.1f%%',
        shadow=True, startangle=30,)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("Ikan dan Udang")

labels = 'Export', 'Import'
sizes = [data_dgniknol[option1], imp_dgniknol[option1]]
colors = ['#66b3ff','#ff9999']
explode = (0, 0.1) 
ax7 = plt.subplot2grid((2,5),(1,1))
plt.pie(sizes, wedgeprops=dict(width=.5), colors=colors ,autopct='%1.1f%%',
        shadow=True, startangle=30,)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("Daging dan Ikan Olahan")

labels = 'Export', 'Import'
sizes = [data_pupuk[option1], imp_pupuk[option1]]
colors = ['#66b3ff','#ff9999']
explode = (0, 0.1) 
ax8 = plt.subplot2grid((2,5),(1,2))
plt.pie(sizes, wedgeprops=dict(width=.5), colors=colors ,autopct='%1.1f%%',
        shadow=True, startangle=30,)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("Pupuk")

labels = 'Export', 'Import'
sizes = [data_besi[option1], imp_besi[option1]]
colors = ['#66b3ff','#ff9999']
explode = (0, 0.1) 
ax9 = plt.subplot2grid((2,5),(1,3))
plt.pie(sizes, wedgeprops=dict(width=.5), colors=colors ,autopct='%1.1f%%',
        shadow=True, startangle=30,)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("Besi")


labels = 'Export', 'Import'
sizes = [data_mesinlistrik[option1], imp_mesinlistrik[option1]]
colors = ['#66b3ff','#ff9999']
explode = (0, 0.1) 
ax10 = plt.subplot2grid((2,5),(1,4))
plt.pie(sizes, wedgeprops=dict(width=.5), colors=colors ,autopct='%1.1f%%',
        shadow=True, startangle=30,)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("Mesin dan Peralatan Listrik")


st.pyplot(fig1)

############## CHOROPLETH

df_ayam = pd.read_excel(fileayam)
header = df_ayam.iloc[1]
header = header.fillna(0)
df_ayam = df_ayam[2:]
df_ayam.columns = header.astype(np.int64)
df_ayam = df_ayam.replace('-',0)
df_ayam.rename(columns = {0:'Provinsi'}, inplace = True)
df_ayam.drop([36], axis=0, inplace=True)

df_sapi = pd.read_excel(filesapi)
header1 = df_sapi.iloc[1]
header1 = header1.fillna(0)
header1 = header1.astype(np.int64)
df_sapi = df_sapi[2:]
df_sapi.columns = header1
df_sapi = df_sapi.replace('-',0)
df_sapi.rename(columns = {0:'Provinsi'}, inplace = True)
df_sapi.drop([36], axis=0, inplace=True)

df_kebun = pd.read_excel(filekebun)
header2 = df_kebun.iloc[2]
header2 = header2.fillna(0)
header2 = header2.astype(np.int64)
df_kebun = df_kebun[3:]
df_kebun.columns = header2
df_kebun = df_kebun.replace('-',0)
df_kebun.drop([37], axis=0, inplace=True)

df_sawit = df_kebun.iloc[:, 1:14]
df_sawit = df_sawit[df_sawit.columns[::-1]]
df_sawit.insert(0,"Provinsi",df_kebun.iloc[:,0])

df_kelapa = df_kebun.iloc[:, 14:27]
df_kelapa = df_kelapa[df_kelapa.columns[::-1]]
df_kelapa.insert(0,"Provinsi",df_kebun.iloc[:,0])

df_karet = df_kebun.iloc[:, 27:40]
df_karet = df_karet[df_karet.columns[::-1]]
df_karet.insert(0,"Provinsi",df_kebun.iloc[:,0])

df_kopi = df_kebun.iloc[:, 40:53]
df_kopi = df_kopi[df_kopi.columns[::-1]]
df_kopi.insert(0,"Provinsi",df_kebun.iloc[:,0])

df_kakao = df_kebun.iloc[:, 53:66]
df_kakao = df_kakao[df_kakao.columns[::-1]]
df_kakao.insert(0,"Provinsi",df_kebun.iloc[:,0])

df_tebu = df_kebun.iloc[:, 66:79]
df_tebu = df_tebu[df_tebu.columns[::-1]]
df_tebu.insert(0,"Provinsi",df_kebun.iloc[:,0])

df_teh = df_kebun.iloc[:, 79:92]
df_teh = df_teh[df_teh.columns[::-1]]
df_teh.insert(0,"Provinsi",df_kebun.iloc[:,0])

df_temb = df_kebun.iloc[:, 92:105]
df_temb = df_temb[df_temb.columns[::-1]]
df_temb.insert(0,"Provinsi",df_kebun.iloc[:,0])


df_padi = pd.read_excel(filepadi)
header3 = df_padi.iloc[1]
header3 = header3.fillna(0)
header3 = header3.astype(np.int64)
df_padi = df_padi[2:]
df_padi.columns = header3
df_padi = df_padi.replace('-',0)
df_padi.drop([36], axis=0, inplace=True)
df_padii = df_padi.iloc[:, 7:]
df_padii.insert(0,"Provinsi",df_padi.iloc[:,0])

df_iktn = pd.read_excel(fileikan1)
header4 = df_iktn.iloc[2]
header4 = header4.fillna(0)
header4 = header4.astype(np.int64)
df_iktn = df_iktn[3:]
df_iktn.columns = header4
df_iktn = df_iktn.replace('-',0)
df_iktn = df_iktn.fillna(0)
df_iktn.drop([37], axis=0, inplace=True)
df_iktnn = df_iktn.iloc[:, 43:]
df_iktnn.insert(0,"Provinsi",df_iktn.iloc[:,0])

df_ikbd = pd.read_excel(fileikan2)
header5 = df_ikbd.iloc[2]
header5 = header5.fillna(0)
header5 = header5.astype(np.int64)
df_ikbd = df_ikbd[3:]
df_ikbd.columns = header5
df_ikbd = df_ikbd.replace('-',0)
df_ikbd = df_ikbd.fillna(0)
df_ikbd.drop([37], axis=0, inplace=True)
df_ikbdd = df_ikbd.iloc[:, 126:]
df_ikbdd.insert(0,"Provinsi",df_ikbd.iloc[:,0])

st.write("")
st.header("Indonesia Comodity Choropleth Map")
col1, col2 = st.columns([4,2])

with col1:
    option2 = st.selectbox(
     'Produksi Dalam Negeri',
     ("Daging Ayam", "Daging Sapi", "Sawit", "Kelapa", 
     "Karet","Kopi","Kakao","Tebu","Teh","Tembakau","Padi",
     "Ikan Tangkap","Ikan Budidaya",),
    key=1111)

if option2 == "Daging Ayam":
    option4 = df_ayam
elif option2 == "Daging Sapi":
    option4 = df_sapi
elif option2 == "Sawit":
    option4 = df_sawit
elif option2 == "Kelapa":
    option4 = df_kelapa
elif option2 == "Karet":
    option4 = df_karet
elif option2 == "Kopi":
    option4 = df_kopi
elif option2 == "Kakao":
    option4 = df_kakao
elif option2 == "Tebu":
    option4 = df_tebu
elif option2 == "Teh":
    option4 = df_teh
elif option2 == "Tembakau":
    option4 = df_temb
elif option2 == "Padi":
    option4 = df_padii
elif option2 == "Ikan Tangkap":
    option4 = df_iktnn
elif option2 == "Ikan Budidaya":
    option4 = df_ikbdd
else:
    option4 = None

with col2:
    yearr = []
    yearr.clear()
    for i in option4.columns[1:]:
        yearr.append(i)
    yearr2 = tuple(yearr)
    option3 = st.selectbox(
     'Komoditas Produksi',
     (yearr2),
     key=1233)

indonesia = mapfile
m = folium.Map(location=[0.7893, 113.9213], tiles='CartoDB positron',name="Light Map",
        zoom_start=5,
        attr='My Data Attribution')
folium.Choropleth(
    geo_data=indonesia,
    name="choropleth",
    data=option4,
    columns=['Provinsi', option3],
    key_on="feature.properties.state",
    fill_color="YlOrRd",
    fill_opacity=0.7,
    line_opacity=.1,
    legend_name="Produksi {} {} (Ribu Ton)".format(option2,option3),
).add_to(m)
folium.features.GeoJson(indonesia, name="LSOA Code",
                        popup=folium.features.GeoJsonPopup(fields=['state'])).add_to(m)
folium_static(m,width=1340, height=500)




df_kons = pd.read_excel(filekons)
df_konsum = df_kons.iloc[:, 1:5]
df_konsum = df_konsum[df_konsum.columns[::-1]]
df_konsum.insert(0,"Komoditas",df_kons.iloc[:,0])
header6 = df_konsum.iloc[2]
header6 = header6.fillna(0)
header6 = header6.astype(np.int64)
df_konsum = df_konsum[3:]
df_konsum.columns = header6
df_konsum = df_konsum.replace('-',0)
df_konsum = df_konsum.fillna(0)
df_konsum.rename(columns = {0:'Tahun'}, inplace = True)
padi = df_konsum.iloc[1]
umbi = df_konsum.iloc[7]
ikan = df_konsum.iloc[15]
daging = df_konsum.iloc[51]
telursusu = df_konsum.iloc[61]
sayur = df_konsum.iloc[71]
kacang = df_konsum.iloc[97]
buah = df_konsum.iloc[105]
minyak = df_konsum.iloc[119]
bahanminum = df_konsum.iloc[124]
bumbu = df_konsum.iloc[132]
tembakau = df_konsum.iloc[182]


st.header("Consumption")
col1, col2 = st.columns([4,2])

with col1:
    optionX = st.selectbox(
     'Konsumsi Dalam Negeri',
     ("Padi/Beras", "Umbi-umbian", "Ikan dan hewan laut", "Daging", 
     "Telur dan Susu","Sayur","Kacang","Buah","Minyak Goreng","Bahan Minuman (Kopi, Teh, Gula, dll.)",
     "Ragam Bumbu","Tembakau",),
    key=1111)

valueY = []
if optionX == "Padi/Beras":
    valueY.clear()
    optionY = padi
    for i in range(1,5):
        valueY.append(optionY.iloc[i])
elif optionX == "Umbi-umbian":
    valueY.clear()
    optionY = umbi
    for i in range(1,5):
        valueY.append(optionY.iloc[i])
elif optionX == "Ikan dan hewan laut":
    valueY.clear()
    optionY = ikan
    for i in range(1,5):
        valueY.append(optionY.iloc[i])
elif optionX == "Daging":
    valueY.clear()
    optionY = daging
    for i in range(1,5):
        valueY.append(optionY.iloc[i])
elif optionX == "Telur dan Susu":
    valueY.clear()
    optionY = telursusu
    for i in range(1,5):
        valueY.append(optionY.iloc[i])
elif optionX == "Sayur":
    valueY.clear()
    optionY = sayur
    for i in range(1,5):
        valueY.append(optionY.iloc[i])
elif optionX == "Buah":
    valueY.clear()
    optionY = buah
    for i in range(1,5):
        valueY.append(optionY.iloc[i])
elif optionX == "Minyak Goreng":
    valueY.clear()
    optionY = minyak
    for i in range(1,5):
        valueY.append(optionY.iloc[i])
elif optionX == "Bahan Minuman (Kopi, Teh, Gula, dll.)":
    valueY.clear()
    optionY = bahanminum
    for i in range(1,5):
        valueY.append(optionY.iloc[i])
elif optionX == "Ragam Bumbu":
    valueY.clear()
    optionY = bumbu
    for i in range(1,5):
        valueY.append(optionY.iloc[i])
elif optionX == "Tembakau":
    valueY.clear()
    optionY = tembakau
    for i in range(1,5):
        valueY.append(optionY.iloc[i])
else:
    optionY = None

fig3 = plt.figure(figsize=(20, 5), facecolor='#e8f4f0')
Year = [2018,2019,2020,2021]
plt.plot(Year,valueY)
locator = matplotlib.ticker.MultipleLocator()
plt.gca().xaxis.set_major_locator(locator)
formatter = matplotlib.ticker.StrMethodFormatter("{x:.0f}")
plt.gca().xaxis.set_major_formatter(formatter)
plt.title("{} (Rupiah/Kapita/Minggu)".format(optionX))
st.pyplot(fig3)
