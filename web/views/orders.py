from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from datetime import datetime

from appadmin.models import Orders, OrderDetail, Payment, Shipping


def index(request, pIndex=1):
    umod = Orders.objects
    sid = request.session['webuser']['id']
    
    ulist = umod.filter(member_id=sid, status=1)
    smod = Shipping.objects
    slist = smod.filter(user_id=sid)

    mywhere = []
    # 获取、判断并封装状态status搜索条件
    status = request.GET.get('status', '')
    if status != '':
        ulist = ulist.filter(status=status)
        mywhere.append("status=" + status)

    ulist = ulist.order_by("id")  # 对id排序
    # 执行分页处理
    pIndex = int(pIndex)
    page = Paginator(ulist, 5)  # 以每页10条数据分页
    maxpages = page.num_pages  # 获取最大页数
    # 判断当前页是否越界
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    list2 = page.page(pIndex)  # 获取当前页数据
    plist = page.page_range  # 获取页码列表信息



    context = {"orderslist": list2, "shiplist": slist, 'plist': plist, 'pIndex': pIndex, 'maxpages': maxpages, 'mywhere': mywhere}
    return render(request, "web/checkout.html", context)


def insert(request):
    try:
        # 执行订单信息的添加
        od = Orders()
        od.member_id = request.session['webuser']['id']
        od.money = request.session['sum']
        od.status = 1  # 订单状态:1过行中/2无效/3已完成
        od.create_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        od.save()

        op = Payment()
        op.order_id = od.id  # 订单id号
        od.member_id = 0
        op.type = 2
        op.bank = request.GET.get("bank", 3)  # 收款银行渠道:1微信/2余额/3现金/4支付宝
        op.money = request.session['sum']
        op.status = 2
        op.create_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        op.save()

        # 执行订单详情的添加
        cartlist = request.session.get("cartlist", {})  # 获取购物车中的菜品信息
        # 遍历购物车中的菜品并添加到订单详情中
        for item in cartlist.values():
            ov = OrderDetail()
            ov.order_id = od.id
            ov.product_id = item['id']  # id
            ov.product_name = item['product_name']
            ov.price = item['price']  # 单价
            ov.quantity = item['num']  # 数量
            ov.status = 1  # 状态:1正常/9删除
            ov.save()

        del request.session["cartlist"]
        del request.session['sum']
        return HttpResponse("Y")
    except Exception as err:
        print(err)
        return HttpResponse("N")


def detail(request):
    ''' 加载订单详情 '''
    pass


def status(request):
    ''' 修改订单状态 '''
    pass
