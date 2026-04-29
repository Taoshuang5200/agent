from crewai import Crew, Process
from tasks import create_tasks
from agents import searcher_agent, analyst_agent, reviewer_agent, writer_agent

def generate_report(topic: str):
    print(f"\n=============================================")
    print(f"🚀 开始启动自动化研报生成系统：主题【{topic}】")
    print(f"=============================================\n")

    # 获取针对该主题的任务流
    tasks = create_tasks(topic)

    # 组装 Crew (团队)
    # process=Process.sequential 表示任务按照 检索->分析->审核->撰写 的顺序线性执行
    research_crew = Crew(
        agents=[searcher_agent, analyst_agent, reviewer_agent, writer_agent],
        tasks=tasks,
        process=Process.sequential, 
        verbose=True
    )

    # 启动工作流
    result = research_crew.kickoff()

    print("\n=============================================")
    print("✅ 研报生成完毕！请查看项目目录下的 output_report_xxx.md 文件。")
    print("=============================================\n")
    return result

if __name__ == "__main__":
    # 你可以在这里修改你想要研究的行业主题
    target_topic = "2024年全球人形机器人行业发展"
    generate_report(target_topic)