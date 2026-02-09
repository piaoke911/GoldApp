from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
import pandas as pd
import random

# --- 核心逻辑：直接把 alpha_engine 的逻辑集成进来 ---
def get_signal(tips, dxy):
    score = 0
    if tips <= 1.50: score += 40
    elif tips <= 1.90: score += 20
    if dxy < 101.2: score += 20
    
    if score >= 50: return "💎 强力买入", score
    elif score >= 0: return "⚪ 观望中", score
    else: return "⚠️ 避险", score

# --- 界面展示 ---
class GoldUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.display = Label(text="📊 黄金量化指挥部\n正在初始化数据...", font_size='22sp', halign='center')
        self.add_widget(self.display)
        Clock.schedule_interval(self.refresh, 5) # 每5秒刷新

    def refresh(self, dt):
        # 模拟实时数据输入
        tips = round(random.uniform(1.4, 2.2), 2)
        dxy = round(random.uniform(99.0, 104.0), 2)
        sig, score = get_signal(tips, dxy)
        
        self.display.text = f"【最新决策】\n{sig}\n\n当前总分: {score}\n实际利率: {tips}%\n美元指数: {dxy}"

class GoldApp(App):
    def build(self):
        return GoldUI()

if __name__ == '__main__':
    GoldApp().run()
