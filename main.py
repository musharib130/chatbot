from langchain_core.messages import HumanMessage
from rich.console import Console
from app.graph import build_graph

console = Console()
graph = build_graph()

# Initialize conversation state
state = {"messages": []}

console.print("[bold green]LangGraph CLI Chatbot[/bold green]")
console.print("Type 'exit' to quit.\n")

while True:
    user_input = console.input("[bold blue]You:[/bold blue] ")

    if user_input.lower() == "exit":
        break

    # Append user message to state
    state["messages"].append(HumanMessage(content=user_input))

    # Invoke LangGraph
    state = graph.invoke(state)

    # Print AI response
    ai_message = state["messages"][-1].content
    console.print(f"[bold magenta]Bot:[/bold magenta] {ai_message}")
