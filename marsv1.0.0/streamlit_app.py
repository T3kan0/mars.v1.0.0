#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import streamlit as st
import pandas as pd
import time
from PIL import Image
import re
st.set_page_config(
    page_title="MARS",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="auto",
)


z, astep, logo = st.columns([0.20, 0.65, 0.15])
with z:
    #st.markdown('<img src = "/marsv1.0.0/static/reg.png" style="width:47%">', unsafe_allow_html=True)
    #st.write('📝')
    #st.markdown("<h1 style='text-align: left; color: darkred;'>📋✍🏽</h1>", unsafe_allow_html=True)
    st.markdown("![Alt Text](https://i.postimg.cc/05GkJpWY/reg.png)")
with astep:
    st.markdown("<h4 style='text-align: center; color: darkred;'>Academic Student Tutorial Excellence Programme🧑🏼‍🎓 👨🏽‍🎓</h4>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: darkred;'>merging attendance registers (MARS)</h2>", unsafe_allow_html=True)
    st.write("<h5 style='text-align: center; color: darkred;'>version: 1.0.0.</h5>", unsafe_allow_html=True)    
with logo:
    #st.markdown('<img src = "app/static/reg.png" style="width:100%">', unsafe_allow_html=True)
    #st.markdown("<h1 style='text-align: right; color: darkred;'>📋✍🏽</h1>", unsafe_allow_html=True)
    st.markdown("![Alt Text](https://i.postimg.cc/05GkJpWY/reg.png)")
    
col1, col2 = st.columns([0.60,0.40], gap='small')
with col1:
    st.markdown("![Alt Text](https://i.postimg.cc/x1KMp0Qr/ufslog.png)")
    #st.markdown('<img src = "app/static/logo3.png" style="width:90%">', unsafe_allow_html=True)
with col2:
    st.write('Welcome to the A_STEP Web Application ***MARS*** ***v.1.0.0***. This was developed for the merging of large weekly\
 attendance register files for the A_STEP in-house data team, as part of their weekly data pre-processing operations.')
    genre = st.radio(
    ":red[**How Would You Like MARS to Combine Your Files?**]💡",
    [":rainbow[**Concatinate**]", ":rainbow[**Right Join**]", ":rainbow[**Left Join:**]"],
    captions = ["Default: Stacking Files Atop One Another 📕📗📘➡️📚",
                "Combines Files Based on Columns in the Right File 👉🏾", "Combines Files Based on Columns in the Left File 👈🏾"])
st.sidebar.markdown("<h1 style='text-align: center; color: #090257;'>Centre for Teaching and Learning</h1>", unsafe_allow_html=True)
st.sidebar.markdown("![Alt Text](https://i.postimg.cc/gJzPdRYd/logio.png)")
#st.sidebar.markdown('<img src = "app/static/logio.jpeg" style="width:100%">', unsafe_allow_html=True)
st.sidebar.markdown("<h1 style='text-align: center; color: #090257;'>Instructions</h1>", unsafe_allow_html=True)



