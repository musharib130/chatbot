from langchain_core.messages import HumanMessage
from rich.console import Console
from app.graph import build_graph
from app.state import ChatState
import asyncio

console = Console()
graph = build_graph()

console.print("[bold green]LangGraph CLI Chatbot[/bold green]")
console.print("Type 'exit' to quit.\n")

state = ChatState(
    messages=[]
)

async def fun():
    while True:
        user_input = console.input("[bold blue]You:[/bold blue] ")

        if user_input.lower() == "exit":
            break

        # Append user message to state
        state["messages"].append(HumanMessage(content=user_input))

        events = graph.astream_events(input=state, version="v2")

        console.print("[bold magenta]Bot:[/bold magenta]", end="")

        async for event in events:    
            if event['event'] == 'on_llm_stream':
                print(event['data']['chunk'].text, end="", flush=True)

        print()


asyncio.run(fun())
