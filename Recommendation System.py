#RECOMMENDATION SYSTEM (BOOKS)
 
# Sample data: books and their genres
books_data = {
    "To Kill a Mockingbird": ["Fiction", "Novel"],
    "Pride and Prejudice": ["Romance", "Fantasy"],
    "1984": ["Social Fiction"],
    "The Silent Patient": ["Mystery", "Thriller"],
    "Brave New World": ["Science Fiction", "Novel"],
    "Doing Harm": ["Horror", "Thriller"],
    "Only One Survive": ["Mystery", "Horror"]
}

# User preferences (genres they like)
user_preferences = ["Thriller", "Mystery"]

# Content-based filtering: Recommend books based on genre similarity
def content_based_filtering(user_prefs, books_data):
    genre_scores = {}
    for book, genres in books_data.items():
        score = sum(1 for pref in user_prefs if pref in genres)
        genre_scores[book] = score
    sorted_books = sorted(genre_scores, key=genre_scores.get, reverse=True)
    return sorted_books[:4]

# Get content-based filtering recommendations
content_based_recommendations = content_based_filtering(user_preferences, books_data)
print("\nContent-Based Filtering Recommendations:")
for book in content_based_recommendations:
    print(f"- {book}")