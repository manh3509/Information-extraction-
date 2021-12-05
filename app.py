from flask import Flask,url_for,render_template,request,flash,redirect
from fun import rule2_adj, rule2_adv, rule2_n,rule2_v,rule2_num,rule2_adp,rule2_loc,rule2_org,rule2_percent,rule2_product
from fun import rule2,rule3,rule2_geo,rule2_per,rule2_gpe,rule2_tim,rule2_art,rule2_eve,rule2_nat,rule2_date,rule2_lan,rule2_money,rule2_car
import spacy
from spacy import displacy

nlp = spacy.load('en_core_web_sm')
import json


HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem">{}</div>"""

from flaskext.markdown import Markdown

app = Flask(__name__)
Markdown(app)


# def analyze_text(text):
# 	return nlp(text)

@app.route('/')
def index_get():
	return render_template('index.html')

@app.route('/index', methods=['GET','POST'])
def index():
    #lấy hàm ra từ
	if request.method == 'POST':
		text = request.form['mycountry']
		pred = rule2(text)
		pred2 = rule3(text)
		pred2_n = rule2_n(text)
		pred2_v = rule2_v(text)
		pred2_adj = rule2_adj(text)
		pred2_adv = rule2_adv(text)
		pred2_num= rule2_num(text)
		pred2_adp = rule2_adp(text)
		pred2_adp = rule2_percent(text)
	return render_template('index.html',pred=pred, text = text,pred2=pred2,pred2_n=pred2_n,pred2_v=pred2_v,pred2_adj=pred2_adj,pred2_adv=pred2_adv,pred2_num=pred2_num,pred2_adp=pred2_adp)

#########################################################################################################################################
@app.route('/extract',methods=["GET","POST"])
def extract():
	if request.method == 'POST':
		raw_text = request.form['rawtext']
		docx = nlp(raw_text)
		html = displacy.render(docx,style="ent")
		html = html.replace("\n\n","\n")
		result = HTML_WRAPPER.format(html)
		pred2_loc = rule2_loc(raw_text)
		pred2_org = rule2_org(raw_text)
		pred2_geo = rule2_geo(raw_text)
		pred2_per = rule2_per(raw_text)
		pred2_gpe = rule2_gpe(raw_text)
		pred2_tim = rule2_tim(raw_text)
		pred2_art = rule2_art(raw_text)
		pred2_eve = rule2_eve(raw_text)
		pred2_nat = rule2_nat(raw_text)
		pred2_date = rule2_date(raw_text)
		pred2_lan = rule2_lan(raw_text)
		pred2_money = rule2_money(raw_text)
		pred2_car = rule2_car(raw_text)
		pred2_percent = rule2_percent(raw_text)
		pred2_product = rule2_product(raw_text)
	return render_template('result.html',rawtext=raw_text,result=result,pred2_loc=pred2_loc,pred2_org=pred2_org,pred2_geo=pred2_geo,pred2_per=pred2_per,pred2_gpe=pred2_gpe,pred2_tim=pred2_tim,pred2_art=pred2_art,pred2_eve=pred2_eve,pred2_nat=pred2_nat,pred2_date=pred2_date,pred2_lan=pred2_lan,pred2_money=pred2_money,pred2_car=pred2_car,pred2_percent=pred2_percent,pred2_product=pred2_product)


@app.route('/previewer')
def previewer():
	return render_template('previewer.html')

@app.route('/preview',methods=["GET","POST"])
def preview():
	if request.method == 'POST':
		newtext = request.form['newtext']
		result = newtext
	return render_template('preview.html',newtext=newtext,result=result)


if __name__ == '__main__':
	app.run(debug=True)