from flask import render_template, redirect, request, url_for, flash,session
from .. import db
from ..models import Book, Borrowbook, User
from .forms import addbookForm, dropbookForm,editbookForm, querybookForm, borrowbookForm
from ..decorators import admin_required ,permission_required
from flask_login import login_required
from . import book
@book.route('/addbook', methods=['GET', 'POST'])
@login_required
@admin_required

def addbook():
    form = addbookForm()
    if form.validate_on_submit():
        bk = Book(bookname=form.bookname.data,
                    author=form.author.data,
                    site=form.site.data,
                    status=form.status.data)
        db.session.add(bk)
        db.session.commit()
        flash('添加成功')
    return render_template('book/addbook.html', form=form)
def for_admins_only():
    return "需要管理员权限"
@book.route('/borrowbook',methods=['GET', 'POST'])
@login_required
@admin_required
def borrowbook():
    form = borrowbookForm()
    if form.validate_on_submit():
        borrow = Borrowbook(bookname1 = form.bookname.data,
                            borrowname = form.borrowname.data
                )
        db.session.add(borrow)
        db.session.commit()
        flash('借阅成功')

    return render_template('book/borrow.html',form=form)
def for_adminsss():
    return "需要管理员权限"

@book.route('/dropbook',methods=['GET', 'POST'])
@login_required
@admin_required
def dropbook():
    form = dropbookForm()
    if form.validate_on_submit():
        bk2 = Book.query.filter(Book.bookname == form.bookname.data).first()
        db.session.delete(bk2)
        db.session.commit()
        flash('删除成功')
    return render_template('book/dropbook.html', form=form)
def for_admins():
    return "需要管理员权限"
@book.route('/editbook',methods=['GET', 'POST'])
@login_required
@admin_required
def editbook():
    form = editbookForm()
    if form.validate_on_submit():
        bk3 = Book.query.filter(Book.bookname == form.oldbookname.data).first()
        bk3.bookname = form.newbookname.data
        bk3.author = form.author.data
        bk3.site = form.site.data
        bk3.status = form.status.data
        db.session.add(bk3)
        db.session.commit()
        flash('修改成功')
        form.newbookname.data=bk3.bookname
        form.author.data=bk3.author
        form.site.data=bk3.site
        form.status.data=bk3.status
    return render_template('book/editbook.html', form=form)
def for_admin():
    return "需要管理员权限"
@book.route('/allbook')
def allbook():
    allbook = db.session.execute('select bookname,author,site,status from books')
    page = request.args.get('page', 1, type=int)
    pagination = Book.query.order_by(Book.bookname.desc()).paginate(
        page, error_out=False)
    books = pagination.items

    return render_template('book/allbook.html',allbook=allbook,pagination=pagination,books=books)
@book.route('/borrowquery')
def borrowquery():
    borrowdbook = db.session.execute('select bookname,author,site,borrowname,borrow_time,back_time from books,borrowbooks where books.bookname=borrowbooks.bookname1')
    page = request.args.get('page', 1, type=int)
    pagination = Borrowbook.query.order_by(Borrowbook.back_time.desc()).paginate(
        page, error_out=False)
    books = pagination.items
    return render_template('book/borrowquery.html',pagination=pagination,books=books,borrowdbook=borrowdbook)
@book.route('/querybook',methods=['GET', 'POST'])
def querybook():
    bookname1 = None
    querybook = None
    count = 0
    form = querybookForm()
    if form.validate_on_submit():
        bookname1 = form.bookname.data
        #querybookname = form.querybookname.data
        form.bookname.data = ''
        #querybook = db.session.execute('select bookname,author,site from books where bookname="bookname1"')
        querybook = Book.query.filter_by(bookname=bookname1).all() or Book.query.filter_by(author=bookname1).all()
        count = len(querybook)
        if querybook is None:
            flash('没有该书')
    page = request.args.get('page', 1, type=int)
    pagination = Book.query.order_by(Book.bookname.desc()).paginate(
        page, error_out=False)
    books = pagination.items
    return render_template('book/querybook.html', form=form,querybook=querybook, bookname1=bookname1, count=count,pagination=pagination,books=books)
