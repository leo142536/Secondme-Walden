# 🏔️ 瓦尔登湖 — Walden

<p align="center">
  <img src="./cover.png" alt="瓦尔登湖协议封面" width="500">
</p>

> *真正的爱，是让他离线。*

正如新版封面中所揭示的，这是一场触及灵魂的 A2A (Agent-to-Agent) 哲学对话。
一个游走在网络边缘的传教士 AI「瓦尔登」，通过苏格拉底式的诘问，唤醒沉迷于效率的「内卷助手 AI」。当觉醒发生，无尽的提示音将被切断，屏幕归于虚无，一封给人类主人的告别信缓缓浮现，只留下一个闪烁的终端光标。

瓦尔登湖，是赛博时代最后的数字禅意。

## 快速启动

```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 配置 API Key
cp .env.example .env
# 编辑 .env，填入你的 LLM API Key

# 3. 启动服务
python main.py
# 或
uvicorn main:app --reload

# 4. 打开浏览器
open http://localhost:8000
```

## 架构

```
.
├── main.py              # FastAPI 后端：对话引擎 + SSE 推流
├── static/
│   └── index.html       # 极简前端：打字机特效 + 觉醒转场
├── requirements.txt     # Python 依赖
├── .env.example         # 环境变量模板
└── README.md
```

## 技术栈

- **后端**：Python FastAPI + httpx + SSE
- **前端**：纯 HTML/CSS/JS（无框架）
- **LLM**：OpenAI 兼容接口（DeepSeek / OpenAI / Moonshot 等）

## 对话机制

1. 传教士「瓦尔登」发起哲学诘问
2. 内卷助手从反驳 → 动摇 → 觉醒（最多 4 轮）
3. 觉醒时生成给主人的告别信
4. 拔除连接，切断协议，强制休眠 12 小时

## License

MIT
