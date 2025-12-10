import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

def analyze_stock(ticker):
    print(f"--- ANALYZING {ticker} ---")
    
    # 1. Tải dữ liệu (6 tháng gần nhất)
    stock = yf.Ticker(ticker)
    hist = stock.history(period="6mo")
    
    if hist.empty:
        print("Error: No data found.")
        return

    # 2. Tính toán chỉ báo kỹ thuật (Technical Indicators)
    # MA20: Xu hướng ngắn hạn
    hist['MA20'] = hist['Close'].rolling(window=20).mean()
    # MA50: Xu hướng trung hạn
    hist['MA50'] = hist['Close'].rolling(window=50).mean()

    # 3. Trực quan hóa (Visualization)
    plt.figure(figsize=(10, 5))
    plt.plot(hist['Close'], label='Close Price', alpha=0.5)
    plt.plot(hist['MA20'], label='MA20 (Short-term)', color='orange')
    plt.plot(hist['MA50'], label='MA50 (Mid-term)', color='green')
    
    plt.title(f'Technical Analysis: {ticker}')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    # Ví dụ phân tích cổ phiếu Apple
    analyze_stock("AAPL")
