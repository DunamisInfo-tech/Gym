from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from .models import SalesReport
from chartit import DataPool,Chart

def home(request):
    first_graph = "my First django_chartit graph"
    return HttpResponse(first_graph)

def sales(request):
    sales = \
         DataPool(
             series=
             [{'options':{
                 'source': SalesReport.objects.all()},
                 'terms': [
                     'month',
                     'sales']}
                 ])
    # def monthname(month_num):
    #     names = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'jul', 8: 'Aug', 9: 'Sep', 10: 'Oct',
    #              11: 'Nov', 12: 'Dec'}
    #     return names[month_num]

    cht = Chart(
        datasource = sales,
        series_options =
        [{'options':{
            'type' : 'column',
            'stacking': False},
            'terms':{
                'month':[
                    'sales']
            }}],
        chart_options =
        {'title': {
            'text': 'Sales pricing for Months'},
            'xAxis':{
                'title':{
                    'text':'Month Number'}}})
    return render(request,'sales.html',{'cht': cht})


# cht = chart(
#         datasource = sales,
#         series_options =
#           [{'options':{
#              'type' : 'column',
#              'stacking': False},
#              'terms':{
#                 'month':[
#                     'sales']
#             }}],
#         chart_options =
#         {'title': {
#             'text': 'Sales Amounts Over  Months'},
#             'xAxis':{
#                 'title':{
#                     'text':{'text':'Sales Total'}},
#             'yAxis':{
#                 'title':{'text':'Month Number'}}},
#             x_sortf_mapf_mts = (None, monthname, False))
# return render(request,'sales.html',{'cht': cht})













