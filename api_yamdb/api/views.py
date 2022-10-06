from django.shortcuts import render, get_object_or_404
from reviews.models import Review, Comment, Title
from .serializers import ReviewSerializer, CommentSerializer
from rest_framework import filters, status, viewsets


# Create your views here.

class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer

    # permission_classes =
    def get_queryset(self):
        title_id = self.kwargs.get('title_id')
        title = get_object_or_404(Title, id=title_id)
        return title.reviews.all()

    def perform_create(self, serializer):
        title_id = self.kwargs.get('title_id')
        title = get_object_or_404(Title, id=title_id)
        serializer.save(author=self.request.user, title=title)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    # permission_classes =

    def get_queryset(self):
        review_id = self.kwargs.get('review_id')
        review = get_object_or_404(Review, pk=review_id)
        return review.comments.all()

    def perform_create(self, serializer):
        review_id = self.kwargs.get('review_id')
        review = get_object_or_404(Review, pk=review_id)
        serializer.save(authot=self.request.user, review=review)
