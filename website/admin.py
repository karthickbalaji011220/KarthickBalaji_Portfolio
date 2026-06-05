from django.contrib import admin
from .models import Profile, Skill, Education, Experience, Certification, Achievement, Project


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'email', 'phone']
    fieldsets = (
        ('Personal Info', {'fields': ('name', 'role', 'short_intro', 'bio', 'career_objective')}),
        ('Images & Files', {'fields': ('profile_image', 'about_image', 'resume_file')}),
        ('Contact', {'fields': ('email', 'phone', 'location', 'linkedin', 'github', 'portfolio_url')}),
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['skill_name', 'percentage', 'order']
    list_editable = ['percentage', 'order']


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'institution', 'year', 'order']
    list_editable = ['order']


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['role', 'company', 'duration', 'order']
    list_editable = ['order']


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ['title', 'issuer', 'year', 'order']
    list_editable = ['order']


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']
    list_editable = ['order']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'order', 'created_at']
    list_editable = ['order']
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        ('Basic Info', {'fields': ('title', 'slug', 'short_description', 'full_description', 'order')}),
        ('Technical', {'fields': ('tech_stack', 'features')}),
        ('Media', {'fields': ('project_image',)}),
        ('Links', {'fields': ('github_link', 'live_demo_link')}),
    )
