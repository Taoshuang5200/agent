from crewai import Task
from agents import searcher_agent, analyst_agent, reviewer_agent, writer_agent

def create_tasks(topic):
    # 任务 1：检索信息
    task_search = Task(
        description=f'使用搜索引擎查找关于【{topic}】的最新行业资讯、市场规模、竞争格局和头部公司动态。收集至少 5 条有价值的核心信息。',
        expected_output='一份包含原始数据、新闻摘要和信息来源链接的汇总文档。',
        agent=searcher_agent
    )

    # 任务 2：深度分析
    task_analyze = Task(
        description=f'基于检索到的关于【{topic}】的信息，使用思维链(CoT)方法进行深度推理：1.归纳核心趋势；2.分析驱动因素；3.总结头部企业的战略。去除重复的口水话。',
        expected_output='一份逻辑严密的行业深度分析简报，包含趋势洞察和核心数据支撑。',
        agent=analyst_agent
    )

    # 任务 3：事实核查
    task_review = Task(
        description='仔细审查分析师产出的简报。检查是否有自相矛盾的逻辑？数据是否有明显夸大或不合理之处？如果发现问题，请进行修正或批注。',
        expected_output='一份经过严格事实核查、剔除了冲突信息的最终版数据与观点清单。',
        agent=reviewer_agent
    )

    # 任务 4：研报撰写
    task_write = Task(
        description=f'基于核查后的清单，撰写一篇关于【{topic}】的标准金融深度研报。必须包含：1. 核心摘要；2. 行业宏观背景；3. 市场规模与趋势；4. 竞争格局分析；5. 投资风险提示。',
        expected_output='一篇专业、客观、采用 Markdown 格式排版的深度研报。字数尽量详实。',
        agent=writer_agent,
        output_file=f'output_report_{topic}.md'  # 最终输出为文件
    )
    
    return [task_search, task_analyze, task_review, task_write]