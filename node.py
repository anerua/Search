from tree import tree


class node:
    name = ''
    status = 3

    def get_connected_nodes(self, tr):
        nodes = []
        for edge in tr.points:

            if edge.line[0] is self:
                nodes.append(edge.line[1])
            elif edge.line[1] is self:
                nodes.append(edge.line[0])
        return nodes

    def get_path_length(self, node2, tr):
        path_length = 0

        for edge in tr.points:
            if ((edge.line[0].name == self.name) and (edge.line[1].name == node2.name)) or (
                    (edge.line[0].name == node2.name) and (edge.line[1].name == self.name)):
                path_length = edge.line[2]
                break;
        return path_length
