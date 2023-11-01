import streamlit as st 
import datetime
st.set_page_config(page_title='form',layout='wide') 

def AgeCaluculator(birthday):
    try:
        today = datetime.date.today()
        month,day,year = birthday.split('-')
        if  today.month <= int(month):
            if today.day < int(day):
                s = 1 
            else:
                s = 0
        else: 
            s = 0 
        # print('you are ',today.year - int(year) - s , 'years old') 
        st.write('you are {} old'.format(today.year-int(year)-s))

        # print(today.year,year,s)

    except ValueError as e:
        st.write(e)




def MotherAgeCaluculator(birthday,motherBirthday):
    try:
        mday,mmonth,myear = motherBirthday.split('-') 
        month,day,year = birthday.split('-')
        if  int(month) <= int(mmonth):
            if int(day) < int(mday):
                m = 1 
            else:
                m = 0
        else: 
                m = 0 

        print('my mother age when i was born ',int(year) - int(myear) - m)
        st.write('my mother age when i was born {}'.format(int(year)-int(myear)-m))

    except ValueError as e:
        st.write(e)


def daysLeftForMyBirthday(birthday):
    try:
        today = datetime.date.today()
        print(today)
        month,day,year = birthday.split('-')
        if today.month == int(month) and today.day >= int(day) or today.month > int(month):
            if month == 2 and day == 29:
                y = today.year
                leap =  today.year % 400 == 0 and today.year % 100 != 0 or today.year % 4 == 0 
            
                while not leap:
                    y = y + 1 
                    leap =  y % 400 == 0 and y % 100 != 0 or y % 4 == 0 
            
                nextbirthday = y
            else:
                nextbirthday = today.year + 1
        
        else:
            nextbirthday = today.year  
        
        value = datetime.date(nextbirthday,int(month),int(day))
       
        st.write('number of days left for your birthday is {}'.format(value-today))
    except ValueError as e:
        st.write(e) 


def daysLeftForMyMotherBirthday(motherBirthday):
    try:
        today = datetime.date.today()
        print(today)
        month,day,year = motherBirthday.split('-')
        if today.month == int(month) and today.day >= int(day) or today.month > int(month):
            if month == 2 and day == 29:
                y = today.year
                leap =  today.year % 400 == 0 and today.year % 100 != 0 or today.year % 4 == 0 
            
                while not leap:
                    y = y + 1 
                    leap =  y % 400 == 0 and y % 100 != 0 or y % 4 == 0 
            
                nextbirthday = y
            else:
                nextbirthday = today.year + 1
        
        else:
            nextbirthday = today.year  
        
        value = datetime.date(nextbirthday,int(month),int(day))
        st.write('number of days left for my mother birthday birthday is {}'.format(value-today))
    except ValueError as e:
        st.write(e)



# st.subheader('Hello welcome to the app')
# st.title('BRUCE WAYNE ENTRIPRISES') 
# st.write('its not who i am underneath but what i do that defines me') 
# st.write('batman vs superman dawn of justice')   

st.markdown("<h1>User Registration</h1>",unsafe_allow_html=True)
with st.form('form2'):
        birthday =  st.text_input('birthday') 
        motherBirthday = st.text_input('motherBirthday')
        submit_button = st.form_submit_button('submit') 
if submit_button:
        one = birthday
        two = motherBirthday
        AgeCaluculator(one)
        MotherAgeCaluculator(one,two)
        daysLeftForMyBirthday(one)
        daysLeftForMyMotherBirthday(two)

  






# form.text_input('firstname')
# form.form_submit_button("submit")