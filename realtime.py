# message = """<html>
# <head></head>
# <body>
# <p>Signal Graph</p>
# </body>
# </html>"""
# filepath = "hello.html"
# with open(filepath, 'w') as f:
#     f.write(message)
#     f.close()
# webbrowser.open_new_tab(filepath)

# url 데이터를 table로 만들기
# import pandas as pd
# tables = pd.read_html('https://www.koreabaseball.com/Record/Player/HitterBasic/Basic1.aspx')
# print(tables[0])
#import webbrowser

# 무작위의 수를 생성
import random
# 순차적인 수를 생성
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
# animation 효과, 실시간 데이터 반영
from matplotlib.animation import FuncAnimation
# 셀형식 
#plt.style.use('fivethirtyeight')

x_val = []
heart_rate_val = []
breathing_rate_val = []
body_temperature_val = []
 
# 순차적인 수를 생성 
index = count()
 
def animate(i):
    x_val.append(next(index))
    # 0~10 사이의 랜덤한 정수 생성
    heart_rate_val.append(random.randint(60,100))
    breathing_rate_val.append(random.randint(12,20))
    body_temperature_val.append(random.randint(36,37))
    # 앞선 그래프를 삭제
    plt.cla()
    # 그래프 그리기
    plt.title("< signal >")
    plt.xlabel('second') 
    plt.ylabel('measures')
    plt.plot(x_val, heart_rate_val, label='heart rate')
    plt.plot(x_val, breathing_rate_val, label='breathing rate')
    plt.plot(x_val, body_temperature_val, label='body temperature')
    plt.legend(bbox_to_anchor=(0,1), loc="upper left", borderaxespad=0.)
    #shadow=True, fancybox=True, loc="upper left"
    #plt.hist : 히스토그램으로 그리기
    #plt.bar : 블록으로 그리기   

ani = FuncAnimation(plt.gcf(), animate, interval = 1000)
# plt.gcf(): 현재 그래프 모양을 가져옴
# animate: 애니메이션 효과 적용
# interval = 1000: 1000 밀리초마다 적용
plt.tight_layout()
plt.show()
ani.save('signal_down.gif', writer='imagemagick')