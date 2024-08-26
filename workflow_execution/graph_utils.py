def is_link(obj):
    if not isinstance(obj, list):
        return False
    if len(obj) != 2:
        return False
    if not isinstance(obj[0], str):
        return False
    if not isinstance(obj[1], int) and not isinstance(obj[1], float):
        return False
    return True


class GraphBuilder:
    _default_prefix_root = ""
    _default_prefix_call_index = 0
    _default_prefix_graph_index = 0

    def __init__(self, prefix=None):
        if prefix is None:
            self.prefix = GraphBuilder.alloc_prefix()
        else:
            self.prefix = prefix
        self.nodes = {}
        self.id_gen = 1

    @classmethod
    def set_default_prefix(cls, prefix_root, call_index, graph_index=0):
        cls._default_prefix_root = prefix_root
        cls._default_prefix_call_index = call_index
        cls._default_prefix_graph_index = graph_index

    @classmethod
    def alloc_prefix(cls, root=None, call_index=None, graph_index=None):
        if root is None:
            root = GraphBuilder._default_prefix_root
        if call_index is None:
            call_index = GraphBuilder._default_prefix_call_index
        if graph_index is None:
            graph_index = GraphBuilder._default_prefix_graph_index
        result = f"{root}.{call_index}.{graph_index}."
        GraphBuilder._default_prefix_graph_index += 1
        return result

    def node(self, class_type, id=None, **kwargs):
        if id is None:
            id = str(self.id_gen)
            self.id_gen += 1
        id = self.prefix + id
        if id in self.nodes:
            return self.nodes[id]

        node = Node(id, class_type, kwargs)
        self.nodes[id] = node
        return node

    def lookup_node(self, id):
        id = self.prefix + id
        return self.nodes.get(id)

    def finalize(self):
        output = {}
        for node_id, node in self.nodes.items():
            output[node_id] = node.serialize()
        return output

    def replace_node_output(self, node_id, index, new_value):
        node_id = self.prefix + node_id
        to_remove = []
        for node in self.nodes.values():
            for key, value in node.inputs.items():
                if is_link(value) and value[0] == node_id and value[1] == index:
                    if new_value is None:
                        to_remove.append((node, key))
                    else:
                        node.inputs[key] = new_value
        for node, key in to_remove:
            del node.inputs[key]

    def remove_node(self, id):
        id = self.prefix + id
        del self.nodes[id]
