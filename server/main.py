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
@app.route("/reviews", methods=['POST'])
def post_review():
    if request.method == "POST":
        try:
            # Extract data from request
            data = request.get_json()
            book_name = data.get("book_name")
            book_author = data.get("book_author")
            book_review = data.get("book_review")

            # Establish a database connection
            conn = db_conn()
            cur = conn.cursor()

            # Insert the review data into reviews table
            cur.execute(
                "INSERT INTO reviews (book_name, book_author, book_review) VALUES (%s, %s, %s)",
                (book_name, book_author, book_review)
            )

            # Commit the sql query to the database
            conn.commit()
            
            # Close cursor and connection
            cur.close()
            conn.close()

            # Return json object saying success
            return jsonify({"message": f"Review for {book_name} created successfully"}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500
        
# Get all reviews
@app.route("/reviews") # default method GET
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
                review = {
                    "book_name": record[1], # get all data from each tuple
                    "book_author": record[2],
                    "book_review": record[3]
                }
                reviews.append(review)
            
            cur.close()
            conn.close()

            return jsonify(reviews)
        except Exception as e:
            return jsonify({'error': str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)