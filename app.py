import streamlit as st
# Eda packages

import pandas as pd
import numpy as np

#Data viz packages

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")

#function

def main():
    
    title_container1 = st.container()
    col1, col2 ,  = st.columns([6,12])
    from PIL import Image
    image = Image.open('static/asia.jpeg')
    with title_container1:
        with col1:
            st.image(image, width=200)
        with col2:
            st.markdown('<h1 style="color: red;">ASIA Consulting</h1>',
                           unsafe_allow_html=True)
    
    
    st.subheader("**Dealing with Dates**")
    
    
    
    st.sidebar.image("static/BMI.jpg", use_column_width=True)
    activites = ["About","Handling Dates","Creating features","Age Calculation","Difference"]
    choice =st.sidebar.selectbox("Select Activity",activites)
    
    st.text('------------------------------------------------------------------------------------------------------------------------------')
    

    if choice == "About":
        st.subheader("About ACS")
        st.text("""ACS is a consulting company specialized in data analysis was established during 2010. Our mission is to clarify the right direction for business owners in order to get better business results using very advanced statistical approaches, also, to support postgraduate students to prove their finding using academic statistical analysis. Providing the work in a high level of quality is one of our important goals. Our future vision is to be a leader in 
business analytics advisor for all successful business owners.
Our qualified staff is our strength of many of our successful projects. 
ACS did more than 100 successful projects since 2010/11. We are focusing on providing a 
sophisticated work with co-operated with our international parter. ACS has an international
agreement with Statistics Solutions (Ltd.) to be authorized for selling a statistical 
package in the GCC region, and that makes ACS more credible in statistical performance.""")
        
        st.subheader("About Mini projects")
        
        
        st.text("""we Have a vision to build Data science project which can help Data scientists
in their work.

""")
        st.write("**This Project is for Treating/fixing and generating features from the Date columns**")
        
 
        
        st.text('© Asia Consulting for Statistics')
