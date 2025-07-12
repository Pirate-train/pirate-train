from django.contrib import admin
from .models import Game, MemoryOffset, Pointer, Trainer

class MemoryOffsetInline(admin.TabularInline):
    model = MemoryOffset
    extra = 1

class PointerInline(admin.TabularInline):
    model = Pointer
    extra = 1

class TrainerInline(admin.TabularInline):
    model = Trainer
    extra = 1

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'current_version', 'last_updated')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    inlines = [MemoryOffsetInline, PointerInline, TrainerInline]

@admin.register(MemoryOffset)
class MemoryOffsetAdmin(admin.ModelAdmin):
    list_display = ('description', 'game', 'offset', 'offset_type', 'version')
    list_filter = ('game', 'offset_type')
    search_fields = ('description', 'offset')

@admin.register(Pointer)
class PointerAdmin(admin.ModelAdmin):
    list_display = ('description', 'game', 'version')
    list_filter = ('game',)
    search_fields = ('description', 'pointer_path')

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('game', 'version', 'upload_date', 'is_approved')
    list_filter = ('is_approved', 'game')
    search_fields = ('game__title', 'version')
    actions = ['approve_trainers']

    def approve_trainers(self, request, queryset):
        queryset.update(is_approved=True)
    approve_trainers.short_description = "Approve selected trainers"