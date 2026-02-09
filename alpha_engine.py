import pandas as pd
import numpy as np

# ==============================================================================
# 🧠 全球顶级量化决策大脑 - 首席架构师定稿版 V3.5 (相关性溢价版)
# ==============================================================================

def calculate_rsi_manual(series, period=14):
    """手动计算RSI，确保不依赖第三方库"""
    delta = series.diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.ewm(alpha=1/period, min_periods=period, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1/period, min_periods=period, adjust=False).mean()
    rs = avg_gain / avg_loss
    return (100 - (100 / (1 + rs))).fillna(50)

def calculate_macd_manual(series):
    """手动计算MACD指标"""
    exp1 = series.ewm(span=12, adjust=False).mean()
    exp2 = series.ewm(span=26, adjust=False).mean()
    macd_line = exp1 - exp2
    signal_line = macd_line.ewm(span=9, adjust=False).mean()
    return macd_line, signal_line

def generate_signal_v2(market_data, df_history, correlation):
    """
    基于华尔街实战参数的动态加权评分系统 - 首席架构师重构
    """
    score_details = {} # 记录详细得分
    reasons = []
    
    # 获取实时核心参数
    tips = market_data.get("tips", 2.0)
    us10y = market_data.get("us10y", 4.0)
    dxy = market_data.get("dxy", 100.0)

    # --- 维度 1: 实际利率 (权重 40) ---
    s_tips = 0
    if tips <= 1.50: s_tips = 40
    elif tips <= 1.90: s_tips = 30
    elif tips > 2.10: s_tips = -20
    score_details['实际利率(TIPS)'] = s_tips

    # --- 维度 2: 名义利率 (权重 10) ---
    s_us10y = 0
    if us10y < 3.85: s_us10y = 10
    elif us10y > 4.50: s_us10y = -10
    score_details['名义利率(US10Y)'] = s_us10y

    # --- 维度 3: 美元指数 (权重 20) ---
    s_dxy = 0
    if dxy < 98.5: s_dxy = 20
    elif dxy < 101.2: s_dxy = 10
    elif dxy > 103.5: s_dxy = -20
    score_details['美元指数(DXY)'] = s_dxy

    # --- 维度 4: 技术共振 (权重 30) ---
    s_tech = 0
    if not df_history.empty:
        closes = df_history
        rsi = calculate_rsi_manual(closes).iloc[-1]
        if rsi < 32: s_tech += 15
        elif rsi > 68: s_tech -= 15
        
        macd, sig = calculate_macd_manual(closes)
        if macd.iloc[-1] > sig.iloc[-1] and macd.iloc[-2] <= sig.iloc[-2]:
            s_tech += 15
    score_details['技术指标(RSI/MACD)'] = s_tech

    # --- 维度 5: 动态避险溢价 (全新注入) ---
    s_corr = 0
    # 当相关系数 > -0.2，说明黄金不再受美元打压，进入“避险共涨”模式
    if correlation > -0.2:
        s_corr = 25
        reasons.append(f"避险模式启动: 金美脱钩(相关系数:{correlation:.2f})")
    elif correlation < -0.85:
        s_corr = 5
        reasons.append(f"逻辑确认: 强负相关规律(相关系数:{correlation:.2f})")
    score_details['避险溢价(Corr)'] = s_corr

    # 总分汇总
    total_score = sum(score_details.values())
    
    # 记录逻辑支撑点
    if s_tips > 0: reasons.append(f"利率利多支撑({tips}%)")
    if s_dxy > 0: reasons.append(f"美元走弱计价利多({dxy})")

    # --- 判定结果逻辑 ---
    if total_score >= 85:
        final_signal = "【💎 顶级·全因子共振买入】"
    elif total_score >= 55:
        final_signal = "【✅ 强势买入】"
    elif total_score >= 0:
        final_signal = "【⚪ 逻辑分歧·观望中】" #
    else:
        final_signal = "【⚠️ 风险规避/清仓】" #

    return final_signal, reasons, total_score, score_details