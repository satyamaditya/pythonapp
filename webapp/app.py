#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask,render_template,request
app=Flask(__name__)

@app.route('/')
def abcd():
    return render_template('add.html')

@app.route('/detail',methods=['GET','POST'])
def xyz():
    if request.method=='POST' :
        x=int(request.form['a'])
        y=int(request.form['b'])
        print(x,'\t',y)
        s=x+y
        return render_template('add.html',answer=s)

if __name__=='__main__':
    app.run()


# In[ ]:




