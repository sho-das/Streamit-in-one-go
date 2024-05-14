import streamlit as st
#Title
st.title('Title -> Hi World! Welcome to puzzle!')
#header
st.header('Header -> GeeksforGeeks')
#subheader
st.subheader('Title -> Hi Again!')
#Text
st.text('Text -> I am out of words')

#Markdowns/Headings H1 to H6
st.markdown('# Hi')
st.markdown('## Hi')
st.markdown('### Hi')
st.markdown('#### Hi')
st.markdown('##### Hi')
st.markdown('###### Hi')

#Success, Information,Warning,Error
st.success('Success!')
st.info('Information!')
st.warning('Warning!')
st.error('Error!')
st.exception(ZeroDivisionError("You cannot divide by Zero"))

#Help
st.help(ZeroDivisionError)

#Write and Code
st.subheader('Write and Code')
st.write("range(1,10)")
st.write(range(1,10))
st.write("3**2")
st.write(3**2)
st.code('x = 10\n'
        'for i in range(x):\n'
        '\tprint(i)')

#Checkboxes
#Without Validation
st.subheader('Checkbox')
st.checkbox('Male')
#With Validation ("Congrats on becoming an adult message when checkbox is clicked")
if(st.checkbox('Adult')):
        st.write('Congrats on becoming an adult')

#RadioButtons
#Validation in radiobutton
st.subheader('RadioButton')
radiobutton = st.radio('Select: ',("I'm above 18","I'm under 18","I'm 18"))
if(radiobutton == "I'm under 18"):
    st.write('You are not an adult!')
else:
    st.write('You are adult!')

#Select Box
st.subheader("SelectBox")
selectBox = st.selectbox("Options are:",['Data Science','Data Analysis','Web Scrapping','Image Processing'])
st.write("You've selected:", selectBox)

#Multi Select Box
#SelectBox
st.subheader("Multi-select Box")
multiselBox = st.multiselect("Options are:",['Data Science','Data Analysis','Web Scrapping','Image Processing'])
st.write("You've selected:", len(multiselBox), "courses which are:",multiselBox)

#Button
st.subheader("Button")
button_clicked = st.button("Click Me!")
if button_clicked:
    st.write("You've clicked me!")

#Slider
st.subheader("Slider")
st.write("You've selected:",st.slider("How happy are you with the experience?", 0,100,step = 10))

#TextInput and TextArea
st.subheader("Text Input")
st.text_input("Username :")
passText = st.text_input("Password :", type = "password")
if passText:
    st.write("I fooled you, I know the password is :", passText)
st.subheader("Text Area")
st.text_area("Write about yourself in the application")

#Input Number, Time and Date
st.subheader("Number Input")
st.number_input("Number")
st.subheader("Time Input")
st.time_input("Time")
st.subheader("Date Input")
st.date_input("Date")
