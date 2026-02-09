from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
import alpha_engine  # 这个文件你在仓库里有
import random

class GoldUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # 手机屏幕显示的仪表盘
        self.display = Label(
            text="💎 黄金量化指挥部\n正在监控全球数据...", 
            font_size='22sp', 
            halign='center',
            markup=True
        )
        self.add_widget(self.display)
        Clock.schedule_interval(self.refresh, 15) # 每15秒刷新

    def refresh(self, dt):
        # 模拟实时情报，解决你缺失 data_fetcher 的问题
        m_data = {
            "tips": round(random.uniform(1.5, 2.2), 2),
            "us10y": round(random.uniform(3.8, 4.5), 2),
            "dxy": round(random.uniform(99.0, 104.0), 2),
            "gold": 2050.0 + random.randint(-50, 50)
        }
        try:
            # 调用你仓库里的 alpha_engine.py 逻辑
            res, reasons, score, details = alpha_engine.generate_signal_v2(m_data, [])
            color = "00FF00" if score > 0 else "FF0000"
            self.display.text = f"[color={color}]【决策信号】[/color]\n{res}\n\n[size=40]得分: {score}[/size]\n核心依据: {reasons[0] if reasons else '平稳'}"
        except Exception as e:
            self.display.text = f"引擎报错: {str(e)}"

class GoldApp(App):
    def build(self):
        return GoldUI()

if __name__ == '__main__':
    GoldApp().run()
