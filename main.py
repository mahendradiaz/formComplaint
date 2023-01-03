import streamlit as st
import mysql.connector
import os

# Koneksikan ke database
conn = mysql.connector.connect(user='root', password='', host='localhost', database='complaint')
conn1 = mysql.connector.connect(user='root', password='', host='localhost', database='complaint')

# Buat cursor
cursor = conn.cursor()
cursor1 = conn1.cursor()
# cursor2 = conn2.cursor()

# Eksekusi perintah SQL
query = "SELECT * FROM complaintDB"
cursor.execute(query)


# Ambil hasil
result = cursor.fetchall()

# Tampilkan hasil
if conn == False:
    print("Tidak Terhubung ke Database!")
else :
    print("Terhubung!")




# addSidebar = st.sidebar.selectbox(
#     "MENU",
#     ("Dashboard", "Pembelian", "Penjualan") 
# )


# MENU DATABASE
# if addSidebar == "Database":
    # st.title("Dashboard")

    # idList = []
    # produkList = []
    # kategoriList = []
    # unitList = []

    # for i in result:
    #     id_produk = i[0]   
    #     idList.append(id_produk)
    #     produk = i[1]
    #     produkList.append(produk)
    #     kategori = i[2]
    #     kategoriList.append(kategori)
    #     unit = i[3]
    #     unitList.append(unit)
    # df = pd.DataFrame(data=result)
    # st.dataframe(df)

# MENU PEMBELIAN
# elif addSidebar == "Pembelian":

st.title("Form Complaint Serambi Temu")

   
# INSERT DATABASE
query2 = "SELECT * FROM complaintDB WHERE id=%s"
sql = "INSERT INTO complaintDB (nama,email,kategori,filename,keterangan) VALUES (%s, %s, %s, %s, %s)"
    
    
#INPUT FORM 
with st.form(key="formComplaint", clear_on_submit=True):
    value1 = st.text_input("Nama", placeholder="Your answer")
    value2 = st.text_input("Email", placeholder="Your answer")
    value3 = st.selectbox("Kategori", ("Pilih Kategori", "Product / Menu", "Service / Waiter", "Fasilitas", "Lainnya"))
    value4 = st.file_uploader("Upload Gambar", type=['png','jpeg','jpg'])    
    value5 = st.text_area("Suggestions for improvement", placeholder="Your answer")
    simpan = st.form_submit_button(label= "Simpan")

    if value4 is not None :
        val = (value1,value2,value3,value4.name,value5) 
    
    # VALIDASI FORM INPUT
    if value1 is None :
        if simpan :
            st.error("Input Data dengan benar!")
    elif value2 is None:
        if simpan :
            st.error("Input Data dengan benar!")
    elif value3 == "Pilih Kategori" :
        if simpan :
            st.error("Input Data dengan benar!")
    elif value3 is None:
        if simpan :
            st.error("Input Data dengan benar!")
    elif value4 is None:
        if simpan :
            st.error("Input Data dengan benar!")
    else :
        if simpan:
            cursor1.execute(sql, val)
            conn1.commit()
            conn1.close()
            with open(os.path.join("imgComplaint", value4.name),"wb") as f:
                f.write(value4.getbuffer())
            st.success("Data Berhasil Disimpan")
            print("Data Berhasil Ditambahkan!")
# Tutup koneksi
conn.close()