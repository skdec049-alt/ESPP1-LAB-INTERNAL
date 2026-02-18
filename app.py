import streamlit as st
import random
import urllib.parse

def get_unique_sequences(total_rolls=60):
    all_numbers = list(range(1, 31))
    assignments = {}
    last_set = set()
    random.seed(42) 

    for roll in range(1, total_rolls + 1):
        available = [n for n in all_numbers if n not in last_set]
        current_set = random.sample(available, 5)
        current_set.sort()
        assignments[roll] = current_set
        last_set = set(current_set)
    return assignments

def main():
    st.set_page_config(page_title="Roll Number Portal", layout="centered")
    st.title("🔢 Unique Number Portal")
    
    roll_no = st.number_input("Enter Roll Number (1-60)", min_value=1, max_value=60, step=1)
    data_map = get_unique_sequences(60)

    if st.button("Generate My Numbers"):
        my_numbers = data_map[roll_no]
        st.session_state['generated_nums'] = my_numbers
        st.session_state['roll'] = roll_no

    # Display results if they exist in session state
    if 'generated_nums' in st.session_state:
        nums = st.session_state['generated_nums']
        roll = st.session_state['roll']
        
        st.write(f"### Results for Roll No: **{roll}**")
        cols = st.columns(5)
        for i, num in enumerate(nums):
            cols[i].metric(label=f"Value {i+1}", value=num)

        # --- WHATSAPP LOGIC ---
        # Create the message text
        msg_text = f"Hello! My Roll No is {roll}. My assigned numbers are: {', '.join(map(str, nums))}."
        
        # URL encode the message for the web link
        encoded_msg = urllib.parse.quote(msg_text)
        
        # Option A: User types their phone number to send it to themselves
        phone = st.text_input("Enter WhatsApp Phone Number (with country code, e.g., 919876543210)")
        
        if phone:
            whatsapp_url = f"https://wa.me/{phone}?text={encoded_msg}"
            st.link_button("📲 Send Result to WhatsApp", whatsapp_url)
        else:
            # Option B: Just open WhatsApp and let them pick a contact
            general_url = f"https://api.whatsapp.com/send?text={encoded_msg}"
            st.link_button("💬 Share via WhatsApp", general_url)

if __name__ == "__main__":
    main()
