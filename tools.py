from langchain_community.tools import DuckDuckGoSearchResults
from langchain.tools import Tool

# 实例化联网搜索工具
search_tool = DuckDuckGoSearchResults()

# 封装为 CrewAI 可用的 Tool
web_search_tool = Tool(
    name="Web Search",
    func=search_tool.run,
    description="用于在互联网上搜索最新的行业新闻、财报数据和研报信息。"
)