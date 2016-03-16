from django.contrib import admin
from .models import *


class IncomeInline(admin.TabularInline):
    model = Income
    extra = 1


class OutcomeInline(admin.TabularInline):
    model = Outcome
    extra = 1


class MonthAdmin(admin.ModelAdmin):

    class Media:
        css = {
             'all': ('css/admin_month_change_list.css',)
        }

    inlines = [
        IncomeInline,
        OutcomeInline,
    ]

    def get_balance(self, obj):
        return obj.get_month_balance()
    get_balance.short_description = "Balance"

    def changelist_view(self, request, extra_context=None):
        """
        Sum balances from all months and display them on the top of the admin panel
        """
        months = self.model.objects.all()
        balance = sum([month.get_month_balance() for month in months])

        my_context = {
            'balance': balance,
        }

        return super(MonthAdmin, self).changelist_view(request, extra_context=my_context)

    list_display = ('name', 'year', 'get_balance')

admin.site.register(Month, MonthAdmin)


class IncomeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Income, IncomeAdmin)


class OutcomeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Outcome, OutcomeAdmin)
