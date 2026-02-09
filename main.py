from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
# 引入你的大脑（确保 alpha_engine.py 也在同级目录）
import alpha_engine 
# 模拟数据获取（为了简化手机端，这里做个模拟接口，以免手机网络报错闪退）
import random

class GoldDashboard(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        # 界面布局：大字报显示信号
        self.signal_label = Label(text="📡 正在连线华尔街...", font_size='30sp', markup=True)
        self.score_label = Label(text="等待数据...", font_size='20sp')
        
        self.add_widget(self.signal_label)
        self.add_widget(self.score_label)
        
        # 每 10 秒刷新一次
        Clock.schedule_interval(self.update_data, 10)

    def update_data(self, dt):
        try:
            # 模拟获取一些数据喂给你的大脑 (在真实环境需替换为 requests)
            # 这里是为了保证你打包出的 APP 肯定能运行不闪退
            fake_market_data = {'tips': 1.8, 'us10y': 3.9, 'dxy': 97.5, 'gold': 2030 + random.randint(-5, 5)}
            fake_history = [] 
            fake_corr = -0.85
            
            # 调用你的核心算法
            signal, reasons, score, details = alpha_engine.generate_signal_v2(fake_market_data, fake_history, fake_corr)
            
            # 更新屏幕文字
            color = "00FF00" if score > 0 else "FF0000"
            self.signal_label.text = f"[color={color}]{signal}[/color]"
            self.score_label.text = f"总分: {score}\n现价: {fake_market_data['gold']}"
        except Exception as e:
            self.signal_label.text = "⚠️ 运行异常"
            self.score_label.text = str(e)

class GoldApp(App):
    def build(self):
        return GoldDashboard()

if __name__ == '__main__':
    GoldApp().run()