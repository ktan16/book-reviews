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
            return jsonify({"message": "Review created successfully"}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)