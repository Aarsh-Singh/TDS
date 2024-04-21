import streamlit as st

def find_largest(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

def main():
    st.title("Find the Largest Number")
    
    st.write("Enter three numbers below:")
    num1 = st.number_input("Number 1", step=1)
    num2 = st.number_input("Number 2", step=1)
    num3 = st.number_input("Number 3", step=1)
    
    if st.button("Find Largest"):
        largest = find_largest(num1, num2, num3)
        st.success(f"The largest number is: {largest}")

if __name__ == "__main__":
    main()
