import streamlit as st
import requests
from requests.exceptions import RequestException

# Configure default joke for error cases
DEFAULT_JOKE = {
    "setup": "Why did the programmer quit his job?",
    "punchline": "Because he didn't get arrays!"
}

# Fixed API endpoints and categories
CATEGORIES = {
    "🎲 Any Topic": "random",
    "💻 Programming": "programming/random",
    "🌍 General": "general/random",
    "🚪 Knock-Knock": "knock-knock/random"
}

BASE_URL = "https://official-joke-api.appspot.com/jokes/"

def get_random_joke(category_endpoint):
    """Fetch a random joke from the API with error handling"""
    try:
        url = f"{BASE_URL}{category_endpoint}"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        
        # Parse different response formats
        joke_data = response.json()
        if isinstance(joke_data, list):
            joke_data = joke_data[0] if len(joke_data) > 0 else DEFAULT_JOKE
            
        return {
            "setup": joke_data.get('setup', DEFAULT_JOKE['setup']),
            "punchline": joke_data.get('punchline', DEFAULT_JOKE['punchline'])
        }
        
    except (RequestException, KeyError, IndexError) as e:
        st.error(f"Error fetching joke: {str(e)}")
        return DEFAULT_JOKE

def main():
    st.title("😊 Random Joke Generator")
    st.markdown("Get ready to laugh! Select a category and click the button below!")
    
    # Initialize session state
    if 'show_punchline' not in st.session_state:
        st.session_state.show_punchline = False
    
    # Category selection
    selected_category = st.selectbox(
        "Choose your joke category:",
        list(CATEGORIES.keys()),
        help="Select your preferred joke category"
    )
    
    # Generate Joke button
    if st.button("🤖 Generate New Joke"):
        with st.spinner("📡 Contacting the joke satellite..."):
            category_endpoint = CATEGORIES[selected_category]
            joke = get_random_joke(category_endpoint)
            
            # Update session state with new joke
            st.session_state.current_joke = joke
            st.session_state.show_punchline = False
    
    # Display current joke
    if 'current_joke' in st.session_state:
        st.divider()
        st.subheader("Setup")
        st.markdown(f"*{st.session_state.current_joke['setup']}*")
        
        # Punchline reveal with animation
        if not st.session_state.show_punchline:
            if st.button("🔍 Reveal Punchline"):
                st.session_state.show_punchline = True
        else:
            st.subheader("Punchline")
            st.success(f"**{st.session_state.current_joke['punchline']}**")
            st.balloons()

if __name__ == "__main__":
    main()


