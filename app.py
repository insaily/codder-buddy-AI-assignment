
import streamlit as st
from main import run_agent
from pathlib import Path
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Coder Buddy AI",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Coder Buddy AI")
st.caption("Describe your idea. Let AI build your website.")

if "generated_html" not in st.session_state:
    st.session_state.generated_html = ""

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.header("About Coder Buddy")
    st.write("Your AI software development assistant.")
    st.write("1. Plan your project")
    st.write("2. Design the architecture")
    st.write("3. Generate website code")
    st.divider()
    st.caption("Powered by LangChain, LangGraph and Groq")

left, right = st.columns([1, 1.4], gap="large")

with left:
    st.subheader("💬 Describe your idea")

    with st.form("website_form"):
        user_request = st.text_area(
            "What do you want to build?",
            placeholder="Example: Create a beautiful birthday website with animations, a photo gallery and a personal message.",
            height=180
        )

        generate = st.form_submit_button(
            "✨ Generate Website",
            use_container_width=True
        )

    if generate:
        if not user_request.strip():
            st.warning("Please describe your website idea first.")
        else:
            with st.spinner("Coder Buddy is planning, designing and coding..."):
                result = run_agent(user_request)

            if result.get("error"):
                st.error(result["error"])
            elif result.get("generated_files"):
                file_path = Path(result["generated_files"][0])

                if file_path.exists():
                    st.session_state.generated_html = file_path.read_text(
                        encoding="utf-8"
                    )
                    st.success("Website generated successfully!")
                else:
                    st.error("The generated HTML file could not be found.")

    if st.session_state.generated_html:
        st.download_button(
            "⬇️ Download HTML",
            data=st.session_state.generated_html,
            file_name="index.html",
            mime="text/html",
            use_container_width=True
        )

with right:
    st.subheader("🌐 Website Preview")

    if st.session_state.generated_html:
        components.html(
            st.session_state.generated_html,
            height=650,
            scrolling=True
        )
    else:
        st.info(
            "Your generated website will appear here. "
            "Enter your idea and click Generate Website."
        )
