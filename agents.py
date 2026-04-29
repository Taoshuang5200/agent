from crewai import Agent
from tools import web_search_tool
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

# 初始化大语言模型 (默认使用 GPT-4o 或 GPT-4-turbo 以保证长链推理能力)
llm = ChatOpenAI(model_name="gpt-4-turbo", temperature=0.3)

# 1. 检索 Agent
searcher_agent = Agent(
    role='资深行业资料检索员',
    goal='根据行业主题，全面检索近一个月的最新新闻、财报和行业数据。',
    backstory='你是一个拥有极强信息搜集能力的情报专家。你擅长使用搜索引擎抓取碎片化信息，绝不遗漏关键数据。',
    verbose=True,
    allow_delegation=False,
    tools=[web_search_tool],
    llm=llm
)

# 2. 分析 Agent (包含长链推理)
analyst_agent = Agent(
    role='高级金融投研分析师',
    goal='对原始文本进行深度清洗、去重，利用长链推理提炼核心趋势观点。',
    backstory='你精通商业逻辑和数据分析。你会运用 Chain of Thought (思维链) 的方式，一步步剖析庞杂的商业信息，找出行业风口和潜在风险。',
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# 3. 审核 Agent (Fact-Checking)
reviewer_agent = Agent(
    role='独立事实核查员 (Fact-Checker)',
    goal='对分析师提取的数据进行事实核查，剔除冲突信息和不可靠的来源。',
    backstory='你极其严谨，对数字和逻辑高度敏感。你的职责是确保研报中引用的数据准确无误，逻辑自洽，不允许出现虚假幻觉 (Hallucination)。',
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# 4. 撰写 Agent
writer_agent = Agent(
    role='首席研报撰写主笔',
    goal='将核查后的核心观点和数据，按照标准金融研报格式输出万字长文（结构化 Markdown）。',
    backstory='你是一位资深财经主笔，文笔专业、客观、严谨。你擅长将复杂的数据转化为通俗易懂且极具洞察力的长篇研报，结构清晰，排版精美。',
    verbose=True,
    allow_delegation=False,
    llm=llm
)