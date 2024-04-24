import streamlit as st
import requests

def get_top_books():
    url = "https://openlibrary.org/search.json"
    params = {
        "q": "*",
        "sort": "rating",
        "limit": 50  # Limit to 50 results
    }
    response = requests.get(url, params=params)
    data = response.json()
    docs = data.get('docs', [])

    top_books = []
    for book in docs:
        title = book.get('title', 'No Title')
        authors = book.get('author_name', ['Unknown Author'])
        author = ', '.join(authors)
        cover_url = f"https://covers.openlibrary.org/b/id/{book.get('cover_i', '')}-S.jpg"
        rating = book.get('average_rating', 'N/A')
        top_books.append((title, author, cover_url, rating))

    return top_books

def app():
    st.header("Top 50 Books")
    st.caption("Here are the top 50 books based on rating.")

    if st.button('Get Top 50 Book Recommendations'):
        top_books = get_top_books()
        if top_books:
            st.subheader('Top 50 Book Recommendations (Sorted by Rating):')
            for rank, (title, author, cover_url, rating) in enumerate(top_books, start=1):
                st.write(f"**Rank #{rank}**")
                st.image(cover_url, caption=title, width=100)
                st.write(f"**Title:** {title}")
                st.write(f"**Author:** {author}")
                st.write(f"**Rating:** {rating}")
                st.write('---')
        else:
            st.write('No recommendations found. Please try again later.')

# This part is important for running the app
if __name__ == '__main__':
    app()
