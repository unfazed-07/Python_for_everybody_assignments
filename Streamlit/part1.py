import streamlit as st
import os
st.write({"Hello":"nigga"})
st.write(True)
st.write(123)
4+8
"Hello World" if False else "bye"
pressed= st.button("Press ME")
print("FIrst",pressed)

pressed2=st.button("secondd Button")
print("Second", pressed2)

st.title("Super Simple title")
st.header("This is a header")
st.subheader("Subheader")
st.markdown("This is _nigga_")
st.caption("Small Text")
code_example="""
def greet(name):
    print("Hello", name)
"""
st.code(code_example, language="python")
st.divider()
st.image(os.path.join(os.getcwd(), "static", "jap.jpg"), width=200)
