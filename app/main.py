from app.graph import build_graph

if __name__ == "__main__":
    graph = build_graph()

    user_input = input("Ask something: ")
    result = graph.invoke({"input": user_input})

    print("\nResponse:\n")
    print(result["output"])
