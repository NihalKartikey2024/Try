import streamlit as st
import requests

def get_book_recommendations(query):
    url = f"http://openlibrary.org/search.json?q={query.replace(' ', '+')}"
    response = requests.get(url)
    data = response.json()
    docs = data.get('docs', [])

    recommendations = []
    for book in docs:
        title = book.get('title', 'No Title')
        authors = book.get('author_name', ['Unknown Author'])
        author = ', '.join(authors)
        cover_url = f"http://covers.openlibrary.org/b/id/{book.get('cover_i', '')}-M.jpg"
        rating = book.get('average_rating', 'N/A')
        recommendations.append((title, author, cover_url, rating))

    return recommendations

# Streamlit app
def app():
    st.header('Book Recommendation System')
    
    # Input for book title
    query = st.text_input('Enter a book title or keyword:')
    
    if st.button('Search'):
        if query:
            recommendations = get_book_recommendations(query)
            if recommendations:
                st.subheader('Recommendations:')
                num_columns = 2
                num_books = len(recommendations)
                num_rows = (num_books - 1) // num_columns + 1

                for i in range(num_rows):
                    book1, book2 = st.columns(2)
                    idx1 = i * num_columns
                    idx2 = idx1 + 1
                    if idx1 < num_books:
                        title1, author1, cover_url1, rating1 = recommendations[idx1]
                        with book1:
                            st.image(cover_url1, use_column_width=True)
                            st.write(f"**Title:** {title1}")
                            st.write(f"**Author:** {author1}")
                            st.write(f"**Rating:** {rating1}")
                            st.write("---")  # Add line separator
                    if idx2 < num_books:
                        title2, author2, cover_url2, rating2 = recommendations[idx2]
                        with book2:
                            st.image(cover_url2, use_column_width=True)
                            st.write(f"**Title:** {title2}")
                            st.write(f"**Author:** {author2}")
                            st.write(f"**Rating:** {rating2}")
                            st.write("---")  # Add line separator
            else:
                st.write('No recommendations found. Please try another query.')
        else:
            st.write('Please enter a book title or keyword.')

if __name__ == '__main__':
    app()
