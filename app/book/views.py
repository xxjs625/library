from flask import render_template, redirect, request, url_for, flash
from . import book
from .. import db
from ..models import Book
from .forms import addbookForm,dropbookForm,editbookForm
from ..decorators import admin_required ,permission_required
from flask_login import login_required
@book.route('/addbook', methods=['GET', 'POST'])
@login_required
@admin_required

def addbook():
    form = addbookForm()
    if form.validate_on_submit():
        bk = Book(bookname=form.bookname.data,
                    author=form.author.data,
                    site=form.site.data)
        db.session.add(bk)
        db.session.commit()
        flash('添加成功')
    return render_template('book/addbook.html', form=form)
def for_admins_only():
    return "需要管理员权限"


@book.route('/dropbook',methods=['GET', 'POST'])
def dropbook():
    form = dropbookForm()
    if form.validate_on_submit():
        bk2 = Book.query.filter(Book.bookname == form.bookname.data).first()
        db.session.delete(bk2)
        db.session.commit()
        flash('删除成功')
    return render_template('book/dropbook.html', form=form)
@book.route('/editbook',methods=['GET', 'POST'])
def editbook():
    form = editbookForm()
    if form.validate_on_submit():
        bk3 = Book.query.filter(Book.bookname == form.oldbookname.data).first()
        bk3.bookname = form.newbookname.data
        bk3.author = form.author.data
        bk3.site = form.site.data
        db.session.add(bk3)
        db.session.commit()
        flash('修改成功')
    return render_template('book/editbook.html', form=form)
@book.route('/allbook')
def allbook():
    allbook = db.session.execute('select bookname,author,site from books')
    return render_template('book/allbook.html',allbook=allbook)