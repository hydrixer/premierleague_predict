import pandas as pd
from io import StringIO
import requests

# 获取数据
url = "https://fbref.com/en/squads/8602292d/2024-2025/matchlogs/all_comps/shooting/Aston-Villa-Match-Logs-All-Competitions"
data = requests.get(url)
print(data.text)
# 读取和处理数据
try:
    shooting = pd.read_html(StringIO(data.text), match="Shooting")[0]
    shooting.columns = shooting.columns.droplevel()  # 如果存在多层列头，删除顶层
except ValueError as e:
    print("Error loading data:", e)
    shooting = pd.DataFrame()  # 如果加载失败，创建空表

if not shooting.empty:
    # 1. 清理无关列
    shooting = shooting.dropna(how='all', axis=1)  # 移除全为空的列
    shooting = shooting.dropna(how='all', axis=0)  # 移除全为空的行

    # 2. 重命名列（示例）
    column_mapping = {
        "Date": "Match Date",
        "Sh": "Shots",
        "SoT": "Shots on Target",
        "Dist": "Avg Shot Distance",
        "FK": "Free Kicks",
        "PK": "Penalties",
        "PKatt": "Penalty Attempts",
    }
    shooting.rename(columns=column_mapping, inplace=True)

    # 3. 筛选重要数据
    important_columns = [
        "Match Date", "Shots", "Shots on Target", "Avg Shot Distance", "Free Kicks", "Penalties", "Penalty Attempts"
    ]
    shooting = shooting[important_columns]

    # 4. 转换数据类型
    shooting["Shots"] = pd.to_numeric(shooting["Shots"], errors="coerce")
    shooting["Shots on Target"] = pd.to_numeric(shooting["Shots on Target"], errors="coerce")
    shooting["Avg Shot Distance"] = pd.to_numeric(shooting["Avg Shot Distance"], errors="coerce")

    # 5. 添加派生统计：射门转化率（射正率）
    shooting["Shot Accuracy (%)"] = (shooting["Shots on Target"] / shooting["Shots"]) * 100
    shooting["Shot Accuracy (%)"] = shooting["Shot Accuracy (%)"].fillna(0).round(2)  # 替换 NaN 为 0，保留两位小数

    # 6. 展示结果
    print("Processed Shooting Data:")
    print(shooting)
else:
    print("No data available for processing.")
