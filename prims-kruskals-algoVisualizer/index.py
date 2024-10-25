
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import networkx as nx
import matplotlib.pyplot as plt
import time

class GraphVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Graph Visualizer")
        # Set the fixed size of the window
        self.root.geometry("450x400")  # Width x Height

        # Disable resizing the window
        self.root.resizable(False, False)
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Input Format", menu=self.file_menu)
        self.file_menu.add_command(label="Prims and Kruskals Algo", command=self.explain)
        self.file_menu.add_command(label="Adjacency List", command=self.adjacency_list_input)
        self.file_menu.add_command(label="{start} {end} {weight}", command=self.adjacency_list_input)
        self.file_menu.add_command(label="Credits", command=self.creditsWindow)
        # self.file_menu.add_command(label="Visualize Delay : 0s", command=self.delay_update(0))
        # self.file_menu.add_command(label="Visualize Delay : 1s", command=self.delay_update(1))
        # self.file_menu.add_command(label="Visualize Delay : 1.5s[default]", command=self.delay_update(1.5))
        # self.file_menu.add_command(label="Visualize Delay : 2s", command=self.delay_update(2))

        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.delay = 1.5
    def create_scrollable_label(self):
        frame = ttk.Frame(self.root)
        frame.grid(row=0, column=0, sticky='nsew')

        canvas = tk.Canvas(frame)
        canvas.grid(row=0, column=0, sticky='nsew')

        v_scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
        v_scrollbar.grid(row=0, column=1, sticky='ns')
        h_scrollbar = ttk.Scrollbar(frame, orient=tk.HORIZONTAL, command=canvas.xview)
        h_scrollbar.grid(row=1, column=0, sticky='ew')

        scrollable_frame = ttk.Frame(canvas)
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        

    # Configure canvas scroll commands
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

        text = """Minimum Spanning Tree (MST) is a fundamental concept in graph theory and has various applications in network design, clustering, and optimization problems. Two of the most commonly used algorithms to find the MST of a graph are Prim’s and Kruskal’s algorithms. Although both algorithms achieve the same goal, they do so in different ways. In this article we are going to explore the differences between them which can help in choosing the right algorithm for specific types of graphs and applications.
        
        Prim’s Algorithm:
        Prim’s algorithm is a greedy algorithm that builds the MST incrementally. It starts with a single vertex and grows the MST one edge at a time, always choosing the smallest edge that connects a vertex in the MST to a vertex outside the MST.
        
        Steps of Prim’s Algorithm:
        1. Initialization: Start with an arbitrary vertex and mark it as part of the MST.
        2. Edge Selection: From the set of edges that connect vertices in the MST to vertices outside the MST, select the edge with the minimum weight.
        3. Update: Add the selected edge and the connected vertex to the MST.
        4. Repeat: Repeat the edge selection and update steps until all vertices are included in the MST.
        
        Prim’s algorithm is typically implemented using a priority queue to efficiently select the minimum weight edge at each step.
        
        Kruskal’s Algorithm:
        Kruskal’s algorithm is also a greedy algorithm but takes a different approach. It begins with all the vertices and no edges, and it adds edges one by one in increasing order of weight, ensuring no cycles are formed until the MST is complete.
        
        Steps of Kruskal’s Algorithm:
        1. Initialization: Sort all the edges in the graph by their weight in non-decreasing order.
        2. Edge Selection: Starting from the smallest edge, add the edge to the MST if it doesn’t form a cycle with the already included edges.
        3. Cycle Detection: Use a union-find data structure to detect and prevent cycles.
        4. Repeat: Continue adding edges until the MST contains exactly (V-1) edges, where V is the number of vertices."""

        label = ttk.Label(scrollable_frame, text=text, wraplength=760, justify=tk.LEFT)
        
        label.grid(row=0, column=0, padx=10, pady=10)
    def explain(self):
        self.clear_frame()
        
        self.create_scrollable_label()



    def delay_update(self,updater):
        self.delay = updater
    def creditsWindow(self):
        self.clear_frame()
        input_label1 = ttk.Label(self.main_frame, text=f"CreatedBy : Rushikesh Iche ©2024")
        input_label1.grid(row=1, column=2, pady=10)
        input_label2 = ttk.Label(self.main_frame, text=f"Used Libraries in Python:" )
        input_label2.grid(row=2, column=2, pady=10)
        input_label3 = ttk.Label(self.main_frame, text=f" 1.NetworkX ")
        input_label3.grid(row=3, column=2, pady=10)
        input_label4 = ttk.Label(self.main_frame, text=f" 2.Tkinter ")
        input_label4.grid(row=4, column=2, pady=10)
        input_label5 = ttk.Label(self.main_frame, text=f" 3.Time " )
        input_label5.grid(row=5, column=2, pady=10)
        input_label6 = ttk.Label(self.main_frame, text=f" 4.MatplotLib ")
        input_label6.grid(row=6, column=2, pady=10)
       
       
        
       
   

    def adjacency_list_input(self):
        self.clear_frame()
        self.add_input_fields("List")
        
    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
    
    def add_input_fields(self, input_type):
        

        input_label = ttk.Label(self.main_frame, text=f"Input the {input_type} here:")
        input_label.grid(row=0, column=0, pady=10)
        
        self.text_area = tk.Text(self.main_frame, width=50, height=10)
        self.text_area.grid(row=1, column=0, pady=10)
        
        self.visualize_button = ttk.Button(self.main_frame, text="Visualize Graph", command=self.visualize_graph)
        self.visualize_button.grid(row=2, column=0, pady=5)

        self.prims_button = ttk.Button(self.main_frame, text="Visualize using Prim's Algorithm", command=self.visualize_prims)
        self.prims_button.grid(row=3, column=0, pady=5)
        
        self.kruskals_button = ttk.Button(self.main_frame, text="Visualize using Kruskal's Algorithm", command=self.visualize_kruskals)
        self.kruskals_button.grid(row=4, column=0, pady=5)

        instructions = ttk.Label(self.main_frame, text="Enter each edge as 'u v w' on a new line for adjacency list.")
        instructions.grid(row=5, column=0, pady=10)
        
    def visualize_graph(self):
        graph_data = self.text_area.get("1.0", tk.END)
        graph = self.parse_input(graph_data)
        if graph:
            G = nx.Graph()
            for u, v, w in graph:
                G.add_edge(u, v, weight=w)
            pos = nx.spring_layout(G)
            self.show_graph(G, pos, "Original Graph")
    
    def visualize_prims(self):
        graph_data = self.text_area.get("1.0", tk.END)
        graph = self.parse_input(graph_data)
        if graph:
            self.prims_algorithm(graph)

    def visualize_kruskals(self):
        graph_data = self.text_area.get("1.0", tk.END)
        graph = self.parse_input(graph_data)
        if graph:
            self.kruskals_algorithm(graph)
    
    def parse_input(self, data):
        lines = data.strip().split('\n')
        graph = []
        try:
            for line in lines:
                u, v, w = map(int, line.split())
                graph.append((u, v, w))
            return graph
        except ValueError:
            messagebox.showerror("Input Error", "Invalid input format. Please enter each edge as 'u v w' on a new line.")
            return None

    def show_graph(self, G, pos, title):
        plt.clf()
        nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue')
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        plt.title(title)
        plt.show()
        plt.pause(self.delay)

    def prims_algorithm(self, graph):
        G = nx.Graph()
        for u, v, w in graph:
            G.add_edge(u, v, weight=w)

        pos = nx.spring_layout(G)
        mst_edges = []
        mst_set = set()
        start_node = next(iter(G.nodes))
        mst_set.add(start_node)

        plt.ion()
        plt.figure()

        while len(mst_set) < len(G.nodes):
            crossing = []
            for u in mst_set:
                for v, weight in G[u].items():
                    if v not in mst_set:
                        crossing.append((u, v, weight['weight']))

            edge = min(crossing, key=lambda e: e[2])
            mst_edges.append(edge)
            mst_set.add(edge[1])

            G_mst = nx.Graph()
            G_mst.add_weighted_edges_from(mst_edges)
            self.show_graph(G_mst, pos, "Prim's Algorithm")
            time.sleep(self.delay)  # 1.5-second delay to visualize each step

        plt.ioff()
        plt.show()

    def kruskals_algorithm(self, graph):
        G = nx.Graph()
        for u, v, w in graph:
            G.add_edge(u, v, weight=w)

        pos = nx.spring_layout(G)
        edges = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
        mst_edges = []
        mst_set = {node: node for node in G.nodes}

        def find(node):
            while mst_set[node] != node:
                node = mst_set[node]
            return node

        def union(u, v):
            root_u = find(u)
            root_v = find(v)
            mst_set[root_u] = root_v

        plt.ion()
        plt.figure()

        for u, v, weight in edges:
            if find(u) != find(v):
                mst_edges.append((u, v, weight['weight']))
                union(u, v)

                G_mst = nx.Graph()
                G_mst.add_weighted_edges_from(mst_edges)
                self.show_graph(G_mst, pos, "Kruskal's Algorithm")
                time.sleep(self.delay)  # 1.5-second delay to visualize each step

        plt.ioff()
        plt.show()

def main():
    root = tk.Tk()
    app = GraphVisualizer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