custom_css = """
<style>
.st-emotion-cache-0.eqpbllx4 {
    background-color: #EBF5FB;
    border: 2px solid #0E0153;
    padding: 20px;
    border-radius: 10px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

[data-testid="stExpander"] .streamlit-expanderContent {
    background-color: #FFFFFF;
    border: 2px solid #0072C9;
    padding: 20px;
    border-radius: 10px;
}

[data-testid="stFileUploader"] .st-emotion-cache-1v04i6n.ef3psqc11 {
    background-color: white;
    border: 2px solid #0072C9; /* Blue border color */
    color: #0072C9; /* Blue text color */
    border-radius: 5px;
}

/* Change the hover color when the button is hovered over */
[data-testid="stFileUploader"] .st-emotion-cache-1v04i6n.ef3psqc11:hover {
    background-color: #0072C9; /* Blue background color */
    color: white; /* White text color */
}

[data-testid="stFileUploader"] .st-emotion-cache-taue2i.e1b2p2ww15 {
    background-color: white;
    border: 2px solid #0072C9; /* Blue border color */
    border-radius: 10px;
}

[data-testid="stFileUploader"] .st-emotion-cache-taue2i.e1b2p2ww15 input[type="file"] {
    display: none;
}
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# Your expander element
with st.sidebar.expander(":blue[Read More ⤵️]"):
    st.write(':grey[**Prepare and Upload ***.xlsx*** or ***.csv*** Register Files**]')
    st.write('- :orange[Add Columns to the Uploaded Files ⤵️]')
    st.write('- :orange[Aggregate Register Files into Bulk File ⤵️]')
    st.write('- :orange[Remove Unwanted Columns ⤵️]')
    st.write('- :orange[Change Column Names ⤵️]')
    st.write('- :orange[Download the Aggregated File 🛸]')

    
bulk_files = st.sidebar.file_uploader(':blue[**Upload Files**:👇]',
                                     type=['xlsx', 'csv'],
                                     accept_multiple_files=True)

if bulk_files:
    st.sidebar.success('File Uploaded', icon="✅")
st.sidebar.markdown("<h1 style='text-align: center; color: #090257;'>About A_STEP</h1>", unsafe_allow_html=True)
with st.sidebar.expander(":blue[Read More ⤵️]"):
    st.write(':grey[The Academic Student Tutorial Excellence Programme (A_STEP) provides both face-to-face and blended tutorials for students. These tutorials are led by trained senior \
    UFS students across all 7 faculties on the Bloemfontein campus as well as the 4 faculties on QwaQwa campus.  The tutors themselves are\
    either under- or postgraduate students, thereby making communication easier between the relevant parties.  A_STEP sessions offer regular,\
    peer-facilitated sessions that occur out of class and after lectures, thereby integrating content with learning skills and study strategies.\
    The work covered and facilitated in the tutorial sessions is therefore embedded within the context of a particular discipline, which is dependent on the faculty.]')
st.sidebar.markdown("<h1 style='text-align: center; color: #090257;'>Contact CTL & A_STEP</h1>", unsafe_allow_html=True)
st.sidebar.write('📭 E: :orange[mbonanits@ufs.ac.za]')
st.sidebar.write('📭 E: :orange[emohoanyane@ufs.ac.za]')
st.sidebar.write('🌐 :blue[www.ufs.ac.za/ctl]')
st.sidebar.info(':red[ 🚩 Web App Developer:] Tekano Mbonani', icon="ℹ️")

col3, col4 = st.columns([.90,0.10], gap='small')
if 'column_choice' not in st.session_state:
    st.session_state['column_choice'] = 'SUBJECT'
#if bulk_files:
    #st.sidebar.success('File Uploaded', icon="✅")
if bulk_files is not None:
    n_files = []
    Names = []
    Sub = []
    Cat_Nb = []
    edited_files = []
    for j, uploaded_file in enumerate(bulk_files):
        if uploaded_file.type == 'text/csv':
            bytes_data = pd.read_csv(uploaded_file, sep=',')
            # Identify tutor columns based on a shared pattern using regular expressions
            pattern = r'\d+: '
            tutor_columns = [col for col in bytes_data.columns if re.match(pattern, col)]
            # Function to replace '1' with tutor names
            def replace_with_tutor_names(row):
                return [re.sub(pattern, '', col) for col in tutor_columns if row[col] == 1]
            # Apply the function to each row and create a new 'Selected Tutors' column
            bytes_data['Selected Tutors'] = bytes_data.apply(replace_with_tutor_names, axis=1)
            # Clean up the 'Selected Tutors' column by joining the tutor names
            bytes_data['Selected Tutors'] = bytes_data['Selected Tutors'].apply(lambda x: ', '.join(x) if x else 'None')
            col_name = uploaded_file.name
            types = uploaded_file.type
            sub = col_name[0:4]
            cat = col_name[4:8]
            n_files.append(bytes_data)
            Names.append(col_name)
            Sub.append(sub)
            Cat_Nb.append(cat)
        else:
            bytes_data = pd.read_excel(uploaded_file)
            # Identify tutor columns based on a shared pattern using regular expressions
            pattern = r'\d+: '
            tutor_columns = [col for col in bytes_data.columns if re.match(pattern, col)]
            # Function to replace '1' with tutor names
            def replace_with_tutor_names(row):
                return [re.sub(pattern, '', col) for col in tutor_columns if row[col] == 1]
            # Apply the function to each row and create a new 'Selected Tutors' column
            bytes_data['Selected Tutors'] = bytes_data.apply(replace_with_tutor_names, axis=1)
            # Clean up the 'Selected Tutors' column by joining the tutor names
            bytes_data['Selected Tutors'] = bytes_data['Selected Tutors'].apply(lambda x: ', '.join(x) if x else 'None')
            col_name = uploaded_file.name
            types = 'excel/xlxs'            
            sub = col_name[0:4]
            cat = col_name[4:8]
            n_files.append(bytes_data)
            Names.append(col_name)
            Sub.append(sub)
            Cat_Nb.append(cat)                        
            
    if len(n_files) == 1:
        with col3:
            st.write(':blue[Register ]',j+1)
            col3.write(bytes_data.head(3))
            col_n1 = bytes_data.columns
        with col4:
            st.write(':blue[Type : ]',types)
            #st.markdown('<img src = "app/static/tech.png" style="width:100%">', unsafe_allow_html=True)
            st.markdown("![Alt Text](https://i.postimg.cc/GtFMv9RX/tech.png)")
            
    elif len(n_files) >=2:
        col5, col6 = st.columns([.90, 0.10], gap='small')
        with col3:
            st.write(':blue[Register ]', j)
            col3.write(n_files[0].head(2))
            col_n1 = n_files[0].columns
        with col4:
            st.write(':blue[Type : ]',types)
            #st.markdown('<img src = "app/static/tech.png" style="width:100%">', unsafe_allow_html=True)
            st.markdown("![Alt Text](https://i.postimg.cc/GtFMv9RX/tech.png)")            
        with col5:
            st.write(':blue[Register ]',j+1)
            col5.write(n_files[1].head(2))
            col_n2 = n_files[1].columns
        with col6:
            st.write(':blue[Type : ]', types)
            #st.markdown('<img src = "app/static/tech.png" style="width:100%">', unsafe_allow_html=True)
            st.markdown("![Alt Text](https://i.postimg.cc/GtFMv9RX/tech.png)")            

              
    st.write(':blue[Number of Files Uploaded : ]', len(n_files))
    editer, selector, adder, explainer = st.columns([.30, .20, .20, 0.30], gap='small')
    with editer:   
        edits = st.radio(
    ":red[**How Would You Like MARS to Edit Your Files?**]💡",
    [":rainbow[**Add Columns**]", ":rainbow[**Remove Columns**]",":rainbow[**Change Column Names**]", ":rainbow[**Split & Duplicate Row Content**]"],
        captions = ["Add news columns in the data files 👨🏽‍🔧",
                "Filter data files by column names 👩🏽‍🔧",
                "Edit column names in data files 🛠️",
                   "Duplicate & Split rows 🛠️"])
    with selector:
        if edits == ":rainbow[**Add Columns**]":
            if len(n_files) == 0:
                st.write(' ')
            elif len(n_files) >=1:
                Add_more = st.button(':red[Add Columns:]')
                st.write(':orange[This option will add two more columns to the uploaded data files 👉🏾: ]')

    with adder:
         if edits == ":rainbow[**Add Columns**]":
            if len(n_files) == 0:
                st.write(' ')
            elif len(n_files) >=1:
                clm_dic = {'SUBJECT': Sub,
                           'CATALOG NBR': Cat_Nb}
                clm_df = pd.DataFrame.from_dict(clm_dic)
                st.write(clm_df.head(4))
    with explainer:
         if edits == ":rainbow[**Add Columns**]":
            if len(n_files) == 0:
                st.write(' ')
            elif len(n_files) >=1:
                if Add_more:
                    edited_files = []
                    for files, clm, clm_ent in zip(n_files, clm_df['SUBJECT'], clm_df['CATALOG NBR']):                        
                        files['SUBJECT'] = clm
                        files['CATALOG NBR'] = clm_ent
                        edited_files.append(files)
                        bulk = files.to_csv()
                    with st.spinner('Wait for it...'):
                        time.sleep(3)
                    st.success('Colums Successfully Added!', icon="✅")
                else:
                   st.write(' ')
    if len(n_files) == 0:
        st.write(' ')
    elif len(n_files) >=1:
        if edits == ":rainbow[**Add Columns**]":
            if Add_more:                               
                st.write(':blue[Register ]',j)
                st.write(edited_files[0].head(3))
    if edits == ":rainbow[**Remove Columns**]":
        with selector:
            if len(n_files) == 0:
                st.write(' ')
            elif len(n_files) >=1:
                Rem_more = st.button(':red[Remove Columns:]')
                st.write(':orange[This option will remove columns from the uploaded data files 👉🏾: ]')

        with adder:
            if len(n_files) == 0:
                st.write(' ')
            elif len(n_files) >=1:
                dtt = pd.read_csv('bulk_file.csv')
                lis = dtt.columns
                column_name = st.multiselect(
                    ':blue[Select Column Name: ⚙️]',
                     lis)
        with explainer:
            if len(n_files) == 0:
                st.write(' ')
            elif len(n_files) >=1:
                if Rem_more:
                    dropped = dtt.drop(columns=column_name)
                    progress_bar = st.progress(0)
                    for perc_completed in range(100):
                        time.sleep(0.001)
                    progress_bar.progress(perc_completed+1)
                    st.write(dropped.columns)
                    st.success('Columns Successfully Removed!', icon="✅")
    if len(n_files) == 0:
        st.write(' ')
    elif len(n_files) >=1:
        if edits == ":rainbow[**Remove Columns**]":
            if Rem_more:
                st.write(':blue[Edited File👇🏾]')
                st.write(dropped.head())
                dropped.to_csv('bulk_file1.csv')
                with open('bulk_file1.csv', "rb") as file:
                    btn = st.download_button(
                        label=":red[Download Edited File]",
                        data=file,
                        file_name='new_file.csv',
                        mime="file/csv"
              )
                
    if edits == ":rainbow[**Add Columns**]":                
        aggreg = st.button(':red[Aggregate Files]')
        if aggreg:
            if len(n_files) == 0:
                st.error('Error❗:  No Files Uploaded 🤷🏽')
            elif len(n_files) == 1:
                st.warning(':red[Warning - Only A Single File Found ‼️]', icon="⚠️")
            elif len(n_files) >1:
                edited_files = []
                for files, clm, clm_ent in zip(n_files, clm_df['SUBJECT'], clm_df['CATALOG NBR']):
                    files['SUBJECT'] = clm
                    files['CATALOG NBR'] = clm_ent
                    edited_files.append(files)
                    new_file = pd.concat(edited_files)
                    new_f = new_file.to_csv('bulk_file.csv')
                progress_bar = st.progress(0)
                for perc_completed in range(100):
                    time.sleep(0.05)
                progress_bar.progress(perc_completed+1)
                st.write(':blue[Bulk/Aggregated File]')
                st.write(edited_files[0].head())
                #st.write(edited_files[0]['SUBJECT'].unique())
                st.success('Files Successfully Merged!', icon="✅")               
    
        if aggreg:
            with open('bulk_file.csv', "rb") as file:
                btn = st.download_button(
                    label=":red[Download Aggregated File]",
                    data=file,
                    file_name='new_file.csv',
                    mime="file/csv"
              )
        else:
            st.write(':blue[Press Aggregate Files to Continue]')
            
    if edits == ":rainbow[**Change Column Names**]":
        if len(n_files) == 0:
            st.info(':red[ 🚩 Remember to Upload Your Files] 🚩', icon="ℹ️")
            st.write(' ')
        elif len(n_files) >=1:
            st.write(' ')
            
            with selector:
                Rename = st.button(':red[Rename Columns:]')
                st.write(':orange[This option will remove columns from the uploaded data files 👉🏾: ]')                          
            with adder:
                renam = pd.read_csv('bulk_file1.csv')
                lis = renam.columns
                column_name = st.multiselect(
                    ':blue[Select Column to Rename: ⚙️]',
                     lis)
            with explainer:
                new_name = st.multiselect(
                    ':blue[Select New Column Name: ⚙️]',
                     ['SUBJECT', 'CATALOG NBR', 'STUDENT EMPLID',
                      'TUTOR EMPLID', 'TYPE', 'DATE', 'START TIME',
                      'END TIME', 'STUDENT NAME', 'STUDENT SURNAME', 'STUDENT NAMES'])
                if Rename:
                    progress_bar = st.progress(0)
                    for perc_completed in range(100):
                        time.sleep(0.005)
                    progress_bar.progress(perc_completed+1)
                    st.success('Files Successfully Edited!', icon="✅") 
        
        if len(n_files) == 0:
            st.write(' ')
        elif len(n_files) >=1:
            if Rename:
                for New_name, Old_name in zip(new_name, column_name):
                    renam.columns = renam.columns.str.replace(Old_name, New_name)
                st.write(':blue[Edited Bulk/Aggregated File]')
                st.write(renam.head())                        
                renam.to_csv('final.csv')
                with open('final.csv', "rb") as file:                                   
                    btn = st.download_button(
                        label=":red[Download Aggregated File]",
                        data=file,
                        file_name='new_file.csv',
                        mime="file/csv"
                  )
                st.info(':orange[Well Done!! Ready to Split Rows with Paired Tutors.]', icon="ℹ️")
    if edits == ":rainbow[**Split & Duplicate Row Content**]":
        if len(n_files) == 0:
            st.write(' ')
        elif len(n_files) >=1:
            with selector:
                Add_btn = st.button('Edit Rows')
                st.write(':orange[This option will separate rows of paired tutors 👉🏾: ]') 
            with adder:
                d = pd.read_csv('final.csv', sep=',')
                renam = pd.DataFrame(d)
                st.write(renam['TUTOR EMPLID'].head(6))
            with explainer:
                if Add_btn:
                    # Split and duplicate tutors
                    # Define the split_and_duplicate function
                    def split_and_duplicate(row):
                        new_rows = []
                        student_columns = [col for col in renam.columns if col != 'TUTOR EMPLID']

                        # Convert 'TUTOR EMPLID' to string and then split
                        tutor_emplids = str(row['TUTOR EMPLID']).split('&') if '&' in str(row['TUTOR EMPLID']) else str(row['TUTOR EMPLID']).split(', ')

                        for tutor_emplid in tutor_emplids:
                            new_row = {col: row[col] for col in student_columns}
                            new_row['TUTOR EMPLID'] = tutor_emplid
                            new_rows.append(new_row)

                        return pd.DataFrame(new_rows)



                    # List of columns to process
                    columns_to_process = renam.columns
                    result_df = renam  # Initialize the result DataFrame with the original data
                    result_df = pd.concat(result_df.apply(split_and_duplicate, axis=1).tolist(), ignore_index=True)

                    with st.spinner('Wait for it...'):
                        time.sleep(3)
                    progress_bar = st.progress(0)
                    for perc_completed in range(100):
                        time.sleep(0.005)
                    progress_bar.progress(perc_completed+1)
                    st.success('Files Successfully Edited!', icon="✅")
            if Add_btn:
                st.write(':blue[Bulk/Aggregated File]')
                st.write(result_df.head())
                result_df.to_csv('final.csv')
                with open('final.csv', "rb") as file:                                   
                    btn = st.download_button(
                        label=":red[Download Aggregated File]",
                        data=file,
                        file_name='new_file.csv',
                        mime="file/csv"
                  )

    else:    
        st.info(':red[ 🚩 Remember to Upload Your Files] 🚩', icon="ℹ️")

