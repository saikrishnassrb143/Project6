from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
data="""<table>
    <th>
        <th>Total months</th>
        <th>Savings</th>
    </th>
    <tr>
        <td>January</td>
        <td>$10000</td>
    </tr>
</table>"""
class HtmlView(View):
    def get(self,request):
        return HttpResponse(data,content_type="text/html")
class XmlView(View):
    def get(self,request):
        return HttpResponse(data,content_type="application/xml")
class ExcelView(View):
    def get(self,request):
        return  HttpResponse(data,content_type="application/vnd.ms-excel")

