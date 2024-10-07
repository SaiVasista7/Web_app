import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo=st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("My Todo App")
st.subheader("My First Todo App by Vasista")
st.write('This app is to improve your productivity.')

for index,todo in enumerate(todos):
    checkbox=st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        # This is to remove the todo from todo's list
        functions.write_todos(todos)
        del st.session_state[todo]
        # This is to remove the todo from session state
        st.rerun()


st.text_input(label="", placeholder="Enter a todo...", key="new_todo",on_change=add_todo,)

print("Hi")

#st.session_state
# this will provide the session state information.
