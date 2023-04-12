from django.contrib import admin
from .models import Menu
from django import forms

label_for_parent_title = 'Родительское меню'
class MenuFormAdmin(forms.ModelForm):
    parent_title = forms.ModelChoiceField(queryset=Menu.objects.all(), label=label_for_parent_title, required=False)

    class Meta:
        model = Menu
        fields = ['title', 'branch', 'url']
class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent_title', 'branch', 'url')
    search_fields = ('title', 'parent_title', 'branch')
    ordering = ('branch', 'title')
    form = MenuFormAdmin

    def parent_title(self, obj):
        obj.parent_title = Menu.objects.get(pk=obj.parent_id).title
        return obj.parent_title if obj.parent_title else "-"
    parent_title.short_description = label_for_parent_title


    def save_model(self, request, obj, form, change):
        if form.cleaned_data['parent_title']:
            parent_title = form.cleaned_data['parent_title']
            parent = Menu.objects.get(title=parent_title)
            obj.parent_id = parent.pk
            obj.branch = parent.branch
        else:
            obj.parent_id = None
        obj.save()

admin.site.register(Menu, MenuAdmin)
