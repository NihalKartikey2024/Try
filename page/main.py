import streamlit as st
st.set_page_config(
    page_title="My Page Title",
    initial_sidebar_state="auto",
    menu_items=None
)

import Home, cp, aboutus, contactus, Search_any, top_books

# Custom Sidebar Menu
def custom_sidebar_menu():
    st.sidebar.title("Menu")
    selected_page = st.sidebar.radio(
        "",
        ('Home', 'Books', 'Top_50_books', 'Search', 'About Us', 'Contact Us')
    )
    return selected_page

# Create an instance of the app 
class MultiApp():

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        selected_page = custom_sidebar_menu()

        if selected_page == "Home":
            Home.app()
        elif selected_page == "Books":
            cp.app()
        elif selected_page == "Top_50_books":
            top_books.app()
        elif selected_page == "Search":
            Search_any.app()
        elif selected_page == "About Us":
            aboutus.app()
        elif selected_page == 'Contact Us':
            contactus.app()

multi_app = MultiApp()

multi_app.add_app("Home", Home.app)
multi_app.add_app("Account", cp.app)
multi_app.add_app("About Us", aboutus.app)
multi_app.add_app("Contact Us", contactus.app)
multi_app.add_app("Top_50_books", top_books.app)
multi_app.add_app("Search", Search_any.app)

multi_app.run()
