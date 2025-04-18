from graph import build_graph
import os

def read_document(file_path: str) -> str:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return ""
if 

if __name__ == "__main__":
    # file_path = input("Enter").strip()    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    print(base_dir)
    document_path = os.path.join(base_dir, "document.txt")
    document = read_document(document_path)

    if document:
        graph = build_graph()
        result = graph.invoke({"document": document})
        print("\n--- FINAL RESULT ---\n")
        print(result)

