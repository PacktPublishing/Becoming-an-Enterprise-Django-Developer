''' Admin Module For Chapter 6 '''
from django.contrib import admin
from django.contrib.admin import ModelAdmin, StackedInline, TabularInline
from django.contrib.auth.admin import UserAdmin

from .forms import (
    AddEngineForm,
    EngineForm,
    EngineSuperUserForm,
    #AddSellerForm,
    #SellerForm,
    #SellerSuperUserForm
)
from ..chapter_3.models import Engine, Seller, Vehicle, VehicleModel


#class EngineInline(TabularInline):
class EngineInline(StackedInline):
    '''
    Stacked/Tabular In-line Engine Admin Form
    '''
    model = Engine
    extra = 1

class VehicleModelInline(TabularInline):
#class VehicleModelInline(StackedInline):
    '''
    Stacked/Tabular In-line Vehicle Model Admin Form
    '''
    model = VehicleModel
    extra = 1

class SellerInline(TabularInline):
#class SellerInline(StackedInline):
    '''
    Stacked/Tabular In-line Seller Admin Form
    '''
    model = Seller
    extra = 1

class VehicleInline(TabularInline):
#class VehicleInline(StackedInline):
    '''
    Stacked/Tabular In-line Vehicle Admin Form
    '''
    model = Vehicle
    extra = 1

class VehiclesInline(TabularInline):
#class VehiclesInline(StackedInline):
    '''
    Stacked/Tabular In-line Seller Vehicle Admin Form
    '''
    model = Seller.vehicles.through
    extra = 1


@admin.register(Engine)
class EngineAdmin(ModelAdmin):
    '''
    Engine Admin Form
    '''
    #pass

    #form = EngineForm
    inlines = [VehicleInline,]

    def get_form(self, request, obj=None, **kwargs):
        if obj:
            print(request.user)

            if request.user.is_superuser:
                return EngineSuperUserForm
            else:
                return EngineForm
        else:
            return AddEngineForm

        return super(EngineAdmin, self).get_form(request, obj, **kwargs)

    def delete_model(self, request, obj):
        print(obj.__dict__)

        print('Before Delete')
        # Code actions before delete here

        super().delete_model(request, obj)

        print('After Delete')
        # Code actions after delete here

    def save_model(self, request, obj, form, change):
        print(obj.__dict__)

        print('Before Save')
        # Code actions before save here

        super().save_model(request, obj, form, change)

        print('After Save')
        # Code actions after save here

@admin.register(Seller)
#class SellerAdmin(ModelAdmin):
class SellerAdmin(UserAdmin):
    '''
    Seller Admin Form
    '''
    #pass

    # Do Not Use, For Display Only
    #fields = ('username', 'password', 'first_name', 'last_name',)
    # END - Do Not Use

    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',
                'password',
            ),
        }),
        (('Personal Info'), {'fields': (
            'first_name',
            'last_name',
            'name',
            'email',
        )}),
        (('Permissions'), {'fields': (
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions',
        )}),
        (('Important Dates'), {'fields': (
             'last_login',
             'date_joined',
        )}),
        #(('Vehicles'), {
        #    'description': ('Vehicles that this user is selling.'),
        #    'fields': (
        #        'vehicles',
        #    ),
        #}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',
                'password1',
                'password2',
            ),
        }),
        (('Personal Info'), {'fields': (
            'first_name',
            'last_name',
            'name',
            'email',
        )}),
    )
    #exclude = ('first_name',)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'name',
        'is_staff',
        'is_superuser',
    )
    list_display_links = (
        'username',
        'name',
    )
    list_editable = (
        'first_name',
        'last_name',
    )
    list_filter = (
        'is_staff',
        'is_superuser',
        'is_active',
        'name',
        'groups'
    )
    ordering = ('username',)
    search_fields = (
        'username',
        'first_name',
        'last_name',
        'name',
        'email'
    )
    prepopulated_fields = {
        'username': ('first_name', 'last_name',)
    }
    #preserve_filters = False
    save_on_top = True

    actions_on_top = True
    actions_on_bottom = True
    actions_selection_counter = True

    #filter_horizontal = ('vehicles',)
    #filter_vertical = ('vehicles',)

    list_per_page = 20

    inlines = [VehiclesInline,]

    #formfield_overrides = {
    #    models.TextField: {'widget': RichTextEditorWidget},
    #}

    #def get_form(self, request, obj=None, **kwargs):
    #    if obj:
    #        print(request.user)

    #        if request.user.is_superuser:
    #            return SellerSuperUserForm
    #        else:
    #            return SellerForm
    #    else:
    #        return AddSellerForm

    #    return super(SellerAdmin, self).get_form(request, obj, **kwargs)


@admin.register(Vehicle)
class VehicleAdmin(ModelAdmin):
    '''
    Vehicle Admin Form
    '''
    #pass
    #radio_fields = {'engine': admin.VERTICAL}
    radio_fields = {'engine': admin.HORIZONTAL}

@admin.register(VehicleModel)
class VehicleModelAdmin(ModelAdmin):
    '''
    Vehicle Model Admin Form
    '''
    #pass
    inlines = [VehicleInline,]


# Alternative to using the @admin.register(ModelName) Decorator
#admin.site.register(Engine, EngineAdmin)
#admin.site.register(Seller, SellerAdmin)
#admin.site.register(Vehicle, VehicleAdmin)
#admin.site.register(VehicleModel, VehicleModelAdmin)