#overall analysis    
    elif choice == "Handling Dates":

        st.subheader("1. Handling Dates")
        st.text("""Here in Handling Dates we can :
1. Fix the Dates
2. Download the clean Data in Format of YYYY:MM:DD
3. Download the clean Data in Format of YYYY:MM:DD HH:MM:SS
4. You can arrange Your Dates in Ascending order""")

        st.text('------------------------------------------------------------------------------------------------------------------------------')
        
        
        st.text('Upload the files to only fix the Dates')
        
        
    
        def get_df(file):
          # get extension and read file
          extension = file.name.split('.')[1]
          if extension.upper() == 'CSV':
            df = pd.read_csv(file)
          elif extension.upper() == 'XLSX':
            df = pd.read_excel(file)
          
          return df
        file = st.file_uploader("Upload file", type=['csv' 
                                                 ,'xlsx'])
        if not file:
            st.write("Upload a .csv or .xlsx file to get started")
            return
        st.write("**Data has been loaded Successfully**")
        
        df = get_df(file)
        if st.checkbox("Show Raw Data"):
            st.write(df.head())
        
        
        st.write("**1. Fix the Dates / converting Dates in DateTime Format**")
        if st.checkbox("Lets Treat the Date Column of your Choice"):
            
            st.subheader("Fix your Dates")
            all_columns=df.columns.to_list()
            selected_columns= st.selectbox("Select Date Columns You want to fix", all_columns)
            #df[selected_columns]=pd.to_datetime(df[selected_columns],errors='coerce')
          
            
        st.write("**2. Download the clean Data in Format of YYYY:MM:DD**")
        if st.checkbox("Dates in the Format of YYYY-MM-DD"):
            df[selected_columns]=pd.to_datetime(df[selected_columns],errors='coerce')
            df[selected_columns]=df[selected_columns].dt.strftime("%Y-%m-%d")
            st.write(df.head())
            st.text("Download the Above Data table by clicking on Download CSV")
            st.download_button(label='Download CSV',data=df.to_csv(),mime='text/csv')
        st.write("**3. Download the clean Data in Format of YYYY:MM:DD HH:MM:SS**")
        if st.checkbox("Dates in the Format of YYYY-MM-DD HH:MM:SS"):
            df[selected_columns]=pd.to_datetime(df[selected_columns],errors='coerce')
            df[selected_columns]=df[selected_columns].dt.strftime("%Y-%m-%d %H:%M:%S")
            st.write(df.head())
            st.text("Download the Above Data table by clicking on Download CSV")
            st.download_button(label='Download CSV',data=df.to_csv(),mime='text/csv')
        st.write("**4. Lets arrange our Dates in Ascending order**")
        
        if st.checkbox("Arranging Dates in Ascending order"):
            #all_columns=df.columns.to_list()
            #selected_columns= st.selectbox("Select Date Columns You want to fix", all_columns)
            if st.checkbox("Click here for Date Arranged in YYYY-MM-DD HH:MM:SS Format "):
                df[selected_columns] = df[selected_columns].astype('datetime64[ns]')
                df.sort_values(by=selected_columns, inplace=True,ignore_index=True)
                df[selected_columns]=df[selected_columns].dt.strftime("%Y-%m-%d %H:%M:%S")
                st.write(df.head())
                st.text("Download the Above Data table by clicking on Download CSV")
                st.download_button(label='Download CSV',data=df.to_csv(),mime='text/csv')
                
            if st.checkbox("Click here for Date Arranged in YYYY-MM-DD  Format "):
                df[selected_columns] = df[selected_columns].astype('datetime64[ns]')
                df.sort_values(by=selected_columns, inplace=True,ignore_index=True)
                df[selected_columns]=df[selected_columns].dt.strftime("%Y-%m-%d ")
                st.write(df.head())
                st.text("Download the Above Data table by clicking on Download CSV")
                st.download_button(label='Download CSV',data=df.to_csv(),mime='text/csv')
                
        st.text('------------------------------------------------------------------------------------------------------------------------------')
    elif choice=="Creating features":    
        st.subheader("2. Creating features")
        st.text("""Here in Creating features we can :
1. create Different types of featrues such as Year, Month, Day, hour, 
Minutes, seconds, Day of year
""")

        st.text('------------------------------------------------------------------------------------------------------------------------------')
        #@st.cache(allow_output_mutation=True)
    
        def get_df(file):
          # get extension and read file
          extension = file.name.split('.')[1]
          if extension.upper() == 'CSV':
            df = pd.read_csv(file)
          elif extension.upper() == 'XLSX':
            df = pd.read_excel(file)
          
          return df
        file = st.file_uploader("Upload file", type=['csv' 
                                                 ,'xlsx'])
        if not file:
            st.write("Upload a .csv or .xlsx file to get started")
            return
        st.write("**Data has been loaded Successfully**")
        
        df = get_df(file)
        if st.checkbox("Show Raw Data"):
            st.write(df.head())
      
        
        st.write("**1. Creating Different Features**")
        if st.checkbox("Create feature for Year, Month, Day, hour, Minutes, seconds, Day of year."):
            all_columns=df.columns.to_list()
            selected_columns= st.selectbox("Select Date Columns You want to Featurize", all_columns)
            df[selected_columns]=pd.to_datetime(df[selected_columns],errors='coerce')
            df[selected_columns]=df[selected_columns].dt.strftime("%Y-%m-%d %H:%M:%S")
            df[selected_columns]=pd.to_datetime(df[selected_columns],errors='coerce')
            df['year'] = df[selected_columns].dt.year
            df[selected_columns]=pd.to_datetime(df[selected_columns],errors='coerce')
            df['month'] = df[selected_columns].dt.month
            df[selected_columns]=pd.to_datetime(df[selected_columns],errors='coerce')
            df['Day'] = df[selected_columns].dt.day
            df[selected_columns]=pd.to_datetime(df[selected_columns],errors='coerce')
            df['Hour'] = df[selected_columns].dt.hour
            df[selected_columns]=pd.to_datetime(df[selected_columns],errors='coerce')
            df['Minute'] = df[selected_columns].dt.minute
            df[selected_columns]=pd.to_datetime(df[selected_columns],errors='coerce')
            df['Second'] =df[selected_columns].dt.second
            df[selected_columns]=pd.to_datetime(df[selected_columns],errors='coerce')
            df['Day of year']=df[selected_columns].dt.dayofyear
            df[selected_columns]=df[selected_columns].dt.strftime("%Y-%m-%d %H:%M:%S")
            st.write(df)
            st.text("Download the Above Data table by clicking on Download CSV")
            st.download_button(label='Download CSV',data=df.to_csv(),mime='text/csv')
    elif choice == "Age Calculation":    
        st.subheader("3. Creating Age Features / Age Calculation")
        st.text("""Here in Creating Age Features / Age Calculation we can :
1. we can Find individual Age by inputting Age in DD-MM-YYYY
2. will also Create different Age feature for our Data using by selecting the required Date Columns
""")
        st.text('------------------------------------------------------------------------------------------------------------------------------')
        st.write('**1. Find your Age**')
        if st.checkbox("Find your Age"):
            def ageCalculator(years, months, days,year,month,date):
                import datetime
                today = datetime.date(years,months,days)
                dob = datetime.date(year, month, date)
                years= ((today-dob).total_seconds()/ (365.242*24*3600))
                yearsInt=int(years)
                months=(years-yearsInt)*12
                monthsInt=int(months)
                days=(months-monthsInt)*(365.242/12)
                daysInt=int(days)
                st.write('**You are {0} years, {1} months, {2} days old.**'.format(yearsInt,monthsInt,daysInt))
            from datetime import datetime
            
            st.write("**Input your Date of Birth**")
            birthdate = st.text_input("Enter you Birthdate (dd-mm-yyyy) : ","01-01-1961")
            my_date = datetime.strptime(birthdate, "%d-%m-%Y")
            b_year = my_date.year
            b_month = my_date.month
            b_date = my_date.day
            now = datetime.now()
            
            # get year from date
            c_year = int(now.strftime("%Y"))
            
            # get month from date
            c_month = int(now.strftime("%m"))
            
            # get day from date
            c_date =int( now.strftime("%d"))
            ageCalculator(c_year,c_month,c_date,b_year,b_month,b_date)
            
        st.write("**2. Find Age By uploading the files**")
        def get_df(file):
          # get extension and read file
          extension = file.name.split('.')[1]
          if extension.upper() == 'CSV':
            df = pd.read_csv(file)
          elif extension.upper() == 'XLSX':
            df = pd.read_excel(file)
          
          return df
        file = st.file_uploader("Upload file", type=['csv' 
                                                 ,'xlsx'])
        if not file:
            st.write("Upload a .csv or .xlsx file to get started")
            return
        st.write("**Data has been loaded Successfully**")
        
        df = get_df(file)
        if st.checkbox("Show Raw Data"):
            st.write(df.head())
        if st.checkbox(" Find your age in Days,year,week,Months"):
            all_columns=df.columns.to_list()
            selected_columns= st.selectbox("Select Date Columns You want to Featurize", all_columns)
            df[selected_columns]=pd.to_datetime(df[selected_columns],errors='coerce')
            ds=pd.DataFrame()
            ds['dob']=df[selected_columns]
            # dropping the nat value if you see the unique value you will find the Nat value present i the data.
            ds=ds.dropna()
            # converting the data from timestamp format to string for calculation part.
            from datetime import datetime, date
            ds['DOB']=ds['dob'].dt.strftime('%d/%m/%Y')
            
   
            # Creating dataframe
            def age(born):
                born = datetime.strptime(born, "%d/%m/%Y").date()
                today = date.today()
                return today - born
            
            
            df['Age_Days'] = ds['DOB'].apply(age).dt.days
            df['Age_Years']= (df['Age_Days']/365).round(2)
            df['Age_Weeks']= (df['Age_Days']/7 ).round(2)
            df['Age_Months']= (df['Age_Days']/30.417 ).round(2)
            df[selected_columns]=df[selected_columns].dt.strftime("%Y-%m-%d %H:%M:%S")
            st.write(df.head())
            st.text("Download the Above Data table by clicking on Download CSV")
            st.download_button(label='Download CSV',data=df.to_csv(),mime='text/csv')
            
    elif choice == "Difference":    
        st.subheader("4. Finding Difference between Two Dates")
        st.text("""Here in Finding Difference between Two Dates we can :
1. we will find difference between Two Dates present in DataFile.
""")
        st.text('------------------------------------------------------------------------------------------------------------------------------')
        
        #@st.cache(allow_output_mutation=True)
    
        def get_df(file):
          # get extension and read file
          extension = file.name.split('.')[1]
          if extension.upper() == 'CSV':
            df = pd.read_csv(file)
          elif extension.upper() == 'XLSX':
            df = pd.read_excel(file)
          
          return df
        file = st.file_uploader("Upload file", type=['csv' 
                                                 ,'xlsx'])
        if not file:
            st.write("Upload a .csv or .xlsx file to get started")
            return
        st.write("**Data has been loaded Successfully**")
        
        df = get_df(file)
        if st.checkbox("Show Raw Data"):
            st.write(df.head())
        st.write('**1. Find Difference Between 2 Dates present in csv/xlsx file**')
        
        if st.checkbox("Find Difference between two Dates"):
            all_columns=df.columns.to_list()
            st.write('**Select 1st Column**')
            selected_columns1= st.selectbox("Select First Date Columns ", all_columns)
            df[selected_columns1]=pd.to_datetime(df[selected_columns1],errors='coerce')
            
            st.write('**Select 2nd Column**')
            selected_columns2= st.selectbox("Select Second Date Columns ", all_columns)
            df[selected_columns2]=pd.to_datetime(df[selected_columns2],errors='coerce')
            
            df['Days'] =  (df[selected_columns1]-df[selected_columns2]).dt.days
            df['Month'] = (df['Days']/30.417 ).round(2)
            df['Years']= (df['Days']/365).round(2)
            st.write(df)
            
            st.text("Download the Above Data table by clicking on Download CSV")
            st.download_button(label='Download CSV',data=df.to_csv(),mime='text/csv')
        st.text('This Dashboard has been implemented using streamlit & python packages. ')
            
            
        st.text('© American University of Kuwait')
        
        
      

if __name__=='__main__':
    main()
