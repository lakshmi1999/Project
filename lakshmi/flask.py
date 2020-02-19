
# A very simple Flask Hello World app for you to get started with...

from flask import Flask,render_template,request
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



app = Flask(__name__)
app.config["DEBUG"] = True
@app.route("/",methods=["GET", "POST"])
def index():
    var=""
    name=""
    if request.method=="GET":
        return render_template("website.html")
    else:
        var=request.form["product"]
        name=request.form["uname"]
        if request.form["trust"]=="Feedback":
            good=[]
            value=[]
            df=pd.read_csv('/home/lakshmivineka/mysite/trustvalue.csv')
            for i in range(1,6):
	            if var==df.columns[i]:
		            val=df[var].max()
		            ind=df[var].idxmax()
		            a=df.iloc[ind,0]
		            for j in range(0,3):
		                good.append(df.iloc[j,0])
		                value.append(df.iloc[j,i])
		            y_pos=np.arange(len(good))
		            plt.bar(y_pos,value,align='center',color='g',width=0.3)
		            plt.xticks(y_pos,good,color="green")
		            plt.xlabel('PROVIDERS',color="red")
		            plt.ylabel('TRUST VALUE(Feedback)',color="red")
		            plt.title(var,color="red")
		            fname="/home/lakshmivineka/mysite/static/img/feedback.png"
		            plt.savefig(fname=fname,dpi=100)
		            return render_template("feedbackresult.html",name=name,var=var,a=a,val=val)
        elif request.form["trust"]=="Cost":
            df=pd.read_csv('/home/lakshmivineka/mysite/costvalue.csv')
            for i in range(1,6):
                if var==df.columns[i]:
                    val=df[var].max()
                    ind=df[var].idxmax()
                    a=df.iloc[ind,0]
                    provider=[]
                    value=[]
                    for j in range(0,3):
                        provider.append(df.iloc[j,0])
                        value.append(df.iloc[j,i])
                    y_pos=np.arange(len(provider))
                    plt.bar(y_pos,value,align='center',color='g',width=0.3)
                    plt.xticks(y_pos,provider,color="green")
                    plt.xlabel('PROVIDERS',color="red")
                    plt.ylabel('COST(in "₹")',color="red")
                    plt.title(var,color="red")
                    fname="/home/lakshmivineka/mysite/static/img/cost.png"
                    plt.savefig(fname=fname,dpi=100)
                    return render_template("costresult.html",name=name,var=var,a=a,val=val)














