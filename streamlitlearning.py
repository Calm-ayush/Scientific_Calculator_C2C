import streamlit as lit
lit.title("this is title")
lit.write("Hi i am ayush")
lit.header("this is header")
lit.subheader("this is subheader")
lit.text("this is text")
lit.markdown("This is md")
lit.caption("this is caption")
lit.code("print('Hello Ayush')")
lit.latex("a+b=c")

#input
lit.button("this is a button")
lit.checkbox("this is a checkbox")
lit.radio("this is a radio",["a","b"])
lit.selectbox("this is a selectbox",["a","b"])
lit.multiselect("this is a multiselect",["a","b"])
lit.slider("this is a slider")
lit.number_input("enter no")
lit.text_input("enter text")
lit.text_area("this is a textarea")
lit.date_input("enter date")
lit.time_input("enter time")
lit.file_uploader("upload a file")

#data display