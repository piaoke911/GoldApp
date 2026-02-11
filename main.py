import yfinance as yf
import pandas as pd
from config import *
from notifier import send_email

def run_logic():
    print("🚀 正在从华尔街抓取数据...")
    # 获取黄金数据
    gold = yf.Ticker("GC=F").history(period="1d")
    price = gold['Close'].iloc[-1]
    
    # 极简量化逻辑：这里可以根据你的 alpha_engine 调整
    score = 50 
    signal = "等待"
    
    print(f"✅ 现价: {price:.2f} | 得分: {score} | 信号: {signal}")
    
    # 强制发一封测试邮件，证明链路已通
    subject = "🔔 黄金雷达点火成功报告"
    content = f"当前黄金现价: ${price:.2f}\n系统状态: 监控中\n发送时间: {pd.Timestamp.now()}"
    
    if send_email(subject, content):
        print("📧 邮件已飞向你的邮箱！")
    else:
        print("❌ 邮件发送遇到障碍")

if __name__ == "__main__":
    run_logic()
