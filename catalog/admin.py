from django.contrib import admin

# Register your models here.
from catalog.models import Author, Book, BookInstance, Genre


class BookInline(admin.TabularInline):
    model = Book
    extra = 0

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInline]

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    #TODO: See why this does not work ?!!
    #list_display = ('title', 'author', 'display_genre')
    list_display = ('title', 'author')
    inlines = [BooksInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

#admin.site.register(Author)
#admin.site.register(Book)
#admin.site.register(BookInstance)
#admin.site.register(Genre)

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

