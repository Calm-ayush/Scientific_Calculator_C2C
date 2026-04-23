import streamlit as lit
import math

#session state (this helps so that whenever a new button is clicked the previous state of calculator remains and not get cleared)
if "currentstate" not in lit.session_state:
    lit.session_state.currentstate=""  #so if there is no last state it creates a new and starts code

def button(x):
    lit.session_state.currentstate+=str(x) #this adds the number pressed to the state

def reset():
    lit.session_state.currentstate="" #this clears the state when clear button is hit

def calculate():
    lit.session_state.currentstate = str(eval(lit.session_state.currentstate)) #this will take the string and tell python to treat it like actual code and calculate the expresision

def advanced(operation): #this will assign whatever operator we want to the function so when we call it we get answer for it
    y=float(lit.session_state.currentstate)

    if operation =="sin":
        lit.session_state.currentstate=str(math.sin(math.radians(y))) #using radian to convert
    elif operation=="cos":
        lit.session_state.currentstate=str(math.cos(math.radians(y)))
    elif operation=="tan":
        lit.session_state.currentstate=str(math.tan(math.radians(y)))
    elif operation =="log":
        lit.session_state.currentstate=str(math.log10(y))
    elif operation=="sqrt":
        lit.session_state.currentstate=str(math.sqrt(y))
    elif operation =="pow":
        lit.session_state.currentstate=str(y**2)
    else:
        print("error")
    
#ui
lit.title("Scientific Calculator")
lit.text_input("Enter numbers",lit.session_state.currentstate,disabled=True)


#layout of advanced keyboard
advanced_layout=[["sin","cos","tan","log","sqrt"],["x²","(",")","C"]]
for i,j in enumerate(advanced_layout):
    col=lit.columns(len(j)) #defining columns
    for v,w in enumerate(j):
        id_adv="adv_"+str(w)+"_"+str(i)+"_"+str(v) #this assigns each button a diff key so there is no error
        if w=="sqrt":
            col[v].button(w,on_click=advanced,args=("sqrt",),key=id_adv,use_container_width=True)
        elif w=="x²":
            col[v].button(w,on_click=advanced,args=("pow",),key=id_adv,use_container_width=True)
        elif w=="C":
            col[v].button(w,on_click=reset,key=id_adv,use_container_width=True)
        elif w=="=":
            col[v].button(w,on_click=calculate,key=id_adv,use_container_width=True)
        elif w in ["sin","cos","tan","log"]:
            col[v].button(w,on_click=advanced,args=(w,),key=id_adv,use_container_width=True)
        else:
            col[v].button(w,on_click=button,args=(w,),key=id_adv,use_container_width=True)
#layout of basic keyboard
basic_layout=[["7","8","9","+"],["4","5","6","-"],["1","2","3","*"],[".","0","=","/"]]

for i,j in enumerate(basic_layout):
    col=lit.columns(4) #defining columns
    for v,w in enumerate(j):
        id_basic="bas_"+str(w)+"_"+str(i)+"_"+str(v) #this assigns each button a diff key so there is no error
        if w =="=": #we need to call calculate function
            col[v].button(w,on_click=calculate,key=id_basic,use_container_width=True)
        else:
            col[v].button(w,on_click=button,args=(w,),key=id_basic,use_container_width=True)
