import streamlit as st
import math
import time

# Initialize session state for history and memory
if 'history' not in st.session_state:
    st.session_state.history = []
if 'memory' not in st.session_state:
    st.session_state.memory = 0

# Function to perform basic operations
def basic_calc(a, b, op):
    try:
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            if b == 0:
                raise ValueError("Division by zero")
            return a / b
        else:
            raise ValueError("Invalid operation")
    except Exception as e:
        return str(e)

# Function for scientific operations
def scientific_calc(value, func):
    try:
        if func == 'sqrt':
            if value < 0:
                raise ValueError("Square root of negative number")
            return math.sqrt(value)
        elif func == 'square':
            return value ** 2
        elif func == 'cube':
            return value ** 3
        elif func == 'sin':
            return math.sin(math.radians(value))
        elif func == 'cos':
            return math.cos(math.radians(value))
        elif func == 'tan':
            return math.tan(math.radians(value))
        elif func == 'log':
            if value <= 0:
                raise ValueError("Log of non-positive number")
            return math.log10(value)
        elif func == 'ln':
            if value <= 0:
                raise ValueError("Ln of non-positive number")
            return math.log(value)
        elif func == 'exp':
            return math.exp(value)
        elif func == 'factorial':
            if not isinstance(value, int) or value < 0:
                raise ValueError("Factorial of negative or non-integer")
            return math.factorial(int(value))
        elif func == 'inv':
            if value == 0:
                raise ValueError("Inverse of zero")
            return 1 / value
        else:
            raise ValueError("Invalid function")
    except Exception as e:
        return str(e)

# Main app
st.set_page_config(page_title="Advanced Calculator", page_icon="🧮", layout="wide")

# Theme toggle
theme = st.sidebar.selectbox("Theme", ["Light", "Dark"])
if theme == "Dark":
    st.markdown("""
    <style>
    body { background-color: #121212; color: white; }
    .stButton>button { background-color: #333; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🧮 Advanced Calculator")
st.markdown("A feature-rich calculator from basic to scientific operations.")

# Tabs for organization
tab1, tab2, tab3 = st.tabs(["Basic Calculator", "Scientific Calculator", "History & Memory"])

with tab1:
    st.header("Basic Operations")
    col1, col2, col3 = st.columns(3)
    with col1:
        a = st.number_input("Enter first number", value=0.0, key="a")
    with col2:
        op = st.selectbox("Operation", ["+", "-", "*", "/"], key="op")
    with col3:
        b = st.number_input("Enter second number", value=0.0, key="b")
    
    if st.button("Calculate", key="calc_basic"):
        result = basic_calc(a, b, op)
        st.success(f"Result: {result}")
        st.session_state.history.append(f"{a} {op} {b} = {result}")
        time.sleep(0.5)  # Brief delay for UX

with tab2:
    st.header("Scientific Operations")
    col1, col2 = st.columns(2)
    with col1:
        value = st.number_input("Enter value", value=0.0, key="value")
    with col2:
        func = st.selectbox("Function", ["sqrt", "square", "cube", "sin", "cos", "tan", "log", "ln", "exp", "factorial", "inv"], key="func")
    
    if st.button("Calculate", key="calc_sci"):
        result = scientific_calc(value, func)
        st.success(f"Result: {result}")
        st.session_state.history.append(f"{func}({value}) = {result}")
        time.sleep(0.5)

with tab3:
    st.header("Calculation History")
    if st.session_state.history:
        for entry in reversed(st.session_state.history[-10:]):  # Show last 10
            st.write(entry)
    else:
        st.write("No history yet.")
    
    st.header("Memory Functions")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("M+", key="m_plus"):
            st.session_state.memory += float(st.session_state.get('last_result', 0))
            st.success(f"Memory: {st.session_state.memory}")
    with col2:
        if st.button("M-", key="m_minus"):
            st.session_state.memory -= float(st.session_state.get('last_result', 0))
            st.success(f"Memory: {st.session_state.memory}")
    with col3:
        if st.button("MR", key="mr"):
            st.info(f"Memory Recall: {st.session_state.memory}")
    with col4:
        if st.button("MC", key="mc"):
            st.session_state.memory = 0
            st.success("Memory Cleared")

# Footer
st.markdown("---")
st.markdown("Built with Streamlit. Refresh to clear history.")
st.markdown("© 2024 Advanced Calculator App")
