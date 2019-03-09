from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired


class addbookForm(FlaskForm):
    bookname = StringField('书名', validators=[
        DataRequired()])
    author = StringField('作者', validators=[DataRequired()])
    site = StringField('位置', validators=[DataRequired()])
    status = StringField('状态', validators=[DataRequired()])
    submit = SubmitField('添加')
class dropbookForm(FlaskForm):
    bookname = StringField('请输入书名', validators=[
        DataRequired()])
    submit = SubmitField('确认删除？')
class editbookForm(FlaskForm):
    oldbookname = StringField('要修改的书名', validators=[
        DataRequired()])
    submit1 = SubmitField('提交')
    newbookname = StringField('新书名', validators=[
        DataRequired()])
    author = StringField('新作者', validators=[DataRequired()])
    site = StringField('新位置', validators=[DataRequired()])
    status = StringField('修改状态', validators=[DataRequired()])
    submit = SubmitField('确认修改')
class querybookForm(FlaskForm):
    bookname =  StringField('查询书籍', validators=[
        DataRequired()])
    submit = SubmitField('查询')
class borrowbookForm(FlaskForm):
    bookname =  StringField('书名', validators=[
        DataRequired()])
    borrowname = StringField('学号', validators=[
        DataRequired()])
    #borrow_time = Da('借阅时间', validators=[
        #DataRequired()])
    #back_time = StringField('应归还时间', validators=[
        #DataRequired()])

    submit = SubmitField('借阅')