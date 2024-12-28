import streamlit as st

def main():
    st.title("Vérification de Nombre Premier")
    n = st.number_input("Choisissez un nombre:", min_value=1, step=1)
    
    if n == 2:
        st.success("Ce nombre est premier.")
    elif n > 2:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                st.error("Ce nombre n'est pas premier.")
                break
        else:
            st.success("Ce nombre est premier.")
    else:
        st.error("Ce nombre n'est pas premier.")

if __name__ == "__main__":
    main()
    
