def is_staff(user):
    return user.is_staff


def is_user(user):
    return user.id


def book_is_favorited(user, album):
    return user.favorite_books.filter(pk=album.pk).exists()