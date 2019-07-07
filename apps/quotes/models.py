from django.db import models
from ..users.models import User


# Create your models here.
class QuoteManager(models.Manager):
    def validate(self, form_data):
        errors = []

        if len(form_data["author"]) < 3:
            errors.append("author's name must be at least 3 characters long.")
        if len(form_data["quote"]) < 10:
            errors.append("quote must be more than 10 characters long. ")
        if len(form_data["quote"]) > 255:
            errors.append("quote must be less than 255 characters")

        return errors

    def create_quote(self, form_data, user_id):
        user = User.objects.get(id=user_id)
        Quote.objects.create(
            author=form_data["author"], quote=form_data["quote"], creator=user
        )

    def update(self, form_data, quote_id):
        quote = self.get(id=quote_id)
        quote.author = form_data["author"]
        quote.quote = form_data["quote"]
        quote.save()

    def add_like(self, user_id, quote_id):
        user = User.objects.get(id=user_id)
        quote = Quote.objects.get(id=quote_id)
        user.liked.add(quote)
        user.save()


    def remove_like(self, user_id, quote_id):
        user = User.objects.get(id=user_id)
        quote = Quote.objects.get(id=quote_id)
        user.liked.remove(quote)

class Quote(models.Model):
    author = models.CharField(max_length=255)
    quote = models.TextField(blank=True, null=True)
    posted_quote = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name="liked")
    creator = models.ForeignKey(User, related_name="quotes", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = QuoteManager()

    def __repr__(self):
        return "<User: %s>" % self.first_name

    def __str__(self):
        return "<User: %s>" % self.first_name
