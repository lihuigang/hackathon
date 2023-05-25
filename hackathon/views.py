from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from pyecharts.charts import Bar
from pyecharts import options as opts

import csv


def hello(request):
    return HttpResponse("Hello world ! ")


# 表单
def upload(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']
        fs = FileSystemStorage(location='csv/')
        filename = fs.save(csv_file.name, csv_file)
        # return render(request, 'upload.html', {'filename': filename})
        return echarts_view(request)
    return render(request, 'upload.html')


# 接收请求数据
def search(request):
    request.encoding = 'utf-8'
    if 'q' in request.GET and request.GET['q']:
        message = '你搜索的内容为: ' + request.GET['q']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)

def echarts_view(request):
    # 生成柱状图数据
    x_data = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    y_data = [820, 932, 901, 934, 1290, 1330, 1320]

    # 生成柱状图
    bar = (
        Bar()
        .add_xaxis(x_data)
        .add_yaxis("Sales", y_data)
        .set_global_opts(title_opts=opts.TitleOpts(title="Sales"))
    )

    # 将图表数据转换为 JSON 格式
    chart_data = bar.dump_options_with_quotes()

    # 将图表数据传递给模板
    return render(request, 'upload.html', {'chart_data': chart_data})