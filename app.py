#!/usr/bin/env python
# coding: utf-8

# In[6]:


from textblob import TextBlob
from flask import Flask
from flask import render_template,request
app = Flask(__name__)

@app.route("/",methods=["GET", "POST"])
def index():
    return(render_template("index.html"))

@app.route("/result", methods=["GET", "POST"])
def result():
    text = request.form.get("text")
    result = TextBlob(text).sentiment
    return(render_template("result.html", result=result))
if __name__=="__main__":
    app.run()



# In[5]:


pip install Flask


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




