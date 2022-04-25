import streamlit as st

st.title("Calculator")
st.title('''
''')
col1, col2, col3 = st.beta_columns(3)

button9 = col3.button("9")
button8 = col2.button("8")
button7 = col1.button("7")
button6 = col3.button("6")
button5 = col2.button("5")
button4 = col1.button("4")
button3 = col3.button("3")
button2 = col2.button("2")
button1 = col1.button("1")
buttonM = col3.button("-")
button0 = col2.button("0")
buttonP = col1.button("+")

#var1 = col1.subheader('')
#modifier = col2.subheader('')
#var2 = col3.subheader('')

if button9:
    var1 = var1 = col1.subheader('9')

if button8:
    var1 = var1 = col1.subheader('8')

if button7:
    var1 = var1 = col1.subheader('7')

if button6:
    var1 = var1 = col1.subheader('6')

if button5:
    var1 = var1 = col1.subheader('5')

if button4:
    var1 = var1 = col1.subheader('4')

if button3:
    var1 = var1 = col1.subheader('3')

if button2:
    var1 = var1 = col1.subheader('2')

if button1:
    var1 = var1 = col1.subheader('1')

if button0:
    var1 = var1 = col1.subheader('0')

if buttonP:
    modifier = col2.subheader('+')

if buttonM:
    modifier = col2.subheader('-')
