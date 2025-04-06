from django.contrib import admin
from.models import Enrollment,Contact,trainer,course,studyresources,Notice,Feedback,Query_Doubts

# Register your models here.
admin.site.register(Contact)
admin.site.register(Notice)
admin.site.register(Enrollment)
admin.site.register(trainer)
admin.site.register(course)
admin.site.register(studyresources)
admin.site.register(Feedback)
admin.site.register(Query_Doubts)


class Contact_Admin(admin.ModelAdmin):
    list_display=['name','email','question']

admin.site.site_header="Class Connect Admin Dashboard"
admin.site.site_title=" CLASS CONNECT "
admin.site.index_title="Connecting Minds, Shaping Futures"