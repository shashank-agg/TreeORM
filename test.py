from Tree import Tree
# t1 = Tree()
# t1.addAttribute("name", "Shashank")
# t1.addAttribute("roll", "12co82")
# t1.getAttributes()

class MyTree(Tree):
    def __init__(self):
        super(MyTree, self).__init__()
        self.addAttribute("name", "Shashank","CHAR(20)",["NOT NULL"])
        self.addAttribute("roll_no", 82,"INT",[])

t = MyTree()
t.createTable("familytree")
