from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
import alpha_engine # 引入你的算法零件
import random

class GoldUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # 手机屏幕中间显示一个大仪表盘
        self.display = Label(text="📊 黄金量化指挥部\n正在连接全球数据...", font_size='20sp', halign='center')
        self.add_widget(self.display)
        Clock.schedule_interval(self.refresh, 10) # 每10秒刷新一次

    def refresh(self, dt):
        # 喂给算法一些模拟数据，确保离线也能跑
        test_data = {"tips": 1.85, "us10y": 4.1, "dxy": 101.5, "gold": 2050.0}
        try:
            # 调用你 alpha_engine.py 里的决策逻辑
            res, reasons, score, details = alpha_engine.generate_signal_v2(test_data, [])
            self.display.text = f"【最新决策信号】\n{res}\n\n当前评分: {score}\n主要逻辑: {reasons[0] if reasons else '平稳'}"
        except Exception as e:
            self.display.text = f"❌ 逻辑引擎故障: {str(e)}"

class GoldApp(App):
    def build(self):
        return GoldUI()

if __name__ == '__main__':
    GoldApp().run()
