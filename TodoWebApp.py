import streamlit as st
import functions


todos= functions.read_todos()
st.set_page_config(layout="wide")

def add_todo():
    todo=st.session_state["new_todo"]+ "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("My To-do App")

st.subheader("This is my to-do app")
st.write("This app is to improve your <b>Productivity</b>",
        unsafe_allow_html=True)
a=st.text_input(label="",
                placeholder="Add new todo....",
                on_change=add_todo,
                key='new_todo')

for index,todo in enumerate(todos):
    checkbox= st.checkbox(todo, key=index+1)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[index+1]
        st.rerun()

st.write("For contacting developer email at tanishqmirdha2005@gmail.com",
        unsafe_allow_html=True)
st.write("Do not message <b>Unnecessarily</b>.Only message if you are facing any <b>problem<b>.",
        unsafe_allow_html=True)
st.write("Otherwise it can be problematic for \"You\"",
        unsafe_allow_html=True)





# st.session_state
# this above line is for developer use while developing
# frontend and connecting that with backend

