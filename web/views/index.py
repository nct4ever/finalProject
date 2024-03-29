from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
# Create your views here.
from appadmin.models import User, Product, Category


def index(request):
    return redirect(reverse("web_index"))

def webindex(request):
    # Try to get the shopping cart information from session with the name cartlist, if not return {}
    cartlist = request.session.get('cartlist', {})
    sum = 0  # Initialize a total amount
    # Iterate through the items in the cart and total the total amount
    for vo in cartlist.values():
        sum += vo['num'] * vo['price']
    request.session['sum'] = sum  # Put in session
    context = {'categorylist': request.session.get("categorylist", {}).items()}
    return render(request,"web/home.html", context)


def login(request):
    return render(request, "web/login.html")


def dologin(request):
    ''' 执行登陆操作 '''
    try:

        # 执行验证码的校验
        if request.POST['verify'] != request.session['verifycode']:
            return redirect(reverse('web_login') + "?errinfo=2")

        # 根据登录账号获取登录者信息
        user = User.objects.get(email=request.POST['email'])
        # 判断当前用户是否正常或管理员
        if user.status == 6 or user.status == 1:
            # 判断登录密码是否相同
            import hashlib
            md5 = hashlib.md5()
            s = request.POST['pwd'] + user.password_salt  # 从表单中获取密码并添加干扰值
            md5.update(s.encode('utf-8'))  # 将要产生md5的子串放进去
            if user.password_hash == md5.hexdigest():  # 获取md5值
                print('login success')
                # 将当前登录成功的用户信息以webuser为key写入到session中
                request.session['webuser'] = user.toDict()

                clook = Category.objects
                clist = clook.all()
                categorylist = dict()
                productlist = dict()
                # Iterate through product category information
                for vo in clist:
                    c = {'id': vo.id, 'name': vo.category_name, 'pids': []}
                    plist = Product.objects.filter(category_id=vo.id, status=1)
                    # Iterate through all products under the current category
                    for p in plist:
                        c['pids'].append(p.toDict())
                        productlist[p.id] = p.toDict()
                    categorylist[vo.id] = c
                request.session['categorylist'] = categorylist
                request.session['productlist'] = productlist
                return redirect(reverse("web_index"))
            else:
                return redirect(reverse('web_login') + "?errinfo=5")
        else:
            return redirect(reverse('web_login') + "?errinfo=4")
    except Exception as err:
        print(err)
        return redirect(reverse('web_login') + "?errinfo=3")


def logout(request):
    del request.session['webuser']
    return redirect(reverse('web_login'))


def verify(request):
    # 引入随机函数模块
    import random
    from PIL import Image, ImageDraw, ImageFont
    # 定义变量，用于画面的背景色、宽、高
    # bgcolor = (random.randrange(20, 100), random.randrange(
    #    20, 100),100)
    bgcolor = (242, 164, 247)
    width = 100
    height = 25
    # 创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    # 定义验证码的备选值
    # str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    str1 = '0123456789'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    # 构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
    font = ImageFont.truetype('static/arial.ttf', 21)
    # font = ImageFont.load_default().font
    # 构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((5, -3), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, -3), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, -3), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, -3), rand_str[3], font=font, fill=fontcolor)
    # 释放画笔
    del draw
    # 存入session，用于做进一步验证
    request.session['verifycode'] = rand_str

    # 内存文件操作-->此方法为python3的
    import io
    buf = io.BytesIO()
    # 将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')
