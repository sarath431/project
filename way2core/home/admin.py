from django.contrib import admin
from home.models import IoTListModel, CheckoutModel, Idea
# Register your models here.
class ProjAdmin(admin.ModelAdmin):
    list_display=['title','abstract','cost','diagram']
    prepopulated_fields={'slug':('title',)}
    ordering=['title']

class CheckAdmin(admin.ModelAdmin):
    list_display=['name','title','phno','Email','Orderdate']

class IdeaAdmin(admin.ModelAdmin):
    list_display=['name','phno','Email','message','diagram']

admin.site.register(IoTListModel,ProjAdmin)
admin.site.register(CheckoutModel, CheckAdmin)
admin.site.register(Idea, IdeaAdmin)
