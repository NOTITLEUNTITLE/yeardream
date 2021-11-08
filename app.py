from flask import Flask
from flask.templating import render_template
import corona_data
from datetime import date, timedelta


app = Flask(__name__)

@app.route('/')
def index():
  now = date.today()
  now_str = now.strftime("%Y%m%d")
  # print(now_str)
  yesterday = now - timedelta(days=1)
  yesterday_str = yesterday.strftime("%Y%m%d")
  t_data = corona_data.get_corona_data(now_str,now_str)
  y_data = corona_data.get_corona_data(yesterday_str,yesterday_str)
  #오늘 데이터가 없다면, 어제 데이터로 실행하라
  if not t_data:
    yesterday = now - timedelta(days=1)
    yesterday_str = yesterday.strftime("%Y%m%d")
    # print(yesterday_str)

    data = corona_data.get_corona_data(yesterday_str,yesterday_str)
    # print(data)
    return render_template('index.html',data=data, today = yesterday)
    
  
  return render_template('index.html',t_data=t_data, y_data=y_data, today=now, yes=yesterday)


if __name__ == '__main__':
  app.run(debug=True)