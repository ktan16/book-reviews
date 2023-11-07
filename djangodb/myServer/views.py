import json
from django.http import JsonResponse
from .models import Reviews, Bookgenres

# Create your views here.

# Post a review
def post_review(request):
    if request.method == "POST":
        try:
            # Exctract data from request
            data = json.loads(request.body)
            book_name = data.get("book_name")
            book_author = data.get("book_author")
            book_review = data.get("book_review")
            book_genres = data.get("book_genres")

            # Create a new review
            Reviews.objects.create(
                book_name=book_name,
                book_author=book_author,
                book_review=book_review
            )

            # Need to get the book_id
            new_review = Reviews.objects.get(
                book_name=book_name,
                book_author=book_author,
                book_review=book_review
            )
            book_id = new_review.pk

            # Add genres
            for genre_name in book_genres:
                Bookgenres.objects.create(
                    book_id=book_id,
                    genre_name=genre_name
                )

            return JsonResponse({"message": f"Review for {book_name} created successfully"}, status=201) 
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

# Get all reviews
def get_reviews(request):
    if request.method == "GET":
        try:
            reviews = Reviews.objects.all()
            reviews_data = []

            for review in reviews:
                genre_names = [
                    # 
                    genre.genre_name for genre in review.bookgenre_set.all() 
                ]
                
            return
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)