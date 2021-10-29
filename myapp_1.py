import streamlit as st
import random
import string
def generate_random_password(characters,passwd_length =6):
    random.shuffle(characters)
    password= []
    for i in range (passwd_length):
        password.append(random.choice(characters))
    return("".join(password))

ALL_CHARACTERS_PATTERN = list(string.ascii_letters + string.digits + "!@#$%^&*()_+=")
AlPHANUMERIC_PATTERN = list(string.ascii_letters + string.digits)
ALPHABTES_PATTERN = list(string.ascii_letters)

def main():
    st.title("Password Generator App")
    st.subheader("Awsome Password Generator")
    
    menu = ["Random Password Generator","About"]
    choice = st.sidebar.selectbox("Random Password Generator",menu)
    
    if choice == "Random Password Generator":
        st.subheader("Random Password Generator")
        
        passwd_pattern_list = ['alphanumeric','alphabet','all']
        passwd_length = st.number_input("Password Length",min_value =5,max_value=20,value=6)
        password_pattern_choice = st.selectbox("Pattern",passwd_pattern_list)
        
        if st.button("Generate"):
            st.info("Random Password")
            
            if password_pattern_choice == 'alphabets':
                password_result = generate_random_password(ALPHABTES_PATTERN,passwd_length)
            elif password_pattern_choice == 'alphanumeric':
                password_result = generate_random_password(AlPHANUMERIC_PATTERN ,passwd_length)
            else:
                password_result = generate_random_password(ALL_CHARACTERS_PATTERN,passwd_length)
                
            #st.write(password_result)
            st.code(password_result)    
        
    else:
        st.subheader("About")
        st.markdown("Password Generator is open source app for generating secure passwords using cryptographically secure pseudo-random number generator. You are given options to choose which characters your password should contain or you can choose your set of a custom symbols. Generating passwords with Password Generator is fast and easy, just check options and hit a button.")
        st.subheader("About Author")
        st.markdown("Hi thanks for using passwd generator, for more awsome app please check my github https://maazirfan.github.io/me")
        
if __name__ =='__main__':
    main()


