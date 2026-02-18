import streamlit as st
import random

def main():
    st.title("🔢 Roll Number Result Interface")
    st.write("Enter your roll number below to see your 5 assigned numbers.")

    # User Input
    roll_no = st.number_input("Enter Roll Number", min_value=1, step=1, value=1)

    if st.button("Generate My Numbers"):
        # Seeding ensures the same roll number always gets the same 5 numbers
        random.seed(roll_no)
        
        # Generate 5 unique numbers between 1 and 30
        results = random.sample(range(1, 31), 5)
        results.sort()  # Optional: sorts them for better readability

        st.success(f"Numbers for Roll No {roll_no}:")
        
        # Display numbers in a nice layout
        cols = st.columns(5)
        for i, num in enumerate(results):
            cols[i].metric(label=f"Number {i+1}", value=num)

if __name__ == "__main__":
    main()
