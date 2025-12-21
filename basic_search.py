from crewai import Agent, Task, Crew, LLM
from crewai_tools import WebsiteSearchTool
from dotenv import load_dotenv

load_dotenv()

llm = LLM(model="gpt-4o-mini")

def summarize_url(url: str) -> str:
    tool = WebsiteSearchTool(website=url)

    agent = Agent(
        role="Article Summarizer",
        goal="Gather comprehensive information from the provided article and summarize it in no more than 100 words.",
        backstory="You are an article summarizer with a passion for finding information on the web.",
        tools=[tool],
        llm=llm,
        verbose=True
    )

    task = Task(
        description=f"Search this article and provide a summary in <= 100 words:\n{url}",
        agent=agent,
        expected_output="A comprehensive summary of the article in no more than 100 words."
    )

    crew = Crew(agents=[agent], tasks=[task])
    result = crew.kickoff()
    return str(result)

if __name__ == "__main__":
    url = input("Paste an article link you need to summarize: ").strip()
    print(summarize_url(url))
