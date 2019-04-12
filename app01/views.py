from django.shortcuts import render

# Create your views here.
from  app01 import models
'''
page_num为当前页码
displayNum为分页器显示页数
per_page为每页显示几条
book为所有获取的object对象  
'''
class Paginator(object):
    def __init__(self,page_num,displayNum,per_page,obj):
        self.page_num=page_num
        self.displayNum=displayNum
        self.per_page=per_page
        self.obj=obj
    def pager(self):
        data_start = 10 * (self.page_num - 1)
        data_end = self.page_num * 10
        # 总数
        total_count = self.obj.count()
        # 总共需要多少页码
        total_page, m = divmod(total_count, self.per_page)
        if m:
            total_page += 1
        all_book = self.obj[data_start:data_end]
        temp = '<li><a href="?page={}" aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'
        if self.page_num - 1 <= 0:
            pre = temp.format(1)
        else:
            pre = temp.format(self.page_num - 1)
        homePage = '<li><a href="?page=1" aria-label="Previous"><span aria-hidden="true">首页</span></a></li>'
        html_str_list = [homePage, pre]
        if self.page_num <= self.displayNum // 2:
            start, end = 1, 1 + self.displayNum
        elif self.page_num >= total_page - self.displayNum // 2:
            start, end = total_page - self.displayNum + 1, total_page + 1
        else:
            start, end = self.page_num - self.displayNum // 2, self.page_num + self.displayNum // 2 + 1

        for i in range(start, end):
            tmp = '<li><a href="/books/?page={0}">{0}</a></li>'.format(i)
            html_str_list.append(tmp)
        if self.page_num + 1 >= total_page:
            late = '<li><a href="?page={0}" aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'.format(
                total_page)
        else:
            late = '<li><a href="?page={0}" aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'.format(
                self.page_num + 1)
        endPage = '<li><a href="?page={}" aria-label="Previous"><span aria-hidden="true">尾页</span></a></li>'.format(
            total_page)
        html_str_list.append(late)
        html_str_list.append(endPage)
        page_html = "".join(html_str_list)
        return all_book, page_html

def books(request):
    if request.GET:
        page_num=request.GET.get("page")
    else:
        page_num=1
    page_num=int(page_num)
    book = models.Book.objects.all()
    paginator=Paginator(page_num,5,10,book)
    all_book,page_html=paginator.pager()
    return render(request,"books.html",{"books":all_book,"page_html":page_html})