from langchain_core.messages import HumanMessage, AIMessage
from rich.console import Console
from app.graph import build_graph
from app.state import ChatState
import asyncio

console = Console()

console.print("[bold green]LangGraph CLI Chatbot[/bold green]")
console.print("Type 'exit' to quit.\n")

state = ChatState(
    messages=[]
)

async def fun():
    while True:
        graph = build_graph()
        
        user_input = console.input("[bold blue]You:[/bold blue] ")

        if user_input.lower() == "exit":
            break

        # Append user message to state
        state["messages"].append(HumanMessage(content=user_input))

        events = graph.astream_events(input=state, version="v2")

        console.print("[bold magenta]Bot:[/bold magenta]", end="")

        ai_res = ""

        async for event in events:
            if event['event'] == 'on_tool_start':
                print(f"Using {event['name']} with data => {event['data']['input']}")

            if event['event'] == 'on_chat_model_stream':
                text = event['data']['chunk'].text
                
                ai_res += text
                print(text, end="", flush=True)
            # else:
            #     print(event["event"], end="\n\n") 


        state["messages"].append(AIMessage(ai_res))
        print()
        # print(f'\n {state} \n')


asyncio.run(fun())
