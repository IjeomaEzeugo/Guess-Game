import streamlit as st
import random

st.header("My Guessing Game")

img = st.image("mydice.gif")


b = st.number_input("Please input a number from 1 to 6")
a = random.randint(1,6)

def game(a,b):
    if b > 6:
         return("Invalid Input, Please select a number between 1 and 6")
    else:
         if a ==b:
           return("CORRECT")

         else:
             st.write(f"Your selected number is {b}")
             st.write(f"Random number is {a}")
             return("Wrong, Try Again")

if st.button("Try your luck"):
    st.write(game(a,b))