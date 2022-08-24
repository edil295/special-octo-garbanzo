from django.contrib import admin
from .models import *
import psycopg2


@admin.display(description='Общая стоимость')
def count_of_apartment(obj):
    return obj.client_block.price_square_meter * obj.area


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_of_sale'
    empty_value_display = 'Без хозяина'
    list_display = ('name', 'date_of_sale', 'status', 'area', count_of_apartment)
    list_editable = ('date_of_sale', )
    list_filter = ('status', 'client_block')
    search_fields = ('name',)


@admin.display(description='Итоговая стоимость квартир')
def cool(obj):
    conn = psycopg2.connect(host='localhost', user='postgres', password='admin', dbname='building')
    cursor = conn.cursor()
    cursor.execute("""select id, (select sum(area) from complex_client 
    where client_block_id = complex_block.id) * (price_square_meter) as apart from complex_block""")
    num = 0
    results = cursor.fetchall()
    for res in results:
        if res[0] == obj.id:
            num = res[1]
    return num


@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    list_display = ('number_block', 'count_entrance', 'count_floors', 'apartment_count', 'count_all_apartment', cool)

    @admin.display(description='Общее кол-во квартир')
    def count_all_apartment(self, obj):
        return obj.count_entrance * obj.count_floors * obj.apartment_count


