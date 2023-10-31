import psycopg2
from flask import Flask, request, jsonify

app = Flask(__name__)

# DB config
db_config = {
    "database": "BookReviews",
    "user": "postgres",
    "password": "postgres123",
    "host": "localhost",
    "port": "5432"
}

def db_conn():
    conn = psycopg2.connect(**db_config)
    return conn

# Post a review
@app.route("/reviews", methods=['POST']) # default method GET
def post_review():
    if request.method == "POST":
        try:
            # Extract data from request
            data = request.get_json()
            book_name = data.get("book_name")
            book_author = data.get("book_author")
            book_review = data.get("book_review")
            book_genres = data.get("book_genres")

            # Establish a database connection
            conn = db_conn()
            cur = conn.cursor()

            # Insert the review data into reviews table
            cur.execute(
                "INSERT INTO reviews (book_name, book_author, book_review) VALUES (%s, %s, %s) RETURNING book_id",
                (book_name, book_author, book_review)
            )

            # Retrieve the book_id
            book_id = cur.fetchone()[0]
            print(book_id)

            for genre_name in book_genres:
                cur.execute(
                    "INSERT INTO bookgenres (book_id, genre_name) VALUES (%s, %s)",
                    (book_id, genre_name)
                )
            
            # Commit the sql query to the database
            conn.commit()
            
            # Close cursor and connection
            cur.close()
            conn.close()

            # Return json object saying success
            return jsonify({"message": f"Review for {book_name} created successfully"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
# Get all reviews
@app.route("/reviews")
def get_reviews():
    if request.method ==  "GET":
        try:
            # Establish databse connection
            conn = db_conn()
            cur = conn.cursor()

            # SQL query
            cur.execute(
                "SELECT * FROM reviews"
            )

            # Fetch all reviews and put into list of dictionary
            review_records = cur.fetchall() # creates a list of tuples where tuples contain all data from columns
            reviews = []

            for record in review_records:
                # Retrieve genres
                book_id = record[0]
                genre_names = []
                cur.execute(
                    f"SELECT * FROM bookgenres WHERE book_id = {book_id}"
                )
                book_genres = cur.fetchall()
                if book_genres:
                    genre_names = [item[2] for item in book_genres]

                # Create a review entry
                review = {
                    "book_name": record[1], # get all data from each tuple
                    "book_author": record[2],
                    "book_review": record[3],
                    "book_genres": genre_names
                }
                reviews.append(review)
            
            cur.close()
            conn.close()

            return jsonify(reviews)
        except Exception as e:
            return jsonify({"error": str(e)}), 500

# Delete a review using book_id
@app.route("/reviews/<int:book_id>", methods=["DELETE"])
def delete_review(book_id):
    if request.method == "DELETE":
        try:
            conn = db_conn()
            cur = conn.cursor()

            cur.execute(
                "DELETE FROM reviews WHERE book_id = %s RETURNING book_name",
                (book_id,)
            )
            book_name = cur.fetchone()[0]

            cur.execute(
                "DELETE FROM bookgenres WHERE book_id = %s",
                (book_id,)
            )

            conn.commit()

            cur.close()
            conn.close()

            return jsonify({"message": f"Review for '{book_name}' deleted."}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)