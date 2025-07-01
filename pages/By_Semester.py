import streamlit as st
import requests

# Function to fetch and display GitHub Markdown content
def fetch_github_readme(url):
    # Convert GitHub page URL to raw content URL
    raw_url = url.replace('github.com', 'raw.githubusercontent.com').replace('/blob/', '/')
    response = requests.get(raw_url)
    if response.status_code == 200:
        return response.text
    else:
        return "Error: Unable to load content from GitHub."

def main():
    st.title('Digital Classroom')

    # Set up tabs
    tabs = st.tabs(["Spring 2025", "Fall 2024", "Spring 2024", "Fall 2023", "Spring 2023", "Additional Content"])

    # Spring 2025 content
    with tabs[0]:
    #    st.markdown("#### Courses offered in Spring 2025 semester")
        fall_url = 'https://github.com/MK316/spring2025/blob/main/README.md'
        fall_content = fetch_github_readme(fall_url)
        st.markdown(fall_content, unsafe_allow_html=True)
    
    # Fall 2024 content
    with tabs[1]:
    #    st.subheader("Fall 2024 Courses")
        fall_url = 'https://github.com/MK316/MK-316/blob/main/pages/fall2024.md'
        fall_content = fetch_github_readme(fall_url)
        st.markdown(fall_content, unsafe_allow_html=True)

    # Spring 2024 content
    with tabs[2]:
    #    st.subheader("Spring 2024 Courses")
        spring_url = 'https://github.com/MK316/MK-316/blob/main/pages/spring2024.md'
        spring_content = fetch_github_readme(spring_url)
        st.markdown(spring_content, unsafe_allow_html=True)

    # Additional Content tab (optional)
    with tabs[3]:
    #    st.subheader("Fall 2023 Courses")
        # Placeholder URL for additional content if needed
        # Uncomment and update the URL if you have content for this tab
        fall2023_url = 'https://github.com/MK316/Fall2023/blob/main/README.md'
        additional_content = fetch_github_readme(fall2023_url)
        st.markdown(additional_content, unsafe_allow_html=True)


    with tabs[4]:
        # st.subheader("Spring 2023 Courses")
        # Placeholder URL for additional content if needed
        # Uncomment and update the URL if you have content for this tab
        additional_url = 'https://github.com/MK316/Spring2023/blob/main/README.md'
        additional_content = fetch_github_readme(additional_url)
        st.markdown(additional_content, unsafe_allow_html=True)

    # Additional Content tab (optional)
    with tabs[5]:
        st.subheader("Additional Content")
        # Placeholder URL for additional content if needed
        # Uncomment and update the URL if you have content for this tab
        # additional_url = 'https://github.com/MK316/Coding4ET/blob/main/Lessons/Lesson02.md'
        # additional_content = fetch_github_readme(additional_url)
        # st.markdown(additional_content, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
