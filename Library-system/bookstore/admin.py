from django.contrib import admin
from bookstore.models import User,Book,Chat,DeleteRequest,Feedback


"""class UserAdmin(admin.ModelAdmin):
    list_display=['is_admin','is_publisher','is_librarian']
admin.site.register(User,UserAdmin)"""

class BookAdmin(admin.ModelAdmin):
    list_display=['title','author','year','publisher','desc','uploaded_by','user_id','pdf','cover']
admin.site.register(Book,BookAdmin)


class ChatAdmin(admin.ModelAdmin):
    list_display=['user','message','posted_at']
admin.site.register(Chat,ChatAdmin)



class DeleteAdmin(admin.ModelAdmin):
    list_display=['delete_request']
admin.site.register(DeleteRequest,DeleteAdmin)


class FeedbackAdmin(admin.ModelAdmin):
    list_display=['feedback']
admin.site.register(Feedback,FeedbackAdmin)
