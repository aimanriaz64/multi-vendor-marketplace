from django.shortcuts import render
from .forms import ReviewForm

def create_review(request):
    form = ReviewForm(request.POST or None)
    if form.is_valid():
        review = form.save(commit=False)
        review.author = request.user
        review.save()
    return render(request, 'reviews/review_form.html', {'form': form})
